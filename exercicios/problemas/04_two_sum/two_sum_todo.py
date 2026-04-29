# TITULO: Two Sum - Implementar
# TIPO: todo
# ID: 025

# =================================================================
# ENUNCIADO
# =================================================================
# Dado um array de inteiros e um valor alvo, encontre os indices
# de dois numeros que somados sejam iguais ao alvo.
#
# Exemplos:
#   two_sum([2, 7, 11, 15], 9)  ->  [0, 1]   # 2 + 7 = 9
#   two_sum([3, 2, 4], 6)       ->  [1, 2]   # 2 + 4 = 6
#   two_sum([3, 3], 6)          ->  [0, 1]   # 3 + 3 = 6
#
# Regras de negocio:
#   - Cada entrada tem exatamente uma solucao
#   - O mesmo elemento nao pode ser usado duas vezes
#   - Retorne os indices em ordem crescente [menor, maior]
# =================================================================

def two_sum(nums, target):
    # TAREFA: Use um dicionario para guardar cada numero ja visitado
    # e seu indice. Para cada nums[i], calcule o complemento
    # (target - nums[i]). Se o complemento ja estiver no dicionario,
    # retorne os dois indices.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert two_sum([2, 7, 11, 15], 9) == [0, 1], "caso 1 incorreto"
assert two_sum([3, 2, 4], 6)      == [1, 2], "caso 2 incorreto"
assert two_sum([3, 3], 6)         == [0, 1], "caso 3 incorreto"
print("two_sum([2, 7, 11, 15], 9) =", two_sum([2, 7, 11, 15], 9))
print("two_sum([3, 2, 4], 6)      =", two_sum([3, 2, 4], 6))
print("two_sum([3, 3], 6)         =", two_sum([3, 3], 6))
print("Exercicio concluido!")
