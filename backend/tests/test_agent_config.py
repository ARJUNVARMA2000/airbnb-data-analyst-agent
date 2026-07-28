import os
import unittest
from unittest.mock import patch

from agent_defs import config


class AgentConfigTests(unittest.TestCase):
    def test_default_model_is_supported_vertex_model(self):
        self.assertEqual(config.DEFAULT_MODEL_ID, "google/gemini-2.5-flash")

    def test_agent_model_environment_override_is_preserved(self):
        with patch.dict(os.environ, {"AGENT_MODEL": "google/gemini-2.5-pro"}):
            selected_model = os.environ.get("AGENT_MODEL", config.DEFAULT_MODEL_ID)

        self.assertEqual(selected_model, "google/gemini-2.5-pro")


if __name__ == "__main__":
    unittest.main()
