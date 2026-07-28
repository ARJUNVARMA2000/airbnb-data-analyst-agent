import os

DEFAULT_MODEL_ID = "google/gemini-2.5-flash"
DEFAULT_MODEL = os.environ.get("AGENT_MODEL", DEFAULT_MODEL_ID)
