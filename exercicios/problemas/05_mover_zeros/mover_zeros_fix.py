# TITULO: Mover Zeros - Bug no Valor de Preenchimento
# TIPO: fix
# ID: 026

# =================================================================
# ENUNCIADO
# =================================================================
# A funcao move todos os zeros para o final da lista, mas preenche
# as posicoes finais com o valor errado.
#
# Corrija o valor usado para preencher as posicoes dos zeros.
# =================================================================

def mover_zeros(nums):
    nao_zeros = [n for n in nums if n != 0]
    zeros     = len(nums) - len(nao_zeros)
    return nao_zeros + [1] * zeros   # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert mover_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0], "caso 1 incorreto"
assert mover_zeros([0])              == [0],               "caso 2 incorreto"
assert mover_zeros([1, 2, 3])        == [1, 2, 3],         "caso 3 incorreto"
assert mover_zeros([0, 0, 1])        == [1, 0, 0],         "caso 4 incorreto"
print("mover_zeros([0, 1, 0, 3, 12]) =", mover_zeros([0, 1, 0, 3, 12]))
print("mover_zeros([0, 0, 1])        =", mover_zeros([0, 0, 1]))
print("Exercicio concluido!")
