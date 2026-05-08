# TITULO: Listas - Indice Fora do Intervalo
# TIPO: fix
# ID: 008

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de estoque tenta exibir a primeira, a segunda e a
# ultima fruta de uma lista, mas o indice do ultimo elemento
# esta errado.
#
# Corrija o acesso ao ultimo elemento da lista.
# =================================================================

frutas = ["maca", "banana", "laranja", "uva"]

print(f"Primeira: {frutas[0]}")
print(f"Segunda : {frutas[1]}")
print(f"Ultima  : {frutas[4]}")    # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert frutas[0]  == "maca",   "primeira fruta incorreta"
assert frutas[1]  == "banana", "segunda fruta incorreta"
assert frutas[-1] == "uva",    "ultima fruta incorreta"
print("Exercicio concluido!")
