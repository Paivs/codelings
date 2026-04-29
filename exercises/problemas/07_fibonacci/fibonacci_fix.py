# TITLE: Fibonacci - Bug no Loop
# TYPE: fix
# DESCRIPTION: A funcao gera termos a mais porque o range esta incorreto.
# ID: 030

def fibonacci(n):
    """Retorna uma lista com os primeiros n numeros da sequencia de Fibonacci."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(n):       # BUG: deveria ser range(n - 2)
        seq.append(seq[-1] + seq[-2])
    return seq


assert fibonacci(1) == [0],                        f"fibonacci(1): {fibonacci(1)}"
assert fibonacci(2) == [0, 1],                     f"fibonacci(2): {fibonacci(2)}"
assert fibonacci(5) == [0, 1, 1, 2, 3],            f"fibonacci(5): {fibonacci(5)}"
assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13], f"fibonacci(8): {fibonacci(8)}"
print("fibonacci(8) =", fibonacci(8))
print("Exercicio concluido!")
