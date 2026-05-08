import os
import random
import sys
import time

from runner import BOLD, RST
from runner.i18n import t

_G  = '\033[32m'
_GB = '\033[92m'
_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%&!?'


def play() -> None:
    try:
        cols = min(os.get_terminal_size().columns, 78)
        rows = min(os.get_terminal_size().lines - 4, 10)
    except OSError:
        cols, rows = 78, 10

    tail   = 6
    heads  = [random.randint(-rows, 0) for _ in range(cols)]
    frames = rows + tail + 8

    sys.stdout.write('\n' * rows)
    sys.stdout.flush()

    for frame in range(frames):
        sys.stdout.write(f'\033[{rows}A')
        for row in range(rows):
            line = ''
            for col in range(cols):
                h = heads[col]
                if row == h:
                    line += _GB + random.choice(_CHARS) + RST
                elif h - tail < row < h:
                    line += _G + random.choice(_CHARS) + RST
                else:
                    line += ' '
            sys.stdout.write('\r' + line + '\n')

        for i in range(len(heads)):
            heads[i] += 1
            if heads[i] > rows + tail:
                heads[i] = random.randint(-rows, -1)

        sys.stdout.flush()
        time.sleep(0.055)

    sys.stdout.write(f'\r\033[K  {_GB}{BOLD}{t("anim.matrix.finale")}{RST}\n')
    sys.stdout.flush()
    time.sleep(1.1)
