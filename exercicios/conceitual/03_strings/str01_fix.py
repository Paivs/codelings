# TITULO: Strings - Metodo Inexistente
# TIPO: fix
# ID: 006

# =================================================================
# ENUNCIADO
# =================================================================
# Um gerador de cartoes de visita formata nomes e textos, mas
# um dos metodos de string usados nao existe em Python.
#
# Corrija o nome do metodo para que o codigo funcione.
# =================================================================

frase = "python e uma linguagem incrivel"

frase_titulo    = frase.totitle()     # <- revise esta linha
frase_maiuscula = frase.upper()
frase_limpa     = "  ola mundo  ".strip()

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert frase_titulo    == "Python E Uma Linguagem Incrivel", "frase_titulo incorreto"
assert frase_maiuscula == "PYTHON E UMA LINGUAGEM INCRIVEL", "frase_maiuscula incorreto"
assert frase_limpa     == "ola mundo",                       "frase_limpa incorreto"
print(frase_titulo)
print(frase_maiuscula)
print(frase_limpa)
print("Exercicio concluido!")
