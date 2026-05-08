import os
import random
import sys
import time

from runner import Y, CY, BOLD, RST
from runner.i18n import t

_UP  = lambda n: f'\033[{n}A'
_CLR = '\r\033[K'

_CAR = [
    r"     .----------.",
    r" ___/ OUTATIME   \__",
    r"|                   |",
    r"|___________________|",
    r"  (o)           (o) ",
]
_CAR_H = len(_CAR)
_CAR_W = max(len(l) for l in _CAR)
_MID   = _CAR_H // 2

_FIRE   = ['~^~', '^~^', '~~~', '*^*', '~*~']
_SPEEDS = ['==>', '===>', '====>', '======>']


def play() -> None:
    try:
        cols = os.get_terminal_size().columns
    except OSError:
        cols = 80

    max_pos  = max(cols - _CAR_W - 10, 20)
    fire_len = 3

    sys.stdout.write('\n' * _CAR_H)
    sys.stdout.flush()

    for pos in range(0, max_pos, 2):
        sys.stdout.write(_UP(_CAR_H))

        pct  = pos / max_pos
        spd  = _SPEEDS[min(int(pct * len(_SPEEDS)), len(_SPEEDS) - 1)]
        fire = random.choice(_FIRE)

        for i, line in enumerate(_CAR):
            if pos < fire_len:
                row = ' ' * pos + line
                if i == _MID:
                    row += CY + spd + RST
            else:
                lead = ' ' * (pos - fire_len)
                if i == _MID:
                    row = lead + Y + fire + RST + line + CY + spd + RST
                else:
                    row = ' ' * pos + line

            sys.stdout.write(_CLR + row[:cols] + '\n')

        sys.stdout.flush()
        time.sleep(0.035)

    sys.stdout.write(_CLR + f'  {Y}{BOLD}{t("anim.delorean.finale")}{RST}\n')
    sys.stdout.flush()
    time.sleep(1.2)
