import sys
import os
from pathlib import Path

_ROOT = str(Path(__file__).resolve().parent.parent.parent)

_SRC = os.path.join(_ROOT, "src")
_ASSETS = os.path.join(_SRC, "assets")

# summary about paths
PATHS = {
    "root": _ROOT,
    "src": _SRC,
    "assets": _ASSETS,
    "image": os.path.join(_ASSETS, "image"),
    "test_output": os.path.join(_ROOT, "test_output"),
}

if __name__ == "__main__":
    print(PATHS)