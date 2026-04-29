# TITLE: Listas - Operacoes Basicas
# TYPE: todo
# DESCRIPTION: Complete as operacoes com a lista 'numeros' conforme os TODO.
# ID: 009

numeros = [5, 2, 8, 1, 9, 3]

# TODO: Adicione o numero 7 ao final da lista

# TODO: Remova o numero 2 da lista

# TODO: Ordene a lista em ordem crescente (modifique a propria lista)

# TODO: Armazene em 'total' a soma de todos os elementos da lista

# TODO: Armazene em 'tamanho' a quantidade de elementos da lista


# --- Validacao (nao modifique abaixo) ---
assert 7 in numeros, "7 deveria estar na lista"
assert 2 not in numeros, "2 nao deveria mais estar na lista"
assert numeros == sorted(numeros), f"A lista deveria estar ordenada: {numeros}"
assert total == sum(numeros), f"'total' deveria ser {sum(numeros)}, mas e {total}"
assert tamanho == len(numeros), f"'tamanho' deveria ser {len(numeros)}, mas e {tamanho}"
print(f"Lista    : {numeros}")
print(f"Total    : {total}")
print(f"Tamanho  : {tamanho}")
print("Exercicio concluido!")
