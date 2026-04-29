# TITULO: Two Sum - Bug no Calculo do Complemento
# TIPO: fix
# ID: 024

# =================================================================
# ENUNCIADO
# =================================================================
# A funcao two_sum encontra os indices de dois numeros que somam
# o alvo, mas o complemento esta sendo calculado de forma errada,
# fazendo a busca procurar o par incorreto.
#
# Corrija a operacao matematica que calcula o complemento.
# =================================================================

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        comp = target + n       # <- revise esta linha
        if comp in seen:
            return [seen[comp], i]
        seen[n] = i

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert two_sum([2, 7, 11, 15], 9) == [0, 1], "caso 1 incorreto"
assert two_sum([3, 2, 4], 6)      == [1, 2], "caso 2 incorreto"
assert two_sum([3, 3], 6)         == [0, 1], "caso 3 incorreto"
print("two_sum([2, 7, 11, 15], 9) =", two_sum([2, 7, 11, 15], 9))
print("two_sum([3, 2, 4], 6)      =", two_sum([3, 2, 4], 6))
print("Exercicio concluido!")
