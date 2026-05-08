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
from runner.sync import sync_from_remote, _load_config, _save_config, _parse_github_url
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
        for i, p in enumerate(parts, 1):
            tt  = sum(len(v) for v in cats[p].values())
            d   = sum(1 for topic_exs in cats[p].values() for e in topic_exs if prog.get(e['key']))
            col = G if d == tt else Y
            print(f"    {BOLD}{i}.{RST}  {label(p):<32} ({col}{d}/{tt}{RST})")
        if remote:
            try:
                owner, repo = _parse_github_url(remote)
                remote_label = f"{owner}/{repo}"
            except ValueError:
                remote_label = remote
            print(f"\n    {CY}S.  {t('menu.sync')}  {DIM}({remote_label}){RST}")
        print(f"\n    {DIM}0.  {t('menu.exit')}{RST}\n")
        c = input(f"  {CY}> {RST}").strip().lower()
        if c == '0':
            return
        if c == 's' and remote:
            sync_from_remote(cfg)
            cats  = discover()
            hints = load_hints()
            continue
        try:
            idx = int(c) - 1
            if 0 <= idx < len(parts):
                if menu_topics(cats, parts[idx], prog, hints) == 'quit':
                    return
        except ValueError:
            pass


def menu_topics(cats, part, prog, hints):
    while True:
        header(prog, cats, compact=True)
        print(f"  {BOLD}{label(part)} — {t('menu.topics')}{RST}\n")
        topics = list(cats[part].keys())
        for i, topic in enumerate(topics, 1):
            exs = cats[part][topic]
            d   = sum(1 for e in exs if prog.get(e['key']))
            n   = len(exs)
            col = G if d == n else Y
            print(f"    {BOLD}{i}.{RST}  {label(topic):<32} [{col}{d}/{n}{RST}]")
        print(f"\n    {DIM}0.  {t('menu.back')}{RST}\n")
        c = input(f"  {CY}> {RST}").strip()
        if c == '0':
            return None
        try:
            idx = int(c) - 1
            if 0 <= idx < len(topics):
                if menu_exercises(cats, part, topics[idx], prog, hints) == 'quit':
                    return 'quit'
        except ValueError:
            pass


def menu_exercises(cats, part, topic, prog, hints):
    while True:
        header(prog, cats, compact=True)
        print(f"  {BOLD}{label(topic)} — {t('menu.exercises')}{RST}\n")
        exs = cats[part][topic]
        for i, e in enumerate(exs, 1):
            m    = e['meta']
            lang = e.get('lang', '')
            tc   = Y if m['type'] == 'fix' else B
            tl   = 'FIX ' if m['type'] == 'fix' else 'TODO'
            st   = f"{G}[OK]{RST}" if prog.get(e['key']) else f"{DIM}[  ]{RST}"
            print(f"    {BOLD}{i}.{RST}  {st} {tc}[{tl}]{RST} {CY}[{lang}]{RST}  {DIM}#{m['id']}{RST}  {m['title']}")
        print(f"\n    {DIM}0.  {t('menu.back')}{RST}\n")
        c = input(f"  {CY}> {RST}").strip()
        if c == '0':
            return None
        try:
            idx = int(c) - 1
            if 0 <= idx < len(exs):
                watch(exs[idx], prog, hints)
        except ValueError:
            pass


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
