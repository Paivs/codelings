# TITULO: Dicionarios - Chave com Case Errado
# TIPO: fix
# ID: 048

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema atualiza uma configuracao existente, mas usa a chave
# com casing diferente do original — em vez de atualizar a entrada
# existente, cria uma entrada duplicada com nome diferente.
# =================================================================

config = {"tema": "claro", "idioma": "pt", "fonte": 14}
config["Tema"] = "escuro"    # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert config["tema"] == "escuro",  f"config['tema'] deveria ser 'escuro', mas e {config.get('tema')!r}"
assert "Tema" not in config,        "a chave 'Tema' nao deveria existir"
assert len(config) == 3,            f"config deveria ter 3 chaves, mas tem {len(config)}"
print(f"config = {config}")
print("Exercicio concluido!")
