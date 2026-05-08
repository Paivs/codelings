import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from runner import BASE
from runner.i18n import t

_PY = "python" if sys.platform == "win32" else "python3"

RUNNERS = {
    ".py":  {"cmd":     [_PY,        "{file}"]},
    ".js":  {"cmd":     ["node",     "{file}"]},
    ".ts":  {"cmd":     ["deno",     "run", "--allow-all", "{file}"]},
    ".go":  {"cmd":     ["go",       "run", "{file}"]},
    ".rb":  {"cmd":     ["ruby",     "{file}"]},
    ".lua": {"cmd":     ["lua",      "{file}"]},
    ".rs":  {"compile": ["rustc",    "{file}", "-o", "{bin}"],
             "run":     ["{bin}"]},
    ".c":   {"compile": ["gcc",      "{file}", "-o", "{bin}"],
             "run":     ["{bin}"]},
    ".java":{"compile": ["javac",    "-d", "{tmpdir}", "{file}"],
             "run":     ["java",     "-ea", "-cp", "{tmpdir}", "Exercicio"]},
}

DOC_PADRAO = {
    ".py":  "https://docs.python.org/3/",
    ".js":  "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
    ".ts":  "https://www.typescriptlang.org/docs/",
    ".go":  "https://go.dev/doc/",
    ".rs":  "https://doc.rust-lang.org/book/",
    ".rb":  "https://ruby-doc.org/",
    ".lua": "https://www.lua.org/manual/5.4/",
    ".c":   "https://en.cppreference.com/w/c",
    ".java":"https://dev.java/learn/",
}

LANG_LABEL = {
    ".py":  "Python",
    ".js":  "JavaScript",
    ".ts":  "TypeScript",
    ".go":  "Go",
    ".rb":  "Ruby",
    ".lua": "Lua",
    ".rs":  "Rust",
    ".c":   "C",
    ".java":"Java",
}

HINTS_FILE    = Path(__file__).parent / 'hints.json'
PROGRESS_FILE = BASE / '.progress.json'

_KEY = {'titulo': 'title', 'tipo': 'type', 'descricao': 'description',
        'title': 'title', 'type': 'type', 'description': 'description'}


def read_meta(path: Path) -> dict:
    m = {'title': path.stem, 'type': 'fix', 'description': '', 'id': '???'}
    comment_chars = ('#', '//', '--')
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                for cc in comment_chars:
                    if stripped.startswith(cc):
                        stripped = stripped[len(cc):].strip()
                        break
                else:
                    break
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


def discover() -> dict:
    root = BASE / 'exercises'
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


def load_hints() -> dict:
    try:
        return json.loads(HINTS_FILE.read_text(encoding='utf-8'))
    except Exception:
        return {}


def load_progress() -> dict:
    try:
        return json.loads(PROGRESS_FILE.read_text(encoding='utf-8'))
    except Exception:
        return {}


def save_progress(p: dict) -> None:
    PROGRESS_FILE.write_text(json.dumps(p, indent=2), encoding='utf-8')


def _run_cmd(cmd: list, cwd: Path):
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
            returncode = 1; stdout = ''; stderr = t('error.timeout')
        return _T()
    except FileNotFoundError:
        prog = cmd[0]
        class _M:
            returncode = 1; stdout = ''
            stderr = t('error.runtime_not_found', prog=prog)
        return _M()
    except Exception as exc:
        class _E:
            returncode = 1; stdout = ''; stderr = str(exc)
        return _E()


def run_ex(path: Path):
    ext = path.suffix.lower()
    runner = RUNNERS.get(ext)
    if not runner:
        class _U:
            returncode = 1; stdout = ''; stderr = t('error.unsupported_ext', ext=ext)
        return _U()

    if 'cmd' in runner:
        cmd = [c.replace('{file}', str(path)) for c in runner['cmd']]
        return _run_cmd(cmd, cwd=path.parent)

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
