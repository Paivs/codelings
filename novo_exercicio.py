#!/usr/bin/env python3
"""CLI interativo para criar novos exercícios no codelings."""

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).parent
EXERCICIOS = BASE / "exercicios"
HINTS_FILE = BASE / "hints.json"

# ── Terminal colors ────────────────────────────────────────────────────────────

RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[36m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
RED    = "\033[31m"
DIM    = "\033[2m"


def c(color: str, text: str) -> str:
    return f"{color}{text}{RESET}"


def header(text: str) -> None:
    largura = 60
    print()
    print(c(CYAN, "═" * largura))
    print(c(CYAN + BOLD, f"  {text}"))
    print(c(CYAN, "═" * largura))
    print()


def step(num: int, text: str) -> None:
    print(c(BOLD, f"  [{num}] {text}"))


def ok(text: str) -> None:
    print(c(GREEN, f"  ✓ {text}"))


def warn(text: str) -> None:
    print(c(YELLOW, f"  ! {text}"))


def erro(text: str) -> None:
    print(c(RED, f"  ✗ {text}"), file=sys.stderr)


# ── Linguagens suportadas ─────────────────────────────────────────────────────

LINGUAGENS: dict[str, dict] = {
    "Python":     {"ext": ".py",  "comment": "#",  "compiled": False},
    "JavaScript": {"ext": ".js",  "comment": "//", "compiled": False},
    "TypeScript": {"ext": ".ts",  "comment": "//", "compiled": False},
    "Go":         {"ext": ".go",  "comment": "//", "compiled": False},
    "Rust":       {"ext": ".rs",  "comment": "//", "compiled": True},
    "Ruby":       {"ext": ".rb",  "comment": "#",  "compiled": False},
    "Lua":        {"ext": ".lua", "comment": "--", "compiled": False},
    "C":          {"ext": ".c",   "comment": "//", "compiled": True},
}

# Esqueleto de código de exemplo por extensão e tipo
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
}

_TESTES: dict[str, str] = {
    ".py":  'assert minhaFuncao(1) == 2, "caso 1 incorreto"\nprint("Exercicio concluido!")\n',
    ".js":  'console.assert(minhaFuncao(1) === 2, "caso 1 incorreto");\nconsole.log("Exercicio concluido!");\n',
    ".ts":  'console.assert(minhaFuncao(1) === 2, "caso 1 incorreto");\nconsole.log("Exercicio concluido!");\n',
    ".go":  'func main() {\n    if minhaFuncao(1) != 2 { panic("caso 1 incorreto") }\n    fmt.Println("Exercicio concluido!")\n}\n',
    ".rs":  'fn main() {\n    assert_eq!(minha_funcao(1), 2, "caso 1 incorreto");\n    println!("Exercicio concluido!");\n}\n',
    ".rb":  'raise "caso 1 incorreto" unless minhaFuncao(1) == 2\nputs "Exercicio concluido!"\n',
    ".lua": 'assert(minhaFuncao(1) == 2, "caso 1 incorreto")\nprint("Exercicio concluido!")\n',
    ".c":   'int main() {\n    assert(minhaFuncao(1) == 2);\n    printf("Exercicio concluido!\\n");\n    return 0;\n}\n',
}

# ── Helpers ────────────────────────────────────────────────────────────────────

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
                m = re.match(r"ID:\s*(\d+)", s)
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


def escolher(prompt: str, opcoes: list[str], padrao: int = 0) -> str:
    print(f"  {c(BOLD, prompt)}")
    for i, op in enumerate(opcoes, 1):
        marker = c(CYAN, "▸") if i == padrao + 1 else " "
        print(f"  {marker} {c(DIM, str(i) + '.')} {op}")
    print()
    while True:
        raw = input(f"  {c(BOLD, 'Escolha')} [{padrao + 1}]: ").strip()
        if raw == "":
            return opcoes[padrao]
        if raw.isdigit() and 1 <= int(raw) <= len(opcoes):
            return opcoes[int(raw) - 1]
        warn(f"Digite um número entre 1 e {len(opcoes)}")


def perguntar(prompt: str, padrao: str = "") -> str:
    sufixo = f" [{padrao}]" if padrao else ""
    while True:
        val = input(f"  {c(BOLD, prompt)}{sufixo}: ").strip()
        if val:
            return val
        if padrao:
            return padrao
        warn("Campo obrigatório.")


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


# ── Template ──────────────────────────────────────────────────────────────────

def gerar_template(titulo: str, tipo: str, id_num: int, ext: str, comment: str) -> str:
    sep_char = "=" * (63 - len(comment))
    sep = f"{comment} {sep_char}"

    instrucao_fix = (
        f"{comment} Descreva o bug existente. Seja específico sobre qual linha\n"
        f"{comment} está errada e o que precisa ser corrigido.\n"
        f"{comment} Use  <- revise esta linha  para marcar a linha bugada."
    )
    instrucao_todo = (
        f"{comment} Descreva o que o aluno precisa implementar.\n"
        f"{comment} Inclua exemplos de entrada/saída e regras de negócio."
    )
    instrucao = instrucao_fix if tipo == "fix" else instrucao_todo

    corpo  = _CORPO.get(ext, {}).get(tipo, f"// TODO: código aqui\n")
    testes = _TESTES.get(ext, f'// TODO: testes aqui\n')

    linhas = [
        f"{comment} TITULO: {titulo}",
        f"{comment} TIPO: {tipo}",
        f"{comment} ID: {id_num:03d}",
        "",
        sep,
        f"{comment} ENUNCIADO",
        sep,
        instrucao,
        sep,
        "",
        corpo,
        sep,
        f"{comment} TESTES (nao modifique abaixo)",
        sep,
        testes,
    ]
    return "\n".join(linhas)


# ── Main flow ──────────────────────────────────────────────────────────────────

def main() -> None:
    header("novo_exercicio — codelings")

    # 1. Linguagem
    step(1, "Linguagem")
    nomes_lang = list(LINGUAGENS.keys())
    nome_lang = escolher("", nomes_lang)
    lang_cfg = LINGUAGENS[nome_lang]
    ext      = lang_cfg["ext"]
    comment  = lang_cfg["comment"]

    # 2. Categoria
    step(2, "Categoria do exercício")
    categoria = escolher("", ["conceitual", "problemas"])

    # 3. Tipo  (problemas são sempre todo)
    if categoria == "problemas":
        tipo = "todo"
        print(f"  Tipo: {c(DIM, 'todo')}  {c(DIM, '(problemas são sempre todo)')}\n")
    else:
        step(3, "Tipo do exercício")
        tipo = escolher("", ["fix  — código com bug para corrigir", "todo  — função para implementar"])
        tipo = tipo.split()[0]

    # 4. Tópico / diretório
    step(4, "Diretório de tópico")
    topicos_existentes = listar_topicos(categoria)
    nomes_topicos      = [d.name for d in topicos_existentes]
    opcoes_topico      = nomes_topicos + ["[+ novo tópico]"]
    escolhido          = escolher("Tópico:", opcoes_topico)

    if escolhido == "[+ novo tópico]":
        slug_topico = perguntar("Slug do novo tópico (ex: recursao, classes)")
        prox_num    = len(topicos_existentes) + 1
        nome_dir    = f"{prox_num:02d}_{slug_topico}"
    else:
        nome_dir = escolhido
        if categoria == "problemas":
            existentes = list((EXERCICIOS / categoria / nome_dir).glob("*"))
            existentes = [f for f in existentes if f.is_file()]
            if existentes:
                warn(f"Este tópico já tem {len(existentes)} exercício(s). Problemas têm 1 por tópico.")
                if perguntar("Continuar mesmo assim? (s/n)", "n").lower() != "s":
                    erro("Cancelado.")
                    sys.exit(1)

    dir_topico = EXERCICIOS / categoria / nome_dir

    # 5. ID
    id_sugerido = proximo_id()
    step(5, "ID do exercício")
    raw_id = perguntar("ID", str(id_sugerido))
    id_num = int(raw_id)

    # 6. Título
    step(6, "Título")
    titulo = perguntar("Título (ex: Palindromo - Bug na Inversao)")

    # 7. Nome do arquivo
    step(7, "Nome do arquivo")
    slug_padrao  = nome_dir.split("_", 1)[-1].replace("-", "_")
    slug_arquivo = perguntar(f"Slug do arquivo sem extensão (ex: palindrome, var03)", slug_padrao)
    nome_arquivo = f"{slug_arquivo}_{tipo}{ext}"
    destino      = dir_topico / nome_arquivo

    if destino.exists():
        warn(f"Arquivo já existe: {destino.relative_to(BASE)}")
        if perguntar("Sobrescrever? (s/n)", "n").lower() != "s":
            erro("Cancelado.")
            sys.exit(1)

    # 8. Editar template
    step(8, "Conteúdo do exercício")
    print(f"  Abrindo editor ({os.environ.get('EDITOR', 'nano')})…")
    print(c(DIM, "  Preencha ENUNCIADO e TESTES, salve e feche.\n"))
    template = gerar_template(titulo, tipo, id_num, ext, comment)
    conteudo = abrir_editor(template)

    # 9. Hint
    step(9, "Dica (hint)")
    hint = perguntar("Dica curta para o aluno (ou Enter para pular)", "")

    # ── Salvar ────────────────────────────────────────────────────────────────
    dir_topico.mkdir(parents=True, exist_ok=True)
    destino.write_text(conteudo, encoding="utf-8")

    chave_hint = str(destino.relative_to(BASE)).replace("\\", "/")
    if hint:
        hints = json.loads(HINTS_FILE.read_text(encoding="utf-8")) if HINTS_FILE.exists() else {}
        hints[chave_hint] = hint
        HINTS_FILE.write_text(
            json.dumps(hints, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print()
    ok(f"Exercício criado: {c(BOLD, chave_hint)}")
    if hint:
        ok("Hint salvo em hints.json")
    print()
    print(c(DIM, f"  Para iniciar: python codelings.py"))
    print()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        warn("Interrompido.")
        sys.exit(0)
