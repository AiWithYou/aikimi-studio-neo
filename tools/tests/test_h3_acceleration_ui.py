"""Real Gradio callback/config checks; no backend process or GPU is started."""
from __future__ import annotations

import asyncio
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from types import ModuleType
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.tests.test_h3_acceleration import H3Acceleration, load_bridge  # noqa: E402


def load_ui(directory: str):
    bridge = load_bridge()
    package = ModuleType("modules")
    package.__path__ = []
    callbacks = ModuleType("modules.script_callbacks")
    callbacks.on_ui_tabs = lambda *args, **kwargs: None
    paths = ModuleType("modules.paths")
    paths.script_path = paths.data_path = directory
    package.script_callbacks = callbacks
    spec = importlib.util.spec_from_file_location("_h3_acceleration_ui_test", ROOT / "extensions-builtin/minimax-h3-studio/scripts/minimax_h3_studio.py")
    ui = importlib.util.module_from_spec(spec)
    with patch.dict(sys.modules, {
        "modules": package, "modules.script_callbacks": callbacks, "modules.paths": paths,
        "modules_forge.minimax_h3_bridge": bridge,
    }):
        spec.loader.exec_module(ui)
    return ui


class H3AccelerationUITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.ui = load_ui(cls.temp.name)
        cls.demo = cls.ui._build_ui()[0][0]
        cls.by_id = {component.elem_id: component for component in cls.demo.blocks.values() if getattr(component, "elem_id", None)}

    @classmethod
    def tearDownClass(cls):
        cls.demo.close()
        cls.temp.cleanup()

    def callback(self, name):
        return next((index, fn) for index, fn in self.demo.fns.items() if fn.fn.__name__ == name)

    def test_four_choices_default_to_standard_and_are_initially_locked(self):
        for name, value in (("h3-model-variant", "base"), ("h3-video-vae", "fp16"), ("h3-decode-mode", "standard"), ("h3-attention-mode", "dense")):
            control = self.by_id[name]
            self.assertEqual(control.value, value)
            self.assertFalse(control.interactive)
        _, initial = self.callback("_initial_ui_with_acceleration")
        self.assertEqual(len(initial.outputs), 32)
        with patch.object(self.ui, "_initial_ui_updates", return_value=tuple(range(21))):
            result = initial.fn("", "http://127.0.0.1:8188", "fast", "16:9")
        self.assertEqual(len(result), 32)
        self.assertTrue(all(value["interactive"] for value in result[21:]))

    def test_turbo_buttons_preserve_all_other_acceleration_axes(self):
        for name, steps in (("_turbo_four_updates", 4), ("_turbo_eight_updates", 8)):
            index, fn = self.callback(name)
            self.assertEqual([item.elem_id for item in fn.outputs][:3], ["h3-model-variant", "h3-steps", "h3-scheduler"])
            result = asyncio.run(self.demo.process_api(index, ["16:9", "native", 10.0, "match"]))
            data = result["data"]
            self.assertEqual(data[:3], ["fused_turbo", steps, "simple"])
            self.assertIn(f"{steps} steps", data[3])
            self.assertEqual(len(data), 5)

    def test_standard_reset_clears_every_acceleration_and_restores_twenty_steps(self):
        index, fn = self.callback("_reset_acceleration_updates")
        result = asyncio.run(self.demo.process_api(index, ["9:16", "preview", 5.0, "match"]))
        data = result["data"]
        self.assertEqual(tuple(data[:8]), H3Acceleration().values())
        self.assertEqual(data[8:10], [20, "simple"])
        self.assertEqual(len(fn.outputs), 12)

    def test_runtime_and_generation_consume_the_same_eight_controls(self):
        for name, count in (("_generate", 25), ("_connect_runtime_updates", 11), ("_restart_runtime_updates", 11), ("_rescan_runtime_updates", 11)):
            _, fn = self.callback(name)
            self.assertEqual(len(fn.inputs), count)
            self.assertEqual([item.elem_id for item in fn.inputs][-8:], ["h3-model-variant", "h3-video-vae", "h3-decode-mode", "h3-tile-batch", "h3-attention-mode", "h3-sparse-tau", "h3-sparse-keep", "h3-sparse-start"])
        args = ["text", "test", None, None, None, None, None, "16:9", "preview", 5, 4, 42, "simple", "match"]
        chosen = H3Acceleration("fused_turbo", "int8", "fast", 2, "sla")
        request = self.ui._request_from_ui(*args, *chosen.values())
        self.assertEqual(request.acceleration, chosen)
        self.assertEqual(self.ui._request_from_ui(*args).acceleration, H3Acceleration())

    def test_history_restores_acceleration_but_never_input_media(self):
        chosen = H3Acceleration("fused_turbo", "int8", "fast", 2, "sla")
        request = self.ui.H3Request(mode="references", prompt="<Picture 1>", acceleration=chosen, steps=4)
        with patch.object(self.ui, "_history_state", return_value=([], "", [])), patch.object(self.ui, "load_history_request", return_value=request):
            result = self.ui._restore_history_with_acceleration("id", "")
        self.assertEqual(len(result), 30)
        self.assertTrue(all(value["value"] is None for value in result[2:7]))
        self.assertEqual(tuple(value["value"] for value in result[22:]), chosen.values())
        self.assertIn("custom", result[19]["value"])
        failure = self.ui._restore_history_with_acceleration("", "")
        self.assertEqual(len(failure), 30)
        self.assertTrue(all("value" not in value for value in failure[22:]))


if __name__ == "__main__":
    unittest.main()
