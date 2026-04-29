# TITLE: Two Sum - Implementar
# TYPE: todo
# DESCRIPTION: Retorne os indices de dois numeros que somam o alvo. Solucao em O(n).
# ID: 025

def two_sum(nums, target):
    """
    Dado uma lista 'nums' e um inteiro 'target', retorna [i, j] tal que
    nums[i] + nums[j] == target. Cada entrada tem exatamente uma solucao.

    two_sum([2, 7, 11, 15], 9)  -> [0, 1]   (2 + 7 = 9)
    two_sum([3, 2, 4], 6)       -> [1, 2]   (2 + 4 = 6)
    two_sum([3, 3], 6)          -> [0, 1]   (3 + 3 = 6)
    """
    # TODO: Use um dicionario para resolver em O(n).
    # Para cada nums[i], o complemento necessario e target - nums[i].
    # Se esse complemento ja estiver no dicionario, encontrou o par!
    pass


# --- Validacao (nao modifique abaixo) ---
assert two_sum([2, 7, 11, 15], 9) == [0, 1], f"Caso 1: {two_sum([2, 7, 11, 15], 9)}"
assert two_sum([3, 2, 4], 6)      == [1, 2], f"Caso 2: {two_sum([3, 2, 4], 6)}"
assert two_sum([3, 3], 6)         == [0, 1], f"Caso 3: {two_sum([3, 3], 6)}"
print("two_sum([2, 7, 11, 15], 9) =", two_sum([2, 7, 11, 15], 9))
print("two_sum([3, 2, 4], 6)      =", two_sum([3, 2, 4], 6))
print("two_sum([3, 3], 6)         =", two_sum([3, 3], 6))
print("Exercicio concluido!")
