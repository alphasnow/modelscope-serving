import os

from app.internal.config import APP_PATH


def stub(file: str):
    return os.path.join(APP_PATH, "tests/stub", file)
