# TITULO: Loops - Condicao de Parada Errada
# TIPO: fix
# ID: 056

# =================================================================
# ENUNCIADO
# =================================================================
# Um gerador de sequencia deve incluir o numero N na lista
# resultante, mas para antes de chegar a ele por causa da condicao
# de parada do loop.
# =================================================================

def sequencia(n):
    i = 1
    resultado = []
    while i < n:    # <- revise esta linha
        resultado.append(i)
        i += 1
    return resultado

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert sequencia(5) == [1, 2, 3, 4, 5], f"sequencia(5) incorreta: {sequencia(5)}"
assert sequencia(1) == [1],             f"sequencia(1) incorreta: {sequencia(1)}"
assert sequencia(3) == [1, 2, 3],       f"sequencia(3) incorreta: {sequencia(3)}"
print(f"sequencia(5) = {sequencia(5)}")
print(f"sequencia(1) = {sequencia(1)}")
print(f"sequencia(3) = {sequencia(3)}")
print("Exercicio concluido!")
