# TITULO: FizzBuzz - Implementar
# TIPO: todo
# ID: 029

# =================================================================
# ENUNCIADO
# =================================================================
# FizzBuzz e um problema classico de programacao.
#
# Exemplos:
#   fizzbuzz(1)  -> "1"
#   fizzbuzz(3)  -> "Fizz"
#   fizzbuzz(5)  -> "Buzz"
#   fizzbuzz(15) -> "FizzBuzz"
#
# Regras de negocio (verificar nesta ordem):
#   1. Divisivel por 3 E por 5  -> "FizzBuzz"
#   2. Divisivel apenas por 3   -> "Fizz"
#   3. Divisivel apenas por 5   -> "Buzz"
#   4. Qualquer outro numero    -> str(n)
# =================================================================

def fizzbuzz(n):
    # TAREFA: Implemente as quatro regras usando o operador % (modulo).
    # A ordem das verificacoes importa: teste FizzBuzz antes de Fizz e Buzz.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert fizzbuzz(1)  == "1",        "caso 1 incorreto"
assert fizzbuzz(3)  == "Fizz",     "caso 2 incorreto"
assert fizzbuzz(5)  == "Buzz",     "caso 3 incorreto"
assert fizzbuzz(15) == "FizzBuzz", "caso 4 incorreto"
assert fizzbuzz(9)  == "Fizz",     "caso 5 incorreto"
assert fizzbuzz(10) == "Buzz",     "caso 6 incorreto"
assert fizzbuzz(30) == "FizzBuzz", "caso 7 incorreto"
print("FizzBuzz de 1 a 20:")
print(" ".join(fizzbuzz(i) for i in range(1, 21)))
print("Exercicio concluido!")
