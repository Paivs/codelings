import os
import sys
import time

from runner import Y, R, CY, BOLD, RST
from runner.i18n import t

_DOT   = '·'
_OPEN  = 'C'
_CLOSE = 'c'
_GHOST = ['&', '%']


def play() -> None:
    try:
        cols = os.get_terminal_size().columns
    except OSError:
        cols = 80

    width  = min(cols - 6, 55)
    dots   = list(_DOT * width)
    ghosts = [width + 2, width + 5]

    sys.stdout.write('\n' * 3)
    sys.stdout.flush()

    eaten = 0
    for pos in range(width + len(ghosts) + 3):
        sys.stdout.write(f'\033[3A')

        pac  = _OPEN if pos % 2 == 0 else _CLOSE

        # eat dot
        if pos < len(dots):
            dots[pos] = ' '
            eaten += 1

        dot_row   = '  ' + ''.join(dots)
        pac_row   = '  ' + ' ' * pos + Y + BOLD + pac + RST + (''.join(dots[pos + 1:]) if pos + 1 < len(dots) else '')
        ghost_row = '  '
        for g in ghosts:
            offset = g - pos
            if 0 < offset < width + 6:
                ghost_row += ' ' * (offset - len(ghost_row) + 2)
                ghost_row += R + _GHOST[ghosts.index(g) % 2] + RST

        sys.stdout.write(f'\r\033[K{ghost_row[:cols]}\n')
        sys.stdout.write(f'\r\033[K{pac_row[:cols]}\n')
        sys.stdout.write(f'\r\033[K  {CY}{t("anim.pacman.score", n=eaten * 10)}{RST}\n')
        sys.stdout.flush()
        time.sleep(0.045)

    sys.stdout.write(f'\033[3A\r\033[K\n\r\033[K  {Y}{BOLD}{t("anim.pacman.finale")}{RST}\n\r\033[K\n')
    sys.stdout.flush()
    time.sleep(1.0)
