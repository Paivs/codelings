# TITLE: Loops - Acumulando com For
# TYPE: todo
# DESCRIPTION: Use loops for para calcular soma, maximo e filtrar pares.
# ID: 015

numeros = [3, 7, 2, 9, 1, 5, 8, 4, 6]

# TODO: Use um loop for para calcular a soma de todos os numeros.
#       Armazene o resultado em 'soma'.


# TODO: Use um loop for para encontrar o maior numero.
#       Armazene o resultado em 'maior'.


# TODO: Use um loop for para criar a lista 'pares' com apenas os numeros pares.


# --- Validacao (nao modifique abaixo) ---
assert soma == 45, f"'soma' deveria ser 45, mas e {soma}"
assert maior == 9, f"'maior' deveria ser 9, mas e {maior}"
assert sorted(pares) == [2, 4, 6, 8], f"'pares' deveria ser [2, 4, 6, 8] (em qualquer ordem), mas e {sorted(pares)}"
print(f"Numeros : {numeros}")
print(f"Soma    : {soma}")
print(f"Maior   : {maior}")
print(f"Pares   : {pares}")
print("Exercicio concluido!")
