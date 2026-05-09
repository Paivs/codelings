#!/usr/bin/env python3
"""CLI interativo para criar novos exercícios no codelings."""

import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
from pathlib import Path

BASE       = Path(__file__).parent.parent
EXERCICIOS = BASE / "exercises"
HINTS_FILE = BASE / "runner" / "hints.json"

# ── Cores ─────────────────────────────────────────────────────────────────────

RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[36m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
RED    = "\033[31m"
DIM    = "\033[2m"

_LARGURA = 60


def c(color: str, text: str) -> str:
    return f"{color}{text}{RESET}"


def ok(text: str) -> None:
    print(c(GREEN, f"  ✓ {text}"))


def warn(text: str) -> None:
    print(c(YELLOW, f"  ! {text}"))


def erro(text: str) -> None:
    print(c(RED, f"  ✗ {text}"), file=sys.stderr)


# ── Terminal ──────────────────────────────────────────────────────────────────

def clr() -> None:
    os.system("cls" if sys.platform == "win32" else "clear")


def _getch() -> str:
    """Lê um caractere ou tecla especial. Retorna 'UP', 'DOWN' ou o char."""
    if sys.platform == "win32":
        import msvcrt
        ch = msvcrt.getch()
        if ch in (b"\x00", b"\xe0"):
            ch2 = msvcrt.getch()
            if ch2 == b"H": return "UP"
            if ch2 == b"P": return "DOWN"
            return ""
        if ch == b"\x03": raise KeyboardInterrupt
        try:
            return ch.decode("utf-8")
        except Exception:
            return ""
    else:
        import tty, termios, select as _sel
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = os.read(fd, 1)
            if ch == b"\x03":
                raise KeyboardInterrupt
            if ch == b"\x1b":
                if _sel.select([fd], [], [], 0.1)[0]:
                    ch2 = os.read(fd, 1)
                    if ch2 == b"[" and _sel.select([fd], [], [], 0.1)[0]:
                        ch3 = os.read(fd, 1)
                        if ch3 == b"A": return "UP"
                        if ch3 == b"B": return "DOWN"
                return "ESC"
            return ch.decode("utf-8", errors="ignore")
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


# ── Layout ────────────────────────────────────────────────────────────────────

def _tela(num: int, titulo: str, resumo: dict) -> None:
    clr()
    print()
    print(c(CYAN, "═" * _LARGURA))
    print(c(CYAN + BOLD, "  novo_exercicio — codelings"))
    print(c(CYAN, "═" * _LARGURA))
    if resumo:
        print()
        for k, v in resumo.items():
            label = c(DIM, f"{k}:")
            valor = c(CYAN, v)
            print(f"  {label:<24} {valor}")
        print()
        print(c(DIM, "─" * _LARGURA))
    print()
    print(c(BOLD, f"  [{num}] {titulo}"))
    print()


# ── Inputs ────────────────────────────────────────────────────────────────────

def escolher(opcoes: list[str], padrao: int = 0) -> str:
    """Seletor com navegação por setas ↑↓ ou número + Enter."""
    n      = len(opcoes)
    cursor = padrao % n
    first  = True

    while True:
        if not first:
            sys.stdout.write(f"\033[{n}A")
        first = False

        for i, op in enumerate(opcoes):
            sys.stdout.write("\r\033[K")
            num = c(DIM, f"{i + 1}.")
            if i == cursor:
                print(f"  {c(CYAN, '▸')} {num} {c(BOLD, op)}")
            else:
                print(f"     {num} {c(DIM, op)}")
        sys.stdout.flush()

        key = _getch()
        if key == "UP":
            cursor = (cursor - 1) % n
        elif key == "DOWN":
            cursor = (cursor + 1) % n
        elif key in ("\r", "\n", " "):
            return opcoes[cursor]
        elif key.isdigit():
            idx = int(key) - 1
            if 0 <= idx < n:
                return opcoes[idx]


def perguntar(prompt: str, padrao: str = "") -> str:
    sufixo = f" [{c(DIM, padrao)}]" if padrao else ""
    while True:
        val = input(f"  {c(BOLD, prompt)}{sufixo}: ").strip()
        if val:
            return val
        if padrao is not None and padrao != "":
            return padrao
        warn("Campo obrigatório.")


# ── Linguagens suportadas ─────────────────────────────────────────────────────

DOC_PADRAO: dict[str, str] = {
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

LINGUAGENS: dict[str, dict] = {
    "Python":     {"ext": ".py",   "comment": "#",  "compiled": False},
    "JavaScript": {"ext": ".js",   "comment": "//", "compiled": False},
    "TypeScript": {"ext": ".ts",   "comment": "//", "compiled": False},
    "Go":         {"ext": ".go",   "comment": "//", "compiled": False},
    "Rust":       {"ext": ".rs",   "comment": "//", "compiled": True},
    "Ruby":       {"ext": ".rb",   "comment": "#",  "compiled": False},
    "Lua":        {"ext": ".lua",  "comment": "--", "compiled": False},
    "C":          {"ext": ".c",    "comment": "//", "compiled": True},
    "Java":       {"ext": ".java", "comment": "//", "compiled": True},
}

_CORPO: dict[str, dict[str, str]] = {
    ".py": {
        "fix":  "def minha_funcao(x):\n    return x + 1   # <- revise esta linha\n",
        "todo": "def minha_funcao(x):\n    # TAREFA: implemente aqui.\n    pass\n",
    },
    ".js": {
        "fix":  "function minhaFuncao(x) {\n    return x + 1;  // <- revise esta linha\n}\n",
        "todo": "function minhaFuncao(x) {\n    // TAREFA: implemente aqui.\n}\n",
    },
    ".ts": {
        "fix":  "function minhaFuncao(x: number): number {\n    return x + 1;  // <- revise esta linha\n}\n",
        "todo": "function minhaFuncao(x: number): number {\n    // TAREFA: implemente aqui.\n    return 0;\n}\n",
    },
    ".go": {
        "fix":  'package main\n\nimport "fmt"\n\nfunc minhaFuncao(x int) int {\n    return x + 1  // <- revise esta linha\n}\n',
        "todo": 'package main\n\nimport "fmt"\n\nfunc minhaFuncao(x int) int {\n    // TAREFA: implemente aqui.\n    return 0\n}\n',
    },
    ".rs": {
        "fix":  "fn minha_funcao(x: i32) -> i32 {\n    x + 1  // <- revise esta linha\n}\n",
        "todo": "fn minha_funcao(x: i32) -> i32 {\n    // TAREFA: implemente aqui.\n    0\n}\n",
    },
    ".rb": {
        "fix":  "def minha_funcao(x)\n  x + 1  # <- revise esta linha\nend\n",
        "todo": "def minha_funcao(x)\n  # TAREFA: implemente aqui.\nend\n",
    },
    ".lua": {
        "fix":  "local function minhaFuncao(x)\n    return x + 1  -- <- revise esta linha\nend\n",
        "todo": "local function minhaFuncao(x)\n    -- TAREFA: implemente aqui.\nend\n",
    },
    ".c": {
        "fix":  '#include <stdio.h>\n#include <assert.h>\n\nint minhaFuncao(int x) {\n    return x + 1;  // <- revise esta linha\n}\n',
        "todo": '#include <stdio.h>\n#include <assert.h>\n\nint minhaFuncao(int x) {\n    // TAREFA: implemente aqui.\n    return 0;\n}\n',
    },
    ".java": {
        "fix":  'class Exercicio {\n\n    static int minhaFuncao(int x) {\n        return x + 1;  // <- revise esta linha\n    }\n',
        "todo": 'class Exercicio {\n\n    static int minhaFuncao(int x) {\n        // TAREFA: implemente aqui.\n        return 0;\n    }\n',
    },
}

_TESTES: dict[str, str] = {
    ".py":  'assert minhaFuncao(1) == 2, "caso 1 incorreto"\nprint("Exercicio concluido!")\n',
    ".js":  'console.assert(minhaFuncao(1) === 2, "caso 1 incorreto");\nconsole.log("Exercicio concluido!");\n',
    ".ts":  'console.assert(minhaFuncao(1) === 2, "caso 1 incorreto");\nconsole.log("Exercicio concluido!");\n',
    ".go":  'func main() {\n    if minhaFuncao(1) != 2 { panic("caso 1 incorreto") }\n    fmt.Println("Exercicio concluido!")\n}\n',
    ".rs":  'fn main() {\n    assert_eq!(minha_funcao(1), 2, "caso 1 incorreto");\n    println!("Exercicio concluido!");\n}\n',
    ".rb":  'raise "caso 1 incorreto" unless minhaFuncao(1) == 2\nputs "Exercicio concluido!"\n',
    ".lua": 'assert(minhaFuncao(1) == 2, "caso 1 incorreto")\nprint("Exercicio concluido!")\n',
    ".c":    'int main() {\n    assert(minhaFuncao(1) == 2);\n    printf("Exercicio concluido!\\n");\n    return 0;\n}\n',
    ".java": '    public static void main(String[] args) {\n        assert minhaFuncao(1) == 2 : "caso 1 incorreto";\n        System.out.println("Exercicio concluido!");\n    }\n}\n',
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def proximo_id() -> int:
    ids = set()
    comment_prefixes = ("#", "//", "--")
    for f in EXERCICIOS.rglob("*"):
        if not f.is_file():
            continue
        try:
            for linha in f.read_text(encoding="utf-8").splitlines()[:8]:
                s = linha.strip()
                for cp in comment_prefixes:
                    if s.startswith(cp):
                        s = s[len(cp):].strip()
                        break
                m = re.match(r"ID:\s*(\d+)", s, re.IGNORECASE)
                if m:
                    ids.add(int(m.group(1)))
                    break
        except Exception:
            pass
    return max(ids, default=0) + 1


def listar_topicos(categoria: str) -> list[Path]:
    base_cat = EXERCICIOS / categoria
    if not base_cat.exists():
        return []
    return sorted(d for d in base_cat.iterdir() if d.is_dir())


def abrir_editor(conteudo: str) -> str:
    editor = os.environ.get("EDITOR", os.environ.get("VISUAL", "nano"))
    with tempfile.NamedTemporaryFile(
        suffix=".txt", mode="w", encoding="utf-8", delete=False
    ) as f:
        f.write(conteudo)
        tmp = f.name
    try:
        subprocess.run([editor, tmp], check=True)
        return Path(tmp).read_text(encoding="utf-8")
    finally:
        os.unlink(tmp)


def gerar_template(titulo: str, tipo: str, id_num: int, ext: str, comment: str) -> str:
    sep = f"{comment} {'=' * (63 - len(comment))}"
    instrucao = (
        f"{comment} Descreva o bug existente. Seja específico sobre qual linha\n"
        f"{comment} está errada e o que precisa ser corrigido.\n"
        f"{comment} Use  <- revise esta linha  para marcar a linha bugada."
        if tipo == "fix" else
        f"{comment} Descreva o que o aluno precisa implementar.\n"
        f"{comment} Inclua exemplos de entrada/saída e regras de negócio."
    )
    corpo  = _CORPO.get(ext, {}).get(tipo, "// TODO: código aqui\n")
    testes = _TESTES.get(ext, "// TODO: testes aqui\n")
    return "\n".join([
        f"{comment} TITULO: {titulo}",
        f"{comment} TIPO: {tipo}",
        f"{comment} ID: {id_num:03d}",
        "", sep, f"{comment} ENUNCIADO", sep,
        instrucao, sep, "",
        corpo,
        sep, f"{comment} TESTES (nao modifique abaixo)", sep,
        testes,
    ])


# ── Config ────────────────────────────────────────────────────────────────────

def _load_config() -> dict:
    cfg_file = BASE / "config.json"
    try:
        return json.loads(cfg_file.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_config(cfg: dict) -> None:
    (BASE / "config.json").write_text(
        json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


# ── Publicação via API ────────────────────────────────────────────────────────

def _publicar(destino: Path, conteudo: str, tem_hint: bool) -> None:
    import urllib.error as _ue

    cfg        = _load_config()
    remote_url = cfg.get("remote_url", "https://github.com/Paivs/codelings-exercises-ptbr")

    try:
        _root = str(Path(__file__).parent.parent)
        if _root not in sys.path:
            sys.path.insert(0, _root)
        from runner.providers import detect_provider
        provider = detect_provider(remote_url, cfg.get("branch", "main"))
    except Exception as e:
        warn(f"Erro ao inicializar provider: {e}")
        return

    if type(provider).__name__ != "GithubProvider":
        warn("Publicação via API disponível apenas para repositórios GitHub.")
        return

    token = cfg.get("github_token", "")
    if not token:
        print()
        print(c(CYAN, "  Token GitHub não configurado."))
        print(c(DIM,  "  Gere em: https://github.com/settings/tokens"))
        print(c(DIM,  "  Permissão necessária: Contents (write)"))
        print()
        acao = escolher(["Inserir token agora", "Cancelar publicação"])
        if acao.startswith("Cancelar"):
            warn("Publicação cancelada.")
            return
        token = perguntar("Token").strip()
        if not token:
            warn("Token vazio. Publicação cancelada.")
            return
        salvar = escolher(["Sim, salvar em config.json", "Não, usar só agora"])
        if salvar.startswith("Sim"):
            cfg["github_token"] = token
            _save_config(cfg)
            ok("Token salvo.")

    rel = str(destino.relative_to(BASE)).replace("\\", "/")
    print(c(DIM, f"\n  Publicando {rel}..."))
    try:
        provider.publish_file(rel, destino.read_bytes(), f"feat: {rel}", token)
        ok(f"Exercício publicado em {provider.label()}")
    except _ue.HTTPError as e:
        if e.code == 401:
            warn("Token inválido ou sem permissão (401). Verifique o token.")
        elif e.code == 403:
            warn("Acesso negado (403). O token não tem permissão de escrita.")
        else:
            warn(f"Erro HTTP {e.code} ao publicar exercício.")
        return
    except _ue.URLError as e:
        warn(f"Sem conexão com o GitHub: {e.reason}")
        return
    except Exception as e:
        warn(f"Erro inesperado ao publicar: {e}")
        return

    if tem_hint and HINTS_FILE.exists():
        print(c(DIM, "  Publicando hints.json..."))
        try:
            provider.publish_file("hints.json", HINTS_FILE.read_bytes(), "chore: atualiza hints.json", token)
            ok("hints.json publicado.")
        except Exception as e:
            warn(f"Erro ao publicar hints.json: {e}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    resumo: dict[str, str] = {}

    # 1. Linguagem
    _tela(1, "Linguagem", resumo)
    nomes_lang = list(LINGUAGENS.keys())
    nome_lang  = escolher(nomes_lang)
    lang_cfg   = LINGUAGENS[nome_lang]
    ext        = lang_cfg["ext"]
    comment    = lang_cfg["comment"]
    resumo["Linguagem"] = nome_lang

    # 2. Categoria
    _tela(2, "Categoria", resumo)
    categoria = escolher(["conceitual", "problemas"])
    resumo["Categoria"] = categoria

    # 3. Tipo
    if categoria == "problemas":
        tipo = "todo"
        resumo["Tipo"] = "todo"
    else:
        _tela(3, "Tipo", resumo)
        tipos     = ["fix  — código com bug para corrigir", "todo  — função para implementar"]
        escolhido = escolher(tipos)
        tipo      = escolhido.split()[0]
        resumo["Tipo"] = tipo

    # 4. Tópico
    _tela(4, "Tópico", resumo)
    topicos_existentes = listar_topicos(categoria)
    nomes_topicos      = [d.name for d in topicos_existentes]
    opcoes_topico      = nomes_topicos + ["[+ novo tópico]"]
    escolhido          = escolher(opcoes_topico)

    if escolhido == "[+ novo tópico]":
        _tela(4, "Novo tópico", resumo)
        slug_topico = perguntar("Slug do novo tópico (ex: recursao, classes)")
        prox_num    = len(topicos_existentes) + 1
        nome_dir    = f"{prox_num:02d}_{slug_topico}"
    else:
        nome_dir = escolhido
        if categoria == "problemas":
            existentes = [f for f in (EXERCICIOS / categoria / nome_dir).glob("*") if f.is_file()]
            if existentes:
                warn(f"Este tópico já tem {len(existentes)} exercício(s). Problemas têm 1 por tópico.")
                if perguntar("Continuar mesmo assim? (s/n)", "n").lower() != "s":
                    sys.exit(1)
    resumo["Tópico"] = nome_dir

    dir_topico = EXERCICIOS / categoria / nome_dir

    # 5. ID
    _tela(5, "ID do exercício", resumo)
    id_num = int(perguntar("ID", str(proximo_id())))
    resumo["ID"] = str(id_num)

    # 6. Título
    _tela(6, "Título", resumo)
    titulo = perguntar("Título (ex: Palindromo - Bug na Inversao)")
    resumo["Título"] = titulo

    # 7. Nome do arquivo
    _tela(7, "Nome do arquivo", resumo)
    slug_padrao  = nome_dir.split("_", 1)[-1].replace("-", "_")
    slug_arquivo = perguntar("Slug sem extensão", slug_padrao)
    nome_arquivo = f"{slug_arquivo}_{tipo}{ext}"
    destino      = dir_topico / nome_arquivo
    resumo["Arquivo"] = nome_arquivo

    if destino.exists():
        warn(f"Arquivo já existe: {destino.relative_to(BASE)}")
        if perguntar("Sobrescrever? (s/n)", "n").lower() != "s":
            sys.exit(1)

    # 8. Conteúdo
    _tela(8, "Conteúdo do exercício", resumo)
    print(f"  Abrindo editor ({os.environ.get('EDITOR', 'nano')})…")
    print(c(DIM, "  Preencha ENUNCIADO e TESTES, salve e feche.\n"))
    conteudo = abrir_editor(gerar_template(titulo, tipo, id_num, ext, comment))

    # 9. Dica e documentação
    _tela(9, "Dica e documentação", resumo)
    hint_text  = perguntar("Dica curta para o aluno (Enter para pular)", "")
    doc_padrao = DOC_PADRAO.get(ext, "")
    print(c(DIM, f"  Link padrão da linguagem: {doc_padrao}"))
    doc_url = perguntar("Link da doc (Enter = padrão, '.' = omitir)", doc_padrao)
    if doc_url == ".":
        doc_url = ""

    # ── Salvar ────────────────────────────────────────────────────────────────
    dir_topico.mkdir(parents=True, exist_ok=True)
    destino.write_text(conteudo, encoding="utf-8")

    chave_hint = str(destino.relative_to(BASE)).replace("\\", "/")
    if hint_text or doc_url:
        hints = json.loads(HINTS_FILE.read_text(encoding="utf-8")) if HINTS_FILE.exists() else {}
        hints[chave_hint] = {"dica": hint_text, "doc": doc_url}
        HINTS_FILE.write_text(json.dumps(hints, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # 10. Publicar
    _tela(10, "Publicar no repositório de exercícios", resumo)
    ok(f"Exercício criado: {c(BOLD, chave_hint)}")
    if hint_text or doc_url:
        ok("Hint salvo em hints.json")
    print()

    if perguntar("Publicar via GitHub API? (s/n)", "s").lower() == "s":
        _publicar(destino, conteudo, bool(hint_text or doc_url))

    print()
    print(c(DIM, "  Para iniciar: python codelings.py"))
    print()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        warn("Interrompido.")
        sys.exit(0)
