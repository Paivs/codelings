# TITULO: Mover Zeros - Implementar
# TIPO: todo
# ID: 027

# =================================================================
# ENUNCIADO
# =================================================================
# Dada uma lista de inteiros, mova todos os zeros para o final
# sem alterar a ordem relativa dos outros elementos.
#
# Exemplos:
#   mover_zeros([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
#   mover_zeros([0])               -> [0]
#   mover_zeros([1, 2, 3])         -> [1, 2, 3]
#
# Regras de negocio:
#   - A ordem dos elementos nao-zero deve ser preservada
#   - Retorne uma nova lista (nao modifique a original)
# =================================================================

def mover_zeros(nums):
    # TAREFA: Separe os elementos nao-zero em uma lista. Calcule
    # quantos zeros existem e concatene-os ao final.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert mover_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0], "caso 1 incorreto"
assert mover_zeros([0])              == [0],               "caso 2 incorreto"
assert mover_zeros([1, 2, 3])        == [1, 2, 3],         "caso 3 incorreto"
assert mover_zeros([0, 0, 1])        == [1, 0, 0],         "caso 4 incorreto"
assert mover_zeros([0, 0, 0])        == [0, 0, 0],         "caso 5 incorreto"
assert mover_zeros([4, 0, 2, 0, 5])  == [4, 2, 5, 0, 0],  "caso 6 incorreto"
print("mover_zeros([0, 1, 0, 3, 12]) =", mover_zeros([0, 1, 0, 3, 12]))
print("mover_zeros([4, 0, 2, 0, 5])  =", mover_zeros([4, 0, 2, 0, 5]))
print("Exercicio concluido!")
