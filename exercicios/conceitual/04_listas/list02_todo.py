# TITULO: Listas - Gerenciamento de Estoque
# TIPO: todo
# ID: 009

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de controle de estoque realiza operacoes sobre
# uma lista de codigos de produtos (representados por numeros).
#
# Lista inicial: [5, 2, 8, 1, 9, 3]
#
# Operacoes necessarias (nesta ordem):
#   1. Adicionar o numero 7 ao final da lista
#   2. Remover o numero 2 da lista
#   3. Ordenar a lista em ordem crescente
#   4. Calcular a soma total  -> guardar em 'total'
#   5. Contar os elementos    -> guardar em 'tamanho'
# =================================================================

numeros = [5, 2, 8, 1, 9, 3]

# TAREFA: Execute as cinco operacoes sobre a lista 'numeros'.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert numeros == [1, 3, 5, 7, 8, 9], "lista incorreta apos as operacoes"
assert total   == 33,                  "total incorreto"
assert tamanho == 6,                   "tamanho incorreto"
print(f"Lista  : {numeros}")
print(f"Total  : {total}")
print(f"Tamanho: {tamanho}")
print("Exercicio concluido!")
