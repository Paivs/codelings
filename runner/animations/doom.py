import sys
import time

from runner import R, G, Y, CY, BOLD, DIM, RST
from runner.i18n import t

_FACES = [
    (
        ["  .----.",
         " | -  - |",
         " |  __  |",
         " | |__| |",
         "  '----' "],
        'anim.doom.0', DIM, 0.5,
    ),
    (
        ["  .----.",
         " | o  o |",
         " |  __  |",
         " | |  | |",
         "  '----' "],
        'anim.doom.1', Y, 0.5,
    ),
    (
        ["  .----.",
         " | O  O |",
         " | /--\\ |",
         " |      |",
         "  '----' "],
        'anim.doom.2', CY, 0.6,
    ),
    (
        ["  .----.",
         " | ^  ^ |",
         " |  --  |",
         " | \\__/ |",
         "  '----' "],
        'anim.doom.3', R, 0.7,
    ),
    (
        ["  .----.",
         " | *  * |",
         " |  vv  |",
         " | \\__/ |",
         "  '----' "],
        'anim.doom.4', G, 0.0,
    ),
]

_H = len(_FACES[0][0]) + 2


def play() -> None:
    sys.stdout.write('\n' * _H)
    sys.stdout.flush()

    for art, caption_key, color, delay in _FACES:
        sys.stdout.write(f'\033[{_H}A')
        for line in art:
            sys.stdout.write(f'\r\033[K  {color}{BOLD}{line}{RST}\n')
        sys.stdout.write(f'\r\033[K\n')
        sys.stdout.write(f'\r\033[K  {color}{t(caption_key)}{RST}\n')
        sys.stdout.flush()
        time.sleep(0.5)
        if delay:
            time.sleep(delay)

    time.sleep(1.0)
