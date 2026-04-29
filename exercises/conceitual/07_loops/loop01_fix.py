# TITLE: Loops - Range Incorreto
# TYPE: fix
# DESCRIPTION: O loop deveria coletar os numeros de 1 a 10, mas o range esta errado.
# ID: 014

numeros = []
for i in range(0, 10):   # BUG: deveria comecar em 1 e ir ate 10 incluso
    numeros.append(i)

assert numeros == list(range(1, 11)), \
    f"Esperado {list(range(1, 11))}\nObtido   {numeros}"
print(f"Numeros: {numeros}")
print("Exercicio concluido!")
