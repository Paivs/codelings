import os
import random
import sys
import time

from runner.animations import (
    bigbang,
    boot,
    delorean,
    doom,
    falcon,
    gitcommit,
    loading,
    matrix,
    pacman,
    tetris,
)

_ANIMATIONS = [
    bigbang.play,
    boot.play,
    delorean.play,
    doom.play,
    falcon.play,
    gitcommit.play,
    loading.play,
    matrix.play,
    pacman.play,
    tetris.play,
]

_ALT_ON  = '\033[?1049h'
_ALT_OFF = '\033[?1049l'


def play_random(chance: float = 0.5) -> None:
    if not sys.stdout.isatty():
        return
    if random.random() > chance:
        return

    sys.stdout.write(_ALT_ON)
    sys.stdout.flush()
    os.system('cls' if sys.platform == 'win32' else 'clear')

    _orig_sleep = time.sleep
    time.sleep = lambda s: _orig_sleep(s * 1.25)
    try:
        random.choice(_ANIMATIONS)()
        time.sleep(1.5)
    finally:
        time.sleep = _orig_sleep
        sys.stdout.write(_ALT_OFF)
        sys.stdout.flush()
