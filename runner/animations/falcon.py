import os
import sys
import time

from runner import CY, BOLD, RST
from runner.i18n import t

_UP  = lambda n: f'\033[{n}A'
_CLR = '\r\033[K'

_FALCON = [
    r"        ,-.      ",
    r"  ______/ _`--.__",
    r" /  *  * (*)  *  " + "\\",
    r"(___*_____________)===",
    r"   `-.__________.'  ",
]
_H = len(_FALCON)
_W = max(len(l) for l in _FALCON)


def play() -> None:
    try:
        cols = os.get_terminal_size().columns
    except OSError:
        cols = 80

    max_pos = max(cols - _W - 20, 15)

    sys.stdout.write('\n' * (_H + 1))
    sys.stdout.flush()

    # Phase 1: cruising
    for pos in range(0, max_pos, 3):
        sys.stdout.write(_UP(_H + 1))
        for i, line in enumerate(_FALCON):
            sys.stdout.write(_CLR + ' ' * pos + line + '\n')
        sys.stdout.write(_CLR + '\n')
        sys.stdout.flush()
        time.sleep(0.04)

    # Phase 2: hyperspace stretch
    pos = max_pos
    for stretch in range(2, cols - pos - _W + 1, 5):
        sys.stdout.write(_UP(_H + 1))
        for i, line in enumerate(_FALCON):
            if i == _H // 2:
                tail = CY + '=' * stretch + RST
            else:
                tail = ' ' * stretch
            sys.stdout.write(_CLR + ' ' * pos + line + tail + '\n')
        sys.stdout.write(_CLR + '\n')
        sys.stdout.flush()
        time.sleep(0.025)

    sys.stdout.write(_UP(_H + 1))
    for _ in range(_H):
        sys.stdout.write(_CLR + '\n')
    sys.stdout.write(_CLR + f'  {CY}{BOLD}{t("anim.falcon.finale")}{RST}\n')
    sys.stdout.flush()
    time.sleep(1.2)
