# TITULO: Dicionarios - Soma de Valores
# TIPO: fix
# ID: 047

# =================================================================
# ENUNCIADO
# =================================================================
# Um caixa calcula o total dos precos de produtos, mas a operacao
# de soma esta iterando sobre as chaves do dicionario em vez dos
# valores, causando um TypeError.
# =================================================================

precos = {"maca": 2.50, "banana": 1.20, "laranja": 3.00}
total  = sum(precos)    # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert abs(total - 6.70) < 0.01, f"total incorreto: {total}"
print(f"precos = {precos}")
print(f"total  = R$ {total:.2f}")
print("Exercicio concluido!")
