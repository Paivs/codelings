import random
import sys
import time

from runner import G, Y, DIM, BOLD, RST
from runner.i18n import t

_STALLS = {42: 0.4, 69: 0.5, 90: 0.6, 99: 1.2}


def play() -> None:
    width = 38
    print()
    for i in range(width + 1):
        pct    = int(i / width * 100)
        filled = '█' * i
        empty  = f'{DIM}░{RST}' * (width - i)
        label  = f'{BOLD}{pct}%{RST}'
        sys.stdout.write(f'\r\033[K  [{G}{filled}{RST}{empty}] {label}')
        sys.stdout.flush()

        stall = _STALLS.get(pct)
        if stall:
            time.sleep(stall)
        elif pct == 100:
            time.sleep(0.4)
        else:
            time.sleep(random.uniform(0.025, 0.07))

    time.sleep(0.3)
    sys.stdout.write(f'\r\033[K  {G}{BOLD}{t("anim.loading.finale")}{RST}\n')
    sys.stdout.flush()
    time.sleep(1.0)
