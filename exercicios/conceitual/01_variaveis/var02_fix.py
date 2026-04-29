# TITULO: Variaveis - Incompatibilidade de Tipos
# TIPO: fix
# ID: 002

# =================================================================
# ENUNCIADO
# =================================================================
# Um formulario recebe o ano de nascimento como texto e tenta
# calcular ha quantos anos isso foi, mas o codigo quebra.
#
# Corrija o codigo para que o calculo funcione corretamente.
# =================================================================

ano_nascimento = "1999"
ano_atual      = 2024
anos_atras     = ano_atual - ano_nascimento    # <- revise esta linha

print(f"Voce nasceu ha {anos_atras} anos.")

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert anos_atras == 25, "calculo do tempo incorreto"
print("Exercicio concluido!")
