# TITLE: Fibonacci - Implementar
# TYPE: todo
# DESCRIPTION: Implemente a funcao que gera os N primeiros numeros de Fibonacci.
# ID: 031

def fibonacci(n):
    """
    Retorna uma lista com os primeiros n numeros da sequencia de Fibonacci.
    Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13 ...
    Cada termo e a soma dos dois anteriores.

    fibonacci(1) -> [0]
    fibonacci(2) -> [0, 1]
    fibonacci(5) -> [0, 1, 1, 2, 3]
    fibonacci(8) -> [0, 1, 1, 2, 3, 5, 8, 13]
    """
    # TODO: Implemente a funcao.
    # Dica: comece com [0, 1] e acrescente a soma dos dois ultimos ate ter n termos.
    pass


# --- Validacao (nao modifique abaixo) ---
assert fibonacci(0) == [],                         f"fibonacci(0): {fibonacci(0)}"
assert fibonacci(1) == [0],                        f"fibonacci(1): {fibonacci(1)}"
assert fibonacci(2) == [0, 1],                     f"fibonacci(2): {fibonacci(2)}"
assert fibonacci(5) == [0, 1, 1, 2, 3],            f"fibonacci(5): {fibonacci(5)}"
assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13], f"fibonacci(8): {fibonacci(8)}"
print("fibonacci(10) =", fibonacci(10))
print("Exercicio concluido!")
