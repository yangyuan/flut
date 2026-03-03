import sys

CODE_FONT_FAMILY = (
    "Menlo"
    if sys.platform == "darwin"
    else "Consolas" if sys.platform == "win32" else "monospace"
)
