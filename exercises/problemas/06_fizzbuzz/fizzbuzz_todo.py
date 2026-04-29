# TITLE: FizzBuzz - Implementar
# TYPE: todo
# DESCRIPTION: Implemente o classico FizzBuzz. Multiplos de 3->Fizz, 5->Buzz, ambos->FizzBuzz.
# ID: 029

def fizzbuzz(n):
    """
    Para um numero inteiro n, retorna (como string):
      "FizzBuzz" se n for divisivel por 3 e por 5
      "Fizz"     se n for divisivel apenas por 3
      "Buzz"     se n for divisivel apenas por 5
      str(n)     caso contrario
    """
    # TODO: Implemente a logica.
    # Use o operador % (modulo) para verificar divisibilidade.
    # Verifique primeiro o caso FizzBuzz (divisivel por 3 E por 5).
    pass


# --- Validacao (nao modifique abaixo) ---
casos = {
    1:"1", 2:"2", 3:"Fizz", 4:"4", 5:"Buzz",
    6:"Fizz", 9:"Fizz", 10:"Buzz", 15:"FizzBuzz", 30:"FizzBuzz",
}
for num, esp in casos.items():
    assert str(fizzbuzz(num)) == esp, \
        f"fizzbuzz({num}): esperado '{esp}', obtido '{fizzbuzz(num)}'"
print("FizzBuzz de 1 a 20:")
print(" ".join(fizzbuzz(i) for i in range(1, 21)))
print("Exercicio concluido!")
