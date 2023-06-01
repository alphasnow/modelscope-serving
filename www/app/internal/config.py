import os
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent.parent.resolve()
APP_PATH = os.path.join(ROOT_PATH, "app")
LOG_PATH = os.path.join(ROOT_PATH, "logs")
