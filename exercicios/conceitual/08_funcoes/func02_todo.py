# TITULO: Funcoes - Calculadora
# TIPO: todo
# ID: 017

# =================================================================
# ENUNCIADO
# =================================================================
# Um aplicativo de calculadora precisa das quatro operacoes basicas.
#
# Exemplos:
#   somar(3, 4)       -> 7
#   subtrair(10, 3)   -> 7
#   multiplicar(4, 5) -> 20
#   dividir(15, 3)    -> 5.0
#   dividir(10, 0)    -> None
#
# Regras de negocio:
#   - Cada funcao recebe dois numeros e retorna o resultado
#   - dividir() retorna None quando o divisor for zero
# =================================================================

# TAREFA: Implemente as quatro funcoes abaixo.

def somar(a, b):
    pass

def subtrair(a, b):
    pass

def multiplicar(a, b):
    pass

def dividir(a, b):
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert somar(3, 4)       == 7,    "somar incorreto"
assert subtrair(10, 3)   == 7,    "subtrair incorreto"
assert multiplicar(4, 5) == 20,   "multiplicar incorreto"
assert dividir(15, 3)    == 5,    "dividir incorreto"
assert dividir(10, 0)    is None, "divisao por zero deve retornar None"
print(f"somar(3, 4)       = {somar(3, 4)}")
print(f"subtrair(10, 3)   = {subtrair(10, 3)}")
print(f"multiplicar(4, 5) = {multiplicar(4, 5)}")
print(f"dividir(15, 3)    = {dividir(15, 3)}")
print(f"dividir(10, 0)    = {dividir(10, 0)}")
print("Exercicio concluido!")
