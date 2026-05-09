#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Codelings — Learn programming by fixing and completing exercises."""

import argparse
import os
import subprocess
import sys
import time

from runner import R, G, Y, B, CY, W, BOLD, DIM, RST
from runner.i18n import t, get_banner, get_compact_banner, setup_i18n, _detect_lang
from runner.runners import run_ex, discover, load_hints, load_progress, save_progress, DOC_PADRAO
from runner.sync import sync_from_remote, _load_config, _save_config, _parse_github_url, DEFAULT_EXERCISES_REMOTE
from runner.animations import play_random

SEP = CY + BOLD + '─' * 62 + RST

# ── Terminal compatibility (Windows / Linux / macOS) ──────────────────────────

if sys.platform == 'win32':
    import msvcrt
    import ctypes
    try:
        ctypes.windll.kernel32.SetConsoleMode(
            ctypes.windll.kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass

    def _kbhit() -> bool:
        return msvcrt.kbhit()

    def _getch() -> str:
        return msvcrt.getch().decode('utf-8', errors='ignore')

    def flush_keys() -> None:
        while msvcrt.kbhit():
            msvcrt.getch()

    class _RawTerm:
        def __enter__(self): return self
        def __exit__(self, *_): pass

else:
    import tty
    import termios
    import select

    def _kbhit() -> bool:
        if not sys.stdin.isatty():
            return False
        return bool(select.select([sys.stdin], [], [], 0)[0])

    def _getch() -> str:
        return sys.stdin.read(1)

    def flush_keys() -> None:
        while _kbhit():
            _getch()

    class _RawTerm:
        def __enter__(self):
            if sys.stdin.isatty():
                self._fd = sys.stdin.fileno()
                self._old = termios.tcgetattr(self._fd)
                tty.setcbreak(self._fd)
            return self

        def __exit__(self, *_):
            if sys.stdin.isatty():
                termios.tcsetattr(self._fd, termios.TCSADRAIN, self._old)


def _read_menu_key() -> str:
    """Blocking read for menus — returns 'UP', 'DOWN', or a character."""
    if sys.platform == 'win32':
        ch = msvcrt.getch()
        if ch in (b'\x00', b'\xe0'):
            ch2 = msvcrt.getch()
            if ch2 == b'H': return 'UP'
            if ch2 == b'P': return 'DOWN'
            return ''
        if ch == b'\x03': raise KeyboardInterrupt
        try:
            return ch.decode('utf-8')
        except Exception:
            return ''
    else:
        fd  = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = os.read(fd, 1)
            if ch == b'\x03': raise KeyboardInterrupt
            if ch == b'\x1b':
                if select.select([fd], [], [], 0.1)[0]:
                    ch2 = os.read(fd, 1)
                    if ch2 == b'[' and select.select([fd], [], [], 0.1)[0]:
                        ch3 = os.read(fd, 1)
                        if ch3 == b'A': return 'UP'
                        if ch3 == b'B': return 'DOWN'
                return 'ESC'
            return ch.decode('utf-8', errors='ignore')
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _menu_select(items: list, default: int = 0, key_map: dict | None = None) -> int:
    """Arrow-key selector. Returns index of chosen item.

    key_map: extra {char: index} shortcuts (e.g. {'s': 3} for Sync).
    Pressing '0' always maps to the last item (back/quit).
    Pressing '1'..'9' jumps to that 1-based index if valid.
    """
    n      = len(items)
    cursor = default % n
    first  = True

    while True:
        if not first:
            sys.stdout.write(f'\033[{n}A')
        first = False

        for i, item in enumerate(items):
            sys.stdout.write('\r\033[K')
            if i == cursor:
                sys.stdout.write(f'  {CY}▸{RST} {item}\n')
            else:
                sys.stdout.write(f'    {item}\n')
        sys.stdout.flush()

        key = _read_menu_key()
        if key == 'UP':
            cursor = (cursor - 1) % n
        elif key == 'DOWN':
            cursor = (cursor + 1) % n
        elif key in ('\r', '\n'):
            return cursor
        elif key == '0':
            return n - 1
        elif key.isdigit():
            idx = int(key) - 1
            if 0 <= idx < n:
                return idx
        elif key_map and key.lower() in key_map:
            return key_map[key.lower()]


_TERMINAL_EDITORS = {'vim', 'vi', 'nvim', 'nano', 'emacs', 'pico', 'micro', 'hx', 'helix'}


def _open_in_editor(editor: str, path) -> None:
    base = os.path.basename(editor).lower()
    shell = sys.platform == 'win32'
    if base in _TERMINAL_EDITORS:
        subprocess.call([editor, str(path)])
    elif base in {'code', 'code-insiders'}:
        subprocess.Popen([editor, '--reuse-window', str(path)],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         shell=shell)
    else:
        subprocess.Popen([editor, str(path)],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         shell=shell)


def clr():
    os.system('cls' if sys.platform == 'win32' else 'clear')


def label(name: str) -> str:
    return (name.split('_', 1)[1] if '_' in name else name).replace('_', ' ').title()


def _medalha(pct: float) -> str:
    if pct >= 1.0:  return '🥇'
    if pct >= 0.75: return '🥈'
    if pct >= 0.5:  return '🥉'
    return '  '


def _parse_hint(raw) -> tuple[str, str]:
    if isinstance(raw, dict):
        return raw.get('dica', ''), raw.get('doc', '')
    return str(raw) if raw else '', ''


def show_result(ex, result, prog, hints, show_hint=False):
    clr()
    m    = ex['meta']
    lang = ex.get('lang', '')
    tc   = Y if m['type'] == 'fix' else B
    tl   = 'FIX' if m['type'] == 'fix' else 'TODO'
    ok   = result.returncode == 0

    hint_text, hint_doc = _parse_hint(hints.get(ex['key'], ''))
    if not hint_doc:
        hint_doc = DOC_PADRAO.get(ex['path'].suffix.lower(), '')
    tem_hint = bool(hint_text or hint_doc)

    print(f"\n{SEP}")
    print(f"{BOLD}  #{m['id']}  {m['title']}{RST}")
    print(f"  {t('result.type_label')}: {tc}{BOLD}{tl}{RST}  |  {CY}{lang}{RST}  |  {DIM}{ex['path'].name}{RST}")
    if m['description']:
        print(f"\n  {m['description']}")
    print(SEP + '\n')

    if ok:
        print(f"  {G}{BOLD}{t('result.ok')}{RST}\n")
        prog[ex['key']] = True
        save_progress(prog)
    else:
        print(f"  {R}{BOLD}{t('result.error')}{RST}\n")

    if result.stdout:
        print(f"{W}{t('result.stdout')}{RST}")
        for line in result.stdout.splitlines():
            print(f"  {line}")
        print()

    if not ok and result.stderr:
        print(f"{R}{t('result.stderr')}{RST}")
        for line in result.stderr.splitlines():
            print(f"  {R}{line}{RST}")
        print()

    if show_hint and tem_hint:
        if hint_text:
            print(f"  {Y}{BOLD}{t('result.hint_label')}{RST} {Y}{hint_text}{RST}")
        if hint_doc:
            print(f"  {Y}{BOLD}{t('result.doc_label')}{RST} {CY}{hint_doc}{RST}")
        print()

    print(f"\n{DIM}{'─' * 62}")
    print(f"  {t('result.file')} : {ex['path']}")
    if not ok and tem_hint and not show_hint:
        print(f"  {t('result.keys_hint')}")
    else:
        print(f"  {t('result.keys_no_hint')}")
    print(f"{'─' * 62}{RST}")


def watch(ex, prog, hints):
    path = ex['path']
    last_mtime  = 0
    last_result = None
    show_hint   = False

    clr()
    print(f"\n  {CY}{t('watch.selected', name=path.name)}{RST}")
    print(f"  {DIM}{t('watch.edit_hint')}{RST}")
    print(f"  {DIM}{t('watch.ctrl_c')}{RST}\n")
    flush_keys()

    try:
        with _RawTerm():
            while True:
                if _kbhit():
                    key = _getch().lower()
                    if key == 'h' and last_result is not None and last_result.returncode != 0:
                        show_hint = True
                        show_result(ex, last_result, prog, hints, show_hint)
                    elif key == 'e':
                        _open_in_editor(_load_config().get('editor', 'code'), path)

                try:
                    mtime = path.stat().st_mtime
                except FileNotFoundError:
                    time.sleep(0.5)
                    continue

                if mtime != last_mtime:
                    last_mtime  = mtime
                    show_hint   = False
                    last_result = run_ex(path)
                    show_result(ex, last_result, prog, hints, show_hint)
                    if last_result.returncode == 0:
                        play_random()
                    flush_keys()

                time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n\n  {CY}{t('watch.returning')}{RST}")
        time.sleep(0.3)


def header(prog, cats, compact=False):
    clr()
    print(get_compact_banner() if compact else get_banner())
    total      = sum(len(v) for p in cats.values() for v in p.values())
    done       = sum(1 for v in prog.values() if v)
    pct        = done / max(total, 1)
    prob_total = sum(len(v) for v in cats.get('problemas', {}).values())
    prob_done  = sum(1 for topic_exs in cats.get('problemas', {}).values()
                     for e in topic_exs if prog.get(e['key']))
    prob_pct   = prob_done / max(prob_total, 1)
    score      = prob_done * 10
    n          = int(40 * pct)
    bar        = G + '#' * n + DIM + '-' * (40 - n) + RST
    medalha    = _medalha(prob_pct)
    print(f"  {t('progress.label')}: [{bar}] {BOLD}{done}/{total}{RST}  {medalha}  {CY}{BOLD}{score} pts{RST}\n")


def menu_parts(cats, prog, hints):
    while True:
        header(prog, cats)
        cfg    = _load_config()
        remote = cfg.get('remote_url', '')
        parts  = list(cats.keys())
        print(f"  {BOLD}{t('menu.select_part')}{RST}\n")

        items  = []
        values = []
        for i, p in enumerate(parts, 1):
            tt  = sum(len(v) for v in cats[p].values())
            d   = sum(1 for topic_exs in cats[p].values() for e in topic_exs if prog.get(e['key']))
            col = G if d == tt else Y
            items.append(f"{BOLD}{i}.{RST}  {label(p):<32} ({col}{d}/{tt}{RST})")
            values.append(('part', p))

        key_map = {}
        if remote:
            try:
                owner, repo = _parse_github_url(remote)
                remote_label = f"{owner}/{repo}"
            except ValueError:
                remote_label = remote
            items.append(f"{CY}S.  {t('menu.sync')}  {DIM}({remote_label}){RST}")
            values.append(('sync', None))
            key_map['s'] = len(items) - 1

        items.append(f"{DIM}0.  {t('menu.exit')}{RST}")
        values.append(('quit', None))

        idx            = _menu_select(items, key_map=key_map)
        action, val    = values[idx]

        if action == 'quit':
            return
        if action == 'sync':
            sync_from_remote(cfg)
            cats  = discover()
            hints = load_hints()
            continue
        if menu_topics(cats, val, prog, hints) == 'quit':
            return


def menu_topics(cats, part, prog, hints):
    while True:
        header(prog, cats, compact=True)
        topics = list(cats[part].keys())
        print(f"  {BOLD}{label(part)} — {t('menu.topics')}{RST}\n")

        items = []
        for i, topic in enumerate(topics, 1):
            exs = cats[part][topic]
            d   = sum(1 for e in exs if prog.get(e['key']))
            n   = len(exs)
            col = G if d == n else Y
            items.append(f"{BOLD}{i}.{RST}  {label(topic):<32} [{col}{d}/{n}{RST}]")
        items.append(f"{DIM}0.  {t('menu.back')}{RST}")

        idx = _menu_select(items)
        if idx == len(items) - 1:
            return None
        if menu_exercises(cats, part, topics[idx], prog, hints) == 'quit':
            return 'quit'


def menu_exercises(cats, part, topic, prog, hints):
    while True:
        header(prog, cats, compact=True)
        exs = cats[part][topic]
        print(f"  {BOLD}{label(topic)} — {t('menu.exercises')}{RST}\n")

        items = []
        for i, e in enumerate(exs, 1):
            m    = e['meta']
            lang = e.get('lang', '')
            tc   = Y if m['type'] == 'fix' else B
            tl   = 'FIX ' if m['type'] == 'fix' else 'TODO'
            st   = f"{G}[OK]{RST}" if prog.get(e['key']) else f"{DIM}[  ]{RST}"
            items.append(f"{BOLD}{i}.{RST}  {st} {tc}[{tl}]{RST} {CY}[{lang}]{RST}  {DIM}#{m['id']}{RST}  {m['title']}")
        items.append(f"{DIM}0.  {t('menu.back')}{RST}")

        idx = _menu_select(items)
        if idx == len(items) - 1:
            return None
        watch(exs[idx], prog, hints)


def main():
    parser = argparse.ArgumentParser(prog='codelings', add_help=False)
    parser.add_argument('--remote', metavar='URL',    help='Configure remote exercises repository')
    parser.add_argument('--branch', metavar='BRANCH', default=None)
    parser.add_argument('--sync',   action='store_true', help='Sync exercises from remote repository')
    parser.add_argument('--lang',   metavar='LANG',   default=None,
                        help='Set interface language (en, pt_BR, es, fr)')
    parser.add_argument('--editor', metavar='EDITOR', default=None,
                        help='Set default editor (code, vim, nano, ...)')
    args, _ = parser.parse_known_args()

    cfg = _load_config()

    if args.lang:
        cfg['lang'] = args.lang
        _save_config(cfg)

    if args.editor:
        cfg['editor'] = args.editor
        _save_config(cfg)

    setup_i18n(_detect_lang(cfg))

    if args.remote:
        cfg['remote_url'] = args.remote
        if args.branch:
            cfg['branch'] = args.branch
        _save_config(cfg)
        print(f"\n  {G}{t('remote.configured', url=args.remote)}{RST}")
        sync_from_remote(cfg)

    elif args.sync:
        ok = sync_from_remote(cfg)
        if not ok:
            sys.exit(1)

    cats = discover()
    if not cats:
        clr()
        print(get_banner())
        print(f"  {CY}{t('sync.first_run', remote=DEFAULT_EXERCISES_REMOTE)}{RST}\n")
        sync_from_remote(cfg)
        cats = discover()
    if not cats:
        print(f"{R}{t('error.no_exercises')}{RST}")
        print(t('error.configure_remote'))
        sys.exit(1)
    prog  = load_progress()
    hints = load_hints()
    try:
        menu_parts(cats, prog, hints)
    except KeyboardInterrupt:
        pass
    clr()
    print(get_banner())
    print(f"  {G}{BOLD}{t('goodbye')}{RST}\n")


if __name__ == '__main__':
    main()
