#!/usr/bin/env python3
"""Restaura exercícios que foram modificados acidentalmente.

Consulta o repositório remoto (GitHub), compara o checksum de cada arquivo
local com a versão canônica e sobrescreve apenas os que divergirem.
"""

import hashlib
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

BASE   = Path(__file__).parent
BRANCH = "main"


def remote_raw_base() -> str:
    """Deriva a URL raw do GitHub a partir do git remote origin."""
    try:
        url = subprocess.check_output(
            ["git", "remote", "get-url", "origin"],
            cwd=BASE, stderr=subprocess.DEVNULL,
        ).decode().strip()
    except Exception:
        sys.exit("Erro: não foi possível ler o remote origin do git.")

    # https://github.com/user/repo(.git)?
    m = re.match(r"https://github\.com/([^/]+/[^/]+?)(?:\.git)?$", url)
    if not m:
        # git@github.com:user/repo(.git)?
        m = re.match(r"git@github\.com:([^/]+/[^/]+?)(?:\.git)?$", url)
    if not m:
        sys.exit(f"Erro: formato de remote não reconhecido: {url}")

    return f"https://raw.githubusercontent.com/{m.group(1)}/{BRANCH}"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fetch(raw_base: str, rel: str) -> str | None:
    url = f"{raw_base}/{rel}"
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            return r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"  404         {rel}  (não existe no remoto)")
        else:
            print(f"  ERRO {e.code}    {rel}")
        return None
    except Exception as e:
        print(f"  ERRO        {rel}: {e}")
        return None


def main() -> None:
    raw_base = remote_raw_base()
    print(f"Repositório: {raw_base}\n")

    exercicios = sorted(
        f for f in BASE.glob("exercicios/**/*") if f.is_file()
    )

    if not exercicios:
        sys.exit("Nenhum exercício encontrado em ./exercicios/")

    restaurados = 0
    sem_alteracao = 0

    for path in exercicios:
        rel    = str(path.relative_to(BASE)).replace("\\", "/")
        remoto = fetch(raw_base, rel)
        if remoto is None:
            continue

        local = path.read_text(encoding="utf-8") if path.exists() else ""

        if sha256(local) != sha256(remoto):
            path.write_text(remoto, encoding="utf-8")
            print(f"  RESTAURADO  {rel}")
            restaurados += 1
        else:
            print(f"  OK          {rel}")
            sem_alteracao += 1

    print(f"\nTotal: {sem_alteracao} sem alteração, {restaurados} restaurado(s).")


if __name__ == "__main__":
    main()
