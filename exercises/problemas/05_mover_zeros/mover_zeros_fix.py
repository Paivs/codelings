# TITLE: Mover Zeros - Bug no Valor de Preenchimento
# TYPE: fix
# DESCRIPTION: A funcao move os zeros mas preenche as posicoes finais com o valor errado.
# ID: 026

def mover_zeros(nums):
    """Move todos os zeros para o final mantendo a ordem dos demais elementos."""
    nao_zeros = [n for n in nums if n != 0]
    zeros = len(nums) - len(nao_zeros)
    return nao_zeros + [1] * zeros   # BUG: [1] deveria ser [0]


assert mover_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0], \
    f"Caso 1: {mover_zeros([0, 1, 0, 3, 12])}"
assert mover_zeros([0])              == [0],          f"Caso 2: {mover_zeros([0])}"
assert mover_zeros([1, 2, 3])        == [1, 2, 3],    f"Caso 3: {mover_zeros([1, 2, 3])}"
assert mover_zeros([0, 0, 1])        == [1, 0, 0],    f"Caso 4: {mover_zeros([0, 0, 1])}"
print("mover_zeros([0, 1, 0, 3, 12]) =", mover_zeros([0, 1, 0, 3, 12]))
print("mover_zeros([0, 0, 1])        =", mover_zeros([0, 0, 1]))
print("Exercicio concluido!")
