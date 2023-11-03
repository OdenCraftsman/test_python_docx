import sys
import os
from pathlib import Path

if getattr(sys, 'frozen', False):
    # 実行ファイル実行時の処理
    _ROOT = sys._MEIPASS
else:
    # スクリプト実行時の処理
    _ROOT = str(Path(__file__).resolve().parent.parent.parent)

_SRC = os.path.join(_ROOT, "src")
_ASSETS = os.path.join(_SRC, "assets")

# summary about paths
PATHS = {
    "root": _ROOT,
    "src": _SRC,
    "assets": _ASSETS,
    "image": os.path.join(_ASSETS, "image"),
    "doors_logo": os.path.join(_ASSETS, "image", "doors_logo.jpg"),
}

if __name__ == "__main__":
    print(PATHS)