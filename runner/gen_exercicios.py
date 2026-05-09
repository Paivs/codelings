#!/usr/bin/env python3
"""Restaura exercícios que foram modificados acidentalmente.

Consulta o repositório remoto, compara o checksum de cada arquivo local com a
versão canônica e sobrescreve apenas os que divergirem.
"""

import hashlib
import subprocess
import sys
import urllib.error
from pathlib import Path

BASE   = Path(__file__).parent.parent
BRANCH = "main"


def _remote_url() -> str:
    try:
        return subprocess.check_output(
            ["git", "remote", "get-url", "origin"],
            cwd=BASE, stderr=subprocess.DEVNULL,
        ).decode().strip()
    except Exception:
        sys.exit("Erro: não foi possível ler o remote origin do git.")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    from runner.providers import detect_provider

    url = _remote_url()
    provider = detect_provider(url, BRANCH)
    print(f"Repositório: {url}\n")

    exercicios = sorted(
        f for f in BASE.glob("exercises/**/*") if f.is_file()
    )

    if not exercicios:
        sys.exit("Nenhum exercício encontrado em ./exercises/")

    restaurados = sem_alteracao = 0

    for path in exercicios:
        rel = str(path.relative_to(BASE)).replace("\\", "/")
        try:
            remoto = provider.fetch_file(rel)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"  404         {rel}  (não existe no remoto)")
            else:
                print(f"  ERRO {e.code}    {rel}")
            continue
        except Exception as e:
            print(f"  ERRO        {rel}: {e}")
            continue

        local = path.read_bytes() if path.exists() else b""
        if sha256(local) != sha256(remoto):
            path.write_bytes(remoto)
            print(f"  RESTAURADO  {rel}")
            restaurados += 1
        else:
            print(f"  OK          {rel}")
            sem_alteracao += 1

    print(f"\nTotal: {sem_alteracao} sem alteração, {restaurados} restaurado(s).")


if __name__ == "__main__":
    main()
