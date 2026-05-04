# TITULO: Funcoes - Return Ausente
# TIPO: fix
# ID: 016

# =================================================================
# ENUNCIADO
# =================================================================
# A funcao calcula a area de um retangulo mas o valor calculado
# nunca chega a quem chamou a funcao.
#
# Corrija o codigo para que o resultado seja retornado corretamente.
# =================================================================

def area_retangulo(largura, altura):
    area = largura * altura
    # <- falta algo aqui

resultado = area_retangulo(5, 3)

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert resultado == 15, "resultado incorreto — verifique o retorno da funcao"
print(f"Area do retangulo 5x3: {resultado}")
print("Exercicio concluido!")
