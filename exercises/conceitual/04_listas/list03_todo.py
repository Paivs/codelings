# TITULO: Listas - Filtrar Pares
# TIPO: todo
# ID: 045

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de analise precisa separar e calcular estatisticas
# dos numeros pares de uma lista.
#
# Lista inicial: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Resultados esperados:
#   pares            -> [2, 4, 6, 8, 10]  (em ordem)
#   soma_pares       -> 30
#   quantidade_pares -> 5
# =================================================================

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TAREFA: Crie 'pares', 'soma_pares' e 'quantidade_pares' a partir de 'numeros'.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert pares            == [2, 4, 6, 8, 10], f"pares incorretos: {pares}"
assert soma_pares       == 30,               f"soma_pares incorreta: {soma_pares}"
assert quantidade_pares == 5,                f"quantidade_pares incorreta: {quantidade_pares}"
print(f"pares            = {pares}")
print(f"soma_pares       = {soma_pares}")
print(f"quantidade_pares = {quantidade_pares}")
print("Exercicio concluido!")
