#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pythonlings - Aprenda Python corrigindo e completando exercicios."""

import os
import sys
import time
import subprocess
import json
import msvcrt
from pathlib import Path

BASE = Path(__file__).parent

# Habilita cores ANSI no Windows
import ctypes
try:
    ctypes.windll.kernel32.SetConsoleMode(
        ctypes.windll.kernel32.GetStdHandle(-11), 7)
except Exception:
    pass

R    = '\033[91m'
G    = '\033[92m'
Y    = '\033[93m'
B    = '\033[94m'
CY   = '\033[96m'
W    = '\033[97m'
BOLD = '\033[1m'
DIM  = '\033[2m'
RST  = '\033[0m'

PROGRESS_FILE = BASE / '.progress.json'
HINTS_FILE    = BASE / 'hints.json'
SEP = CY + BOLD + '─' * 62 + RST

BANNER = (
    f"\n{BOLD}{CY}"
    "  ╔══════════════════════════════════════════════════╗\n"
    "  ║                                                  ║\n"
    "  ║    PYTHONLINGS  -  Aprenda Python Fazendo!       ║\n"
    "  ║                                                  ║\n"
    "  ╚══════════════════════════════════════════════════╝\n"
    f"{RST}"
)


def clr():
    os.system('cls')


def load_progress():
    try:
        return json.loads(PROGRESS_FILE.read_text(encoding='utf-8'))
    except Exception:
        return {}


def save_progress(p):
    PROGRESS_FILE.write_text(json.dumps(p, indent=2), encoding='utf-8')


def load_hints():
    try:
        return json.loads(HINTS_FILE.read_text(encoding='utf-8'))
    except Exception:
        return {}


_KEY = {'titulo': 'title', 'tipo': 'type', 'descricao': 'description',
        'title': 'title', 'type': 'type', 'description': 'description'}


def read_meta(path):
    m = {'title': path.stem, 'type': 'fix', 'description': '', 'id': '???'}
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                s = line.strip()
                if not s.startswith('#'):
                    break
                if ':' not in s:
                    continue
                k, _, v = s[2:].partition(':')
                k = _KEY.get(k.strip().lower(), k.strip().lower())
                v = v.strip()
                if k in m:
                    m[k] = v.lower() if k == 'type' else v
    except Exception:
        pass
    return m


def discover():
    root = BASE / 'exercicios'
    cats = {}
    if not root.exists():
        return cats
    for part in sorted(root.iterdir()):
        if not part.is_dir():
            continue
        cats[part.name] = {}
        for topic in sorted(part.iterdir()):
            if not topic.is_dir():
                continue
            exs = [
                {
                    'path': f,
                    'key': str(f.relative_to(BASE)).replace('\\', '/'),
                    'meta': read_meta(f),
                }
                for f in sorted(topic.glob('*.py'))
            ]
            if exs:
                cats[part.name][topic.name] = exs
    return cats


def run_ex(path):
    env = {**os.environ, 'PYTHONIOENCODING': 'utf-8', 'PYTHONUTF8': '1'}
    try:
        return subprocess.run(
            [sys.executable, str(path)],
            capture_output=True,
            text=True,
            timeout=10,
            encoding='utf-8',
            errors='replace',
            cwd=str(path.parent),
            env=env,
        )
    except subprocess.TimeoutExpired:
        class _Timeout:
            returncode = 1
            stdout = ''
            stderr = 'Tempo limite excedido (10s). Verifique se ha loops infinitos.'
        return _Timeout()
    except Exception as exc:
        class _Err:
            returncode = 1
            stdout = ''
            stderr = str(exc)
        return _Err()


def flush_keys():
    """Descarta qualquer tecla pendente no buffer do terminal."""
    while msvcrt.kbhit():
        msvcrt.getch()


def show_result(ex, result, prog, hints, show_hint=False):
    clr()
    m = ex['meta']
    tc = Y if m['type'] == 'fix' else B
    tl = 'FIX' if m['type'] == 'fix' else 'TODO'
    ok = result.returncode == 0
    hint = hints.get(ex['key'], '')

    print(f"\n{SEP}")
    print(f"{BOLD}  #{m['id']}  {m['title']}{RST}")
    print(f"  Tipo: {tc}{BOLD}{tl}{RST}  |  {DIM}{ex['path'].name}{RST}")
    if m['description']:
        print(f"\n  {m['description']}")
    print(SEP + '\n')

    if ok:
        print(f"  {G}{BOLD}[OK] Exercicio concluido!{RST}\n")
        prog[ex['key']] = True
        save_progress(prog)
    else:
        print(f"  {R}{BOLD}[ERRO] Ha problemas no exercicio{RST}\n")

    if result.stdout:
        print(f"{W}--- saida ---{RST}")
        for line in result.stdout.splitlines():
            print(f"  {line}")
        print()

    if not ok and result.stderr:
        print(f"{R}--- erro ---{RST}")
        for line in result.stderr.splitlines():
            print(f"  {R}{line}{RST}")
        print()

    if show_hint and hint:
        print(f"  {Y}{BOLD}Dica:{RST} {Y}{hint}{RST}\n")

    print(f"\n{DIM}{'─' * 62}")
    print(f"  Arquivo : {ex['path']}")
    if not ok and hint and not show_hint:
        print(f"  Teclas  : [H] mostrar dica   |   Ctrl+C voltar ao menu")
    else:
        print(f"  Teclas  : Ctrl+C voltar ao menu")
    print(f"{'─' * 62}{RST}")


def watch(ex, prog, hints):
    path = ex['path']
    last_mtime = 0
    last_result = None
    show_hint = False

    clr()
    print(f"\n  {CY}Exercicio selecionado: {BOLD}{path.name}{RST}")
    print(f"  {DIM}Edite o arquivo e salve — o resultado aparece automaticamente.{RST}")
    print(f"  {DIM}Ctrl+C para voltar ao menu.{RST}\n")
    flush_keys()

    try:
        while True:
            # Detecta tecla pressionada sem bloquear
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8', errors='ignore').lower()
                if key == 'h' and last_result is not None and last_result.returncode != 0:
                    show_hint = True
                    show_result(ex, last_result, prog, hints, show_hint)

            try:
                mtime = path.stat().st_mtime
            except FileNotFoundError:
                time.sleep(0.5)
                continue

            if mtime != last_mtime:
                last_mtime = mtime
                show_hint = False
                last_result = run_ex(path)
                show_result(ex, last_result, prog, hints, show_hint)
                flush_keys()

            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n\n  {CY}Voltando ao menu...{RST}")
        time.sleep(0.3)


def label(name):
    return (name.split('_', 1)[1] if '_' in name else name).replace('_', ' ').title()


def header(prog, cats):
    clr()
    print(BANNER)
    total = sum(len(v) for p in cats.values() for v in p.values())
    done = sum(1 for v in prog.values() if v)
    n = int(40 * done / max(total, 1))
    bar = G + '#' * n + DIM + '-' * (40 - n) + RST
    print(f"  Progresso: [{bar}] {BOLD}{done}/{total}{RST}\n")


def menu_parts(cats, prog, hints):
    while True:
        header(prog, cats)
        parts = list(cats.keys())
        print(f"  {BOLD}Selecione uma parte:{RST}\n")
        for i, p in enumerate(parts, 1):
            t = sum(len(v) for v in cats[p].values())
            d = sum(1 for topic in cats[p].values() for e in topic if prog.get(e['key']))
            col = G if d == t else Y
            print(f"    {BOLD}{i}.{RST}  {label(p):<32} ({col}{d}/{t}{RST})")
        print(f"\n    {DIM}0.  Sair{RST}\n")
        c = input(f"  {CY}> {RST}").strip()
        if c == '0':
            return
        try:
            idx = int(c) - 1
            if 0 <= idx < len(parts):
                if menu_topics(cats, parts[idx], prog, hints) == 'quit':
                    return
        except ValueError:
            pass


def menu_topics(cats, part, prog, hints):
    while True:
        header(prog, cats)
        print(f"  {BOLD}{label(part)} — Topicos:{RST}\n")
        topics = list(cats[part].keys())
        for i, t in enumerate(topics, 1):
            exs = cats[part][t]
            d = sum(1 for e in exs if prog.get(e['key']))
            n = len(exs)
            col = G if d == n else Y
            print(f"    {BOLD}{i}.{RST}  {label(t):<32} [{col}{d}/{n}{RST}]")
        print(f"\n    {DIM}0.  Voltar{RST}\n")
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
        header(prog, cats)
        print(f"  {BOLD}{label(topic)} — Exercicios:{RST}\n")
        exs = cats[part][topic]
        for i, e in enumerate(exs, 1):
            m = e['meta']
            tc = Y if m['type'] == 'fix' else B
            tl = 'FIX ' if m['type'] == 'fix' else 'TODO'
            st = f"{G}[OK]{RST}" if prog.get(e['key']) else f"{DIM}[  ]{RST}"
            print(f"    {BOLD}{i}.{RST}  {st} {tc}[{tl}]{RST}  {DIM}#{m['id']}{RST}  {m['title']}")
        print(f"\n    {DIM}0.  Voltar{RST}\n")
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
    cats = discover()
    if not cats:
        print(f"{R}Nenhum exercicio encontrado em ./exercises/{RST}")
        print("Certifique-se de que a pasta 'exercises' existe com os exercicios.")
        sys.exit(1)
    prog  = load_progress()
    hints = load_hints()
    try:
        menu_parts(cats, prog, hints)
    except KeyboardInterrupt:
        pass
    clr()
    print(BANNER)
    print(f"  {G}{BOLD}Ate logo! Continue praticando Python!{RST}\n")


if __name__ == '__main__':
    main()
