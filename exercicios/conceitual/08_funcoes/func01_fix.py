# TITULO: Funcoes - Return Ausente
# TIPO: fix
# ID: 016

# =================================================================
# ENUNCIADO
# =================================================================
# Uma funcao calcula a area de um retangulo, mas nao devolve
# o resultado para quem a chamou. Por isso, 'resultado' recebe
# None em vez do valor calculado.
#
# Adicione o comando necessario para a funcao devolver o valor.
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
