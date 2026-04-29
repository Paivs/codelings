# TITULO: FizzBuzz - Bug no Nome Retornado
# TIPO: fix
# ID: 028

# =================================================================
# ENUNCIADO
# =================================================================
# A funcao FizzBuzz retorna uma string errada para multiplos de 3.
# Em vez de "Fizz", ela retorna "Bizz".
#
# Corrija o valor retornado para multiplos de 3.
# =================================================================

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Bizz"    # <- revise esta linha
    if n % 5 == 0:
        return "Buzz"
    return str(n)

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert fizzbuzz(1)  == "1",        "caso 1 incorreto"
assert fizzbuzz(3)  == "Fizz",     "caso 2 incorreto"
assert fizzbuzz(5)  == "Buzz",     "caso 3 incorreto"
assert fizzbuzz(15) == "FizzBuzz", "caso 4 incorreto"
assert fizzbuzz(9)  == "Fizz",     "caso 5 incorreto"
print("FizzBuzz de 1 a 20:")
print(" ".join(fizzbuzz(i) for i in range(1, 21)))
print("Exercicio concluido!")
