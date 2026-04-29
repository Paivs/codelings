# TITLE: Two Sum - Bug no Calculo do Complemento
# TYPE: fix
# DESCRIPTION: A funcao busca o par errado porque o complemento e calculado incorretamente.
# ID: 024

def two_sum(nums, target):
    """Retorna [i, j] tal que nums[i] + nums[j] == target."""
    seen = {}
    for i, n in enumerate(nums):
        comp = target + n       # BUG: deveria ser target - n
        if comp in seen:
            return [seen[comp], i]
        seen[n] = i


assert two_sum([2, 7, 11, 15], 9) == [0, 1], f"Caso 1: {two_sum([2, 7, 11, 15], 9)}"
assert two_sum([3, 2, 4], 6)      == [1, 2], f"Caso 2: {two_sum([3, 2, 4], 6)}"
assert two_sum([3, 3], 6)         == [0, 1], f"Caso 3: {two_sum([3, 3], 6)}"
print("two_sum([2, 7, 11, 15], 9) =", two_sum([2, 7, 11, 15], 9))
print("two_sum([3, 2, 4], 6)      =", two_sum([3, 2, 4], 6))
print("two_sum([3, 3], 6)         =", two_sum([3, 3], 6))
print("Exercicio concluido!")
