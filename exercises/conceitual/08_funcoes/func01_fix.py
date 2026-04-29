# TITLE: Funcoes - Return Ausente
# TYPE: fix
# DESCRIPTION: A funcao calcula a area de um retangulo mas nao devolve o resultado.
# ID: 016

def area_retangulo(largura, altura):
    area = largura * altura
    # BUG: falta retornar 'area'

resultado = area_retangulo(5, 3)
assert resultado == 15, f"Esperado 15, obtido {resultado!r}"
print(f"Area do retangulo 5x3 : {resultado}")
print("Exercicio concluido!")
