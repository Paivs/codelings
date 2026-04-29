# TITLE: Funcoes - Calculadora Simples
# TYPE: todo
# DESCRIPTION: Implemente as quatro operacoes basicas de uma calculadora.
# ID: 017

def somar(a, b):
    # TODO: Retorne a soma de a e b
    pass

def subtrair(a, b):
    # TODO: Retorne a subtracao de a por b
    pass

def multiplicar(a, b):
    # TODO: Retorne o produto de a por b
    pass

def dividir(a, b):
    # TODO: Retorne a divisao de a por b.
    # Se b for 0 (divisao por zero), retorne None.
    pass


# --- Validacao (nao modifique abaixo) ---
assert somar(3, 4)       == 7,    "somar(3, 4) deveria ser 7"
assert subtrair(10, 3)   == 7,    "subtrair(10, 3) deveria ser 7"
assert multiplicar(4, 5) == 20,   "multiplicar(4, 5) deveria ser 20"
assert dividir(15, 3)    == 5,    "dividir(15, 3) deveria ser 5"
assert dividir(10, 0)    is None, "dividir(10, 0) deveria ser None"
print(f"somar(3, 4)       = {somar(3, 4)}")
print(f"subtrair(10, 3)   = {subtrair(10, 3)}")
print(f"multiplicar(4, 5) = {multiplicar(4, 5)}")
print(f"dividir(15, 3)    = {dividir(15, 3)}")
print(f"dividir(10, 0)    = {dividir(10, 0)}")
print("Exercicio concluido!")
