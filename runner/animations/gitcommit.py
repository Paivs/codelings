import random
import string
import sys
import time

from runner import G, Y, DIM, BOLD, RST
from runner.i18n import t

_MSG_KEYS = [f'anim.git.msg.{i}' for i in range(9)]


def _typewrite(text: str, delay: float = 0.04) -> None:
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()


def _short_hash() -> str:
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))


def play() -> None:
    msg = t(random.choice(_MSG_KEYS))
    sha = _short_hash()

    print()
    sys.stdout.write(f'  {DIM}${RST} ')
    sys.stdout.flush()
    _typewrite(f'git commit -m "{msg}"')
    time.sleep(0.25)

    print(f'  {Y}[main {sha}]{RST} {msg}')
    time.sleep(0.08)
    print(f'  {DIM}{t("anim.git.stat")}{RST}')
    time.sleep(0.08)
    print(f'  {G}{BOLD}{t("anim.git.committed")}{RST}')
    sys.stdout.flush()
    time.sleep(1.0)
