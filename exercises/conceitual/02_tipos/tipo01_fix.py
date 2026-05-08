# TITULO: Tipos - Entrada como String
# TIPO: fix
# ID: 004

# =================================================================
# ENUNCIADO
# =================================================================
# Um formulario captura o ano de nascimento e tenta calcular ha
# quantos anos o usuario nasceu, mas o codigo quebra.
#
# Lembre-se: valores vindos de input() sao sempre strings.
# Corrija o codigo para que o calculo funcione.
# =================================================================

entrada    = "2005"
ano_atual  = 2024
anos_atras = ano_atual - entrada    # <- revise esta linha

print(f"Voce nasceu ha {anos_atras} anos.")

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert anos_atras == 19, "calculo incorreto"
print("Exercicio concluido!")
