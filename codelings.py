#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Codelings - Aprenda programação corrigindo e completando exercícios."""

import os
import sys
import time
import subprocess
import json
import tempfile
from pathlib import Path

BASE = Path(__file__).parent

# ── Runners por extensão ───────────────────────────────────────────────────────

RUNNERS = {
    ".py":  {"cmd":     ["python3",  "{file}"]},
    ".js":  {"cmd":     ["node",     "{file}"]},
    ".ts":  {"cmd":     ["deno",     "run", "--allow-all", "{file}"]},
    ".go":  {"cmd":     ["go",       "run", "{file}"]},
    ".rb":  {"cmd":     ["ruby",     "{file}"]},
    ".lua": {"cmd":     ["lua",      "{file}"]},
    ".rs":   {"compile": ["rustc",  "{file}", "-o", "{bin}"],
              "run":     ["{bin}"]},
    ".c":    {"compile": ["gcc",    "{file}", "-o", "{bin}"],
              "run":     ["{bin}"]},
    ".java": {"compile": ["javac",  "-d", "{tmpdir}", "{file}"],
              "run":     ["java",   "-ea", "-cp", "{tmpdir}", "Exercicio"]},
}

DOC_PADRAO = {
    ".py":  "https://docs.python.org/3/",
    ".js":  "https://developer.mozilla.org/pt-BR/docs/Web/JavaScript",
    ".ts":  "https://www.typescriptlang.org/docs/",
    ".go":  "https://go.dev/doc/",
    ".rs":  "https://doc.rust-lang.org/book/",
    ".rb":  "https://ruby-doc.org/",
    ".lua": "https://www.lua.org/manual/5.4/",
    ".c":    "https://en.cppreference.com/w/c",
    ".java": "https://dev.java/learn/",
}

LANG_LABEL = {
    ".py":  "Python",
    ".js":  "JavaScript",
    ".ts":  "TypeScript",
    ".go":  "Go",
    ".rb":  "Ruby",
    ".lua": "Lua",
    ".rs":  "Rust",
    ".c":    "C",
    ".java": "Java",
}

# ── Compatibilidade de terminal (Windows / Linux / macOS) ─────────────────────

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

# ── Cores ──────────────────────────────────────────────────────────────────────

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
    "  ║    CODELINGS  -  Aprenda Programando!            ║\n"
    "  ║                                                  ║\n"
    "  ╚══════════════════════════════════════════════════╝\n"
    f"{RST}"
)


def clr():
    os.system('cls' if sys.platform == 'win32' else 'clear')


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
    comment_chars = ('#', '//', '--')
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                s = line.strip()
                stripped = s
                for cc in comment_chars:
                    if stripped.startswith(cc):
                        stripped = stripped[len(cc):].strip()
                        break
                else:
                    break  # não é linha de comentário
                if ':' not in stripped:
                    continue
                k, _, v = stripped.partition(':')
                k = _KEY.get(k.strip().lower(), k.strip().lower())
                v = v.strip()
                if k in m:
                    m[k] = v.lower() if k == 'type' else v
    except Exception:
        pass
    return m


def discover():
    root = BASE / 'exercicios'
    exts = set(RUNNERS.keys())
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
                    'key':  str(f.relative_to(BASE)).replace('\\', '/'),
                    'meta': read_meta(f),
                    'lang': LANG_LABEL.get(f.suffix.lower(), f.suffix[1:].upper()),
                }
                for f in sorted(topic.iterdir())
                if f.is_file() and f.suffix.lower() in exts
            ]
            if exs:
                cats[part.name][topic.name] = exs
    return cats


def _run_cmd(cmd, cwd):
    env = {**os.environ, 'PYTHONIOENCODING': 'utf-8', 'PYTHONUTF8': '1'}
    try:
        return subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=15,
            encoding='utf-8',
            errors='replace',
            cwd=str(cwd),
            env=env,
        )
    except subprocess.TimeoutExpired:
        class _T:
            returncode = 1; stdout = ''; stderr = 'Tempo limite excedido (15s). Verifique se há loops infinitos.'
        return _T()
    except FileNotFoundError:
        prog = cmd[0]
        class _M:
            returncode = 1; stdout = ''
            stderr = f'Runtime não encontrado: "{prog}". Instale-o e tente novamente.'
        return _M()
    except Exception as exc:
        class _E:
            returncode = 1; stdout = ''; stderr = str(exc)
        return _E()


def run_ex(path):
    ext = path.suffix.lower()
    runner = RUNNERS.get(ext)
    if not runner:
        class _U:
            returncode = 1; stdout = ''; stderr = f'Extensão não suportada: {ext}'
        return _U()

    if 'cmd' in runner:
        cmd = [c.replace('{file}', str(path)) for c in runner['cmd']]
        return _run_cmd(cmd, cwd=path.parent)

    # Linguagem compilada: compile → execute
    bin_name = path.stem + ('.exe' if sys.platform == 'win32' else '')
    with tempfile.TemporaryDirectory() as tmpdir:
        bin_path = Path(tmpdir) / bin_name

        def expand(s):
            return (s.replace('{file}',   str(path))
                     .replace('{bin}',    str(bin_path))
                     .replace('{tmpdir}', tmpdir)
                     .replace('{class}',  path.stem))

        r = _run_cmd([expand(c) for c in runner['compile']], cwd=path.parent)
        if r.returncode != 0:
            return r
        return _run_cmd([expand(c) for c in runner['run']], cwd=path.parent)


def _parse_hint(raw) -> tuple[str, str]:
    """Suporta formato string legado e dict {dica, doc}."""
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
    print(f"  Tipo: {tc}{BOLD}{tl}{RST}  |  {CY}{lang}{RST}  |  {DIM}{ex['path'].name}{RST}")
    if m['description']:
        print(f"\n  {m['description']}")
    print(SEP + '\n')

    if ok:
        print(f"  {G}{BOLD}[OK] Exercício concluído!{RST}\n")
        prog[ex['key']] = True
        save_progress(prog)
    else:
        print(f"  {R}{BOLD}[ERRO] Há problemas no exercício{RST}\n")

    if result.stdout:
        print(f"{W}--- saída ---{RST}")
        for line in result.stdout.splitlines():
            print(f"  {line}")
        print()

    if not ok and result.stderr:
        print(f"{R}--- erro ---{RST}")
        for line in result.stderr.splitlines():
            print(f"  {R}{line}{RST}")
        print()

    if show_hint and tem_hint:
        if hint_text:
            print(f"  {Y}{BOLD}Dica:{RST} {Y}{hint_text}{RST}")
        if hint_doc:
            print(f"  {Y}{BOLD}Doc: {RST} {CY}{hint_doc}{RST}")
        print()

    print(f"\n{DIM}{'─' * 62}")
    print(f"  Arquivo : {ex['path']}")
    if not ok and tem_hint and not show_hint:
        print(f"  Teclas  : [H] mostrar dica   |   Ctrl+C voltar ao menu")
    else:
        print(f"  Teclas  : Ctrl+C voltar ao menu")
    print(f"{'─' * 62}{RST}")


def watch(ex, prog, hints):
    path = ex['path']
    last_mtime  = 0
    last_result = None
    show_hint   = False

    clr()
    print(f"\n  {CY}Exercício selecionado: {BOLD}{path.name}{RST}")
    print(f"  {DIM}Edite o arquivo e salve — o resultado aparece automaticamente.{RST}")
    print(f"  {DIM}Ctrl+C para voltar ao menu.{RST}\n")
    flush_keys()

    try:
        with _RawTerm():
            while True:
                if _kbhit():
                    key = _getch().lower()
                    if key == 'h' and last_result is not None and last_result.returncode != 0:
                        show_hint = True
                        show_result(ex, last_result, prog, hints, show_hint)

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
                    flush_keys()

                time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n\n  {CY}Voltando ao menu...{RST}")
        time.sleep(0.3)


def label(name):
    return (name.split('_', 1)[1] if '_' in name else name).replace('_', ' ').title()


def _medalha(pct: float) -> str:
    if pct >= 1.0: return '🥇'
    if pct >= 0.75: return '🥈'
    if pct >= 0.5: return '🥉'
    return '  '


def header(prog, cats):
    clr()
    print(BANNER)
    total  = sum(len(v) for p in cats.values() for v in p.values())
    done   = sum(1 for v in prog.values() if v)
    pct    = done / max(total, 1)
    score  = done * 10
    n      = int(40 * pct)
    bar    = G + '#' * n + DIM + '-' * (40 - n) + RST
    medalha = _medalha(pct)
    print(f"  Progresso: [{bar}] {BOLD}{done}/{total}{RST}  {medalha}  {CY}{BOLD}{score} pts{RST}\n")


def menu_parts(cats, prog, hints):
    while True:
        header(prog, cats)
        parts = list(cats.keys())
        print(f"  {BOLD}Selecione uma parte:{RST}\n")
        for i, p in enumerate(parts, 1):
            t   = sum(len(v) for v in cats[p].values())
            d   = sum(1 for topic in cats[p].values() for e in topic if prog.get(e['key']))
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
        print(f"  {BOLD}{label(part)} — Tópicos:{RST}\n")
        topics = list(cats[part].keys())
        for i, t in enumerate(topics, 1):
            exs = cats[part][t]
            d   = sum(1 for e in exs if prog.get(e['key']))
            n   = len(exs)
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
        print(f"  {BOLD}{label(topic)} — Exercícios:{RST}\n")
        exs = cats[part][topic]
        for i, e in enumerate(exs, 1):
            m    = e['meta']
            lang = e.get('lang', '')
            tc   = Y if m['type'] == 'fix' else B
            tl   = 'FIX ' if m['type'] == 'fix' else 'TODO'
            st   = f"{G}[OK]{RST}" if prog.get(e['key']) else f"{DIM}[  ]{RST}"
            print(f"    {BOLD}{i}.{RST}  {st} {tc}[{tl}]{RST} {CY}[{lang}]{RST}  {DIM}#{m['id']}{RST}  {m['title']}")
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
        print(f"{R}Nenhum exercício encontrado em ./exercicios/{RST}")
        print("Certifique-se de que a pasta 'exercicios' existe com os exercícios.")
        sys.exit(1)
    prog  = load_progress()
    hints = load_hints()
    try:
        menu_parts(cats, prog, hints)
    except KeyboardInterrupt:
        pass
    clr()
    print(BANNER)
    print(f"  {G}{BOLD}Até logo! Continue praticando!{RST}\n")


if __name__ == '__main__':
    main()
