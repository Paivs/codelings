# TITLE: Mover Zeros - Implementar
# TYPE: todo
# DESCRIPTION: Mova todos os zeros para o final mantendo a ordem dos outros elementos.
# ID: 027

def mover_zeros(nums):
    """
    Retorna uma nova lista com todos os zeros movidos para o final.
    A ordem relativa dos elementos nao-zero deve ser preservada.

    mover_zeros([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
    mover_zeros([0])               -> [0]
    mover_zeros([1, 2, 3])         -> [1, 2, 3]
    mover_zeros([0, 0, 1])         -> [1, 0, 0]
    """
    # TODO: Implemente a funcao.
    # Dica: Separe os elementos nao-zero e depois concatene os zeros no final.
    pass


# --- Validacao (nao modifique abaixo) ---
assert mover_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert mover_zeros([0])              == [0]
assert mover_zeros([1, 2, 3])        == [1, 2, 3]
assert mover_zeros([0, 0, 1])        == [1, 0, 0]
assert mover_zeros([0, 0, 0])        == [0, 0, 0]
assert mover_zeros([4, 0, 2, 0, 5])  == [4, 2, 5, 0, 0]
print("mover_zeros([0, 1, 0, 3, 12]) =", mover_zeros([0, 1, 0, 3, 12]))
print("mover_zeros([4, 0, 2, 0, 5])  =", mover_zeros([4, 0, 2, 0, 5]))
print("mover_zeros([1, 2, 3])        =", mover_zeros([1, 2, 3]))
print("Exercicio concluido!")
