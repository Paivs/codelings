# TITULO: Variaveis - Erro de Digitacao
# TIPO: fix
# ID: 001

# =================================================================
# ENUNCIADO
# =================================================================
# O sistema de cadastro abaixo deveria exibir os dados de um
# usuario, mas ha um erro de digitacao no nome de uma variavel.
#
# Corrija o codigo para que ele rode sem erros.
# =================================================================

nome   = "Ana"
iddade = 22
cidade = "Recife"

print(f"Nome  : {nome}")
print(f"Idade : {idade}")     # <- revise esta linha
print(f"Cidade: {cidade}")

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert nome   == "Ana",    "nome incorreto"
assert idade  == 22,       "idade incorreta"
assert cidade == "Recife", "cidade incorreta"
print("Exercicio concluido!")
