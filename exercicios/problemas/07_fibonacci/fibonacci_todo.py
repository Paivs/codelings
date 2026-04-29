# TITULO: Fibonacci - Implementar
# TIPO: todo
# ID: 031

# =================================================================
# ENUNCIADO
# =================================================================
# A sequencia de Fibonacci e uma das mais famosas da matematica.
# Cada termo e a soma dos dois anteriores.
#
# Exemplos:
#   fibonacci(1) -> [0]
#   fibonacci(2) -> [0, 1]
#   fibonacci(5) -> [0, 1, 1, 2, 3]
#   fibonacci(8) -> [0, 1, 1, 2, 3, 5, 8, 13]
#
# Regras de negocio:
#   - fibonacci(0) retorna lista vazia []
#   - fibonacci(1) retorna [0]
#   - Os demais termos sao calculados como seq[-1] + seq[-2]
# =================================================================

def fibonacci(n):
    # TAREFA: Trate os casos base (n <= 0 e n == 1) e use um loop
    # para adicionar termos ate a lista ter exatamente n elementos.
    # Comece com seq = [0, 1] e acrescente um termo por iteracao.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert fibonacci(0) == [],                         "caso 1 incorreto"
assert fibonacci(1) == [0],                        "caso 2 incorreto"
assert fibonacci(2) == [0, 1],                     "caso 3 incorreto"
assert fibonacci(5) == [0, 1, 1, 2, 3],            "caso 4 incorreto"
assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13], "caso 5 incorreto"
print("fibonacci(10) =", fibonacci(10))
print("Exercicio concluido!")
