# TITULO: Tipos - Multiplicacao com String
# TIPO: fix
# ID: 035

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema recebe um valor como texto e calcula o dobro dele,
# mas o resultado esta errado porque o valor nao foi convertido
# para numero antes da operacao.
# =================================================================

entrada = "7"
dobro   = entrada * 2    # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert dobro == 14,             f"dobro deveria ser 14, mas e {dobro!r}"
assert isinstance(dobro, int),  "dobro deve ser int"
print(f"entrada = {entrada!r}")
print(f"dobro   = {dobro}")
print("Exercicio concluido!")
