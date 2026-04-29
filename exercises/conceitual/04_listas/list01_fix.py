# TITLE: Listas - Indice Fora do Intervalo
# TYPE: fix
# DESCRIPTION: O codigo tenta acessar um indice que nao existe na lista.
# ID: 008

frutas = ["maca", "banana", "laranja", "uva"]

print(f"Primeira fruta : {frutas[0]}")
print(f"Segunda fruta  : {frutas[1]}")
print(f"Ultima fruta   : {frutas[4]}")
