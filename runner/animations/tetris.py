import sys
import time

from runner import CY, Y, G, DIM, BOLD, RST
from runner.i18n import t

_W = 12  # board inner width

# Pre-built frames: piece (##/##) drops from top, fills a line
_FRAMES = [
    [" ##  ",
     " ##  ",
     "     ",
     "     ",
     "     ",
     "## ##",
     "#####"],

    ["     ",
     " ##  ",
     " ##  ",
     "     ",
     "     ",
     "## ##",
     "#####"],

    ["     ",
     "     ",
     " ##  ",
     " ##  ",
     "     ",
     "## ##",
     "#####"],

    ["     ",
     "     ",
     "     ",
     " ##  ",
     " ##  ",
     "## ##",
     "#####"],

    ["     ",
     "     ",
     "     ",
     "     ",
     " ##  ",
     "####-",   # piece landing — incomplete row
     "#####"],

    ["     ",
     "     ",
     "     ",
     "     ",
     "     ",
     "#####",   # line complete!
     "#####"],
]

_DELAYS = [0.12, 0.12, 0.12, 0.12, 0.18, 0.5]

_H = len(_FRAMES[0])


def _render(content: list[str], flash: bool = False) -> None:
    border = CY if not flash else Y
    for row in content:
        sys.stdout.write(f'\r\033[K  {border}|{RST}{BOLD}{row}{RST}{border}|{RST}\n')
    sys.stdout.write(f'\r\033[K  {border}{"=" * (len(content[0]) + 2)}{RST}\n')


def play() -> None:
    total_lines = _H + 1  # board + border

    sys.stdout.write('\n' * total_lines)
    sys.stdout.flush()

    for i, (frame, delay) in enumerate(zip(_FRAMES, _DELAYS)):
        sys.stdout.write(f'\033[{total_lines}A')
        _render(frame, flash=(i == len(_FRAMES) - 1))
        sys.stdout.flush()
        time.sleep(delay)

    # Flash "LINE CLEAR"
    for _ in range(3):
        sys.stdout.write(f'\033[{total_lines}A')
        _render(['     '] * (_H - 1) + ['#####'], flash=True)
        sys.stdout.flush()
        time.sleep(0.12)
        sys.stdout.write(f'\033[{total_lines}A')
        _render(['     '] * (_H - 1) + ['     '], flash=False)
        sys.stdout.flush()
        time.sleep(0.12)

    sys.stdout.write(f'\r\033[K  {G}{BOLD}{t("anim.tetris.clear")}{RST}\n')
    sys.stdout.flush()
    time.sleep(1.0)
