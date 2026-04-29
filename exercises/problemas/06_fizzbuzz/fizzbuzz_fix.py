# TITLE: FizzBuzz - Bug no Nome
# TYPE: fix
# DESCRIPTION: A funcao FizzBuzz retorna a palavra errada para multiplos de 3.
# ID: 028

def fizzbuzz(n):
    """Multiplos de 3->Fizz, 5->Buzz, ambos->FizzBuzz, outros->str(n)."""
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Bizz"    # BUG: deveria ser "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


casos = {1:"1", 3:"Fizz", 5:"Buzz", 9:"Fizz", 10:"Buzz", 15:"FizzBuzz", 30:"FizzBuzz"}
for num, esp in casos.items():
    assert str(fizzbuzz(num)) == esp, f"fizzbuzz({num}): esperado '{esp}', obtido '{fizzbuzz(num)}'"
print("FizzBuzz de 1 a 20:")
print(" ".join(fizzbuzz(i) for i in range(1, 21)))
print("Exercicio concluido!")
