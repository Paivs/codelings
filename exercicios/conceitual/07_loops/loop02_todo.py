# TITULO: Loops - Analise de Dados
# TIPO: todo
# ID: 015

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de analise recebe uma lista de medicoes e precisa
# calcular estatisticas basicas usando loops for.
#
# Lista: [3, 7, 2, 9, 1, 5, 8, 4, 6]
#
# Resultados esperados:
#   soma  -> 45
#   maior -> 9
#   pares -> [2, 8, 4, 6]  (na ordem em que aparecem)
# =================================================================

numeros = [3, 7, 2, 9, 1, 5, 8, 4, 6]

# TAREFA: Calcule 'soma', 'maior' e a lista 'pares' usando loops for.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert soma          == 45,           "soma incorreta"
assert maior         == 9,            "maior incorreto"
assert sorted(pares) == [2, 4, 6, 8], "pares incorretos"
print(f"Soma  : {soma}")
print(f"Maior : {maior}")
print(f"Pares : {pares}")
print("Exercicio concluido!")
