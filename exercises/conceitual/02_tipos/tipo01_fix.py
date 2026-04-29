# TITLE: Tipos - Conversao Implicita
# TYPE: fix
# DESCRIPTION: O codigo calcula o ano de nascimento mas ha um erro de tipo.
# ID: 004

entrada = "2005"

ano_atual = 2024
anos_atras = ano_atual - int(entrada)

print(f"Voce nasceu ha {anos_atras} anos.")
