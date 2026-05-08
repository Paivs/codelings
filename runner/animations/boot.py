import random
import sys
import time

from runner import G, Y, DIM, BOLD, RST
from runner.i18n import t

_LINES = [
    ('anim.boot.bios',       True,  0.05),
    ('anim.boot.copyright',  False, 0.04),
    ('',                     False, 0.10),
    ('anim.boot.cpu',        False, None),
    ('anim.boot.memory',     False, None),
    ('anim.boot.kernel',     False, None),
    ('anim.boot.mount',      False, None),
    ('anim.boot.hints',      False, None),
    ('anim.boot.flux',       False, None),
    ('',                     False, 0.08),
    ('anim.boot.ready',      True,  0.00),
]


def play() -> None:
    print()
    for key, bold, delay in _LINES:
        if not key:
            print()
            time.sleep(delay or 0.05)
            continue

        text = t(key)
        color = BOLD if bold else (Y if key == 'anim.boot.ready' else '')

        if delay is None:
            dots = '.' * random.randint(20, 35)
            sys.stdout.write(f'  {color}{text}{RST} {DIM}{dots}{RST}')
            sys.stdout.flush()
            time.sleep(random.uniform(0.12, 0.28))
            sys.stdout.write(f' {G}OK{RST}\n')
            sys.stdout.flush()
            time.sleep(random.uniform(0.04, 0.1))
        else:
            print(f'  {color}{text}{RST}')
            time.sleep(delay)

    time.sleep(0.6)
