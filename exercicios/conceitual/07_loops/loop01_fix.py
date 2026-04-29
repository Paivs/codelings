# TITULO: Loops - Range Incorreto
# TIPO: fix
# ID: 014

# =================================================================
# ENUNCIADO
# =================================================================
# Um relatorio precisa listar os numeros de 1 a 10, mas o loop
# esta gerando uma sequencia diferente da esperada.
#
# Corrija o range para que a lista contenha exatamente os inteiros
# de 1 a 10, inclusive.
# =================================================================

numeros = []
for i in range(0, 10):    # <- revise esta linha
    numeros.append(i)

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert numeros == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "lista incorreta"
print(f"Numeros: {numeros}")
print("Exercicio concluido!")
