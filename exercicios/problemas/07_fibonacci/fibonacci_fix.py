# TITULO: Fibonacci - Bug no Range do Loop
# TIPO: fix
# ID: 030

# =================================================================
# ENUNCIADO
# =================================================================
# A funcao gera a sequencia de Fibonacci, mas o range do loop esta
# errado, fazendo com que mais termos do que o pedido sejam gerados.
#
# Corrija o range para que a funcao retorne exatamente n termos.
# =================================================================

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(n):           # <- revise esta linha
        seq.append(seq[-1] + seq[-2])
    return seq

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert fibonacci(1) == [0],                        "caso 1 incorreto"
assert fibonacci(2) == [0, 1],                     "caso 2 incorreto"
assert fibonacci(5) == [0, 1, 1, 2, 3],            "caso 3 incorreto"
assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13], "caso 4 incorreto"
print("fibonacci(8) =", fibonacci(8))
print("Exercicio concluido!")
