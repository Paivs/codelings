import math
import os
import sys
import time

from runner import Y, CY, G, W, BOLD, DIM, RST
from runner.i18n import t

_DENSITY = ' .·:+*#@'


def play() -> None:
    try:
        cols = min(os.get_terminal_size().columns - 2, 60)
        rows = min(os.get_terminal_size().lines - 4, 14)
    except OSError:
        cols, rows = 60, 14

    # Make even for centering
    cols = cols if cols % 2 == 0 else cols - 1
    rows = rows if rows % 2 == 0 else rows - 1

    cx = cols / 2
    cy = rows / 2
    max_r = math.sqrt(cx ** 2 + (cy * 2) ** 2)  # *2 to correct char aspect ratio

    colors = [DIM, CY, G, Y, W, BOLD + W]
    total  = 18

    # Intro
    mid_row = '\n' * (rows // 2)
    sys.stdout.write(mid_row)
    sys.stdout.write(f'\r\033[K  {DIM}{t("anim.bigbang.intro")}{RST}\n')
    sys.stdout.flush()
    time.sleep(1.8)

    # Clear intro and reserve space
    sys.stdout.write(f'\033[{rows // 2 + 1}A')
    sys.stdout.write('\n' * (rows + 1))
    sys.stdout.flush()

    for frame in range(total):
        sys.stdout.write(f'\033[{rows + 1}A')
        radius = (frame / (total - 1)) * max_r
        color  = colors[min(frame * len(colors) // total, len(colors) - 1)]

        for row in range(rows):
            line = ''
            for col in range(cols):
                # Correct for terminal char aspect ratio (~2:1 h:w)
                d = math.sqrt((col - cx) ** 2 + ((row - cy) * 2) ** 2)
                inner = radius - 4
                if d <= radius:
                    if d >= inner:
                        idx = max(0, int((d / max_r) * (len(_DENSITY) - 1)))
                        line += _DENSITY[idx]
                    else:
                        # fading interior
                        idx = max(0, int(((frame - 2) / total) * (len(_DENSITY) - 1)))
                        line += _DENSITY[idx] if frame > 4 else ' '
                else:
                    line += ' '

            sys.stdout.write(f'\r\033[K {color}{line}{RST}\n')

        sys.stdout.write(f'\r\033[K\n')
        sys.stdout.flush()
        time.sleep(0.07)

    sys.stdout.write(f'\033[{rows + 1}A')
    for _ in range(rows):
        sys.stdout.write(f'\r\033[K\n')
    sys.stdout.write(f'\r\033[K  {Y}{BOLD}{t("anim.bigbang.finale")}{RST}\n')
    sys.stdout.flush()
    time.sleep(1.2)
