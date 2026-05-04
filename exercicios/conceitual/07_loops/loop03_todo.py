# TITULO: Loops - Multiplos de N
# TIPO: todo
# ID: 057

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema matematico lista todos os multiplos de um numero
# dentro de um intervalo e calcula estatisticas sobre eles.
#
# numero = 7, limite = 70
#
# Resultados esperados:
#   multiplos   -> [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
#   quantidade  -> 10
#   soma        -> 385
# =================================================================

numero = 7
limite = 70

# TAREFA: Crie 'multiplos', 'quantidade' e 'soma' usando um loop.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert multiplos  == [7, 14, 21, 28, 35, 42, 49, 56, 63, 70], f"multiplos incorretos: {multiplos}"
assert quantidade == 10,                                        f"quantidade incorreta: {quantidade}"
assert soma       == 385,                                       f"soma incorreta: {soma}"
print(f"multiplos  = {multiplos}")
print(f"quantidade = {quantidade}")
print(f"soma       = {soma}")
print("Exercicio concluido!")
