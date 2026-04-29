# TITLE: Strings - Metodo Inexistente
# TYPE: fix
# DESCRIPTION: O codigo usa um metodo de string que nao existe em Python.
# ID: 006

frase = "python e uma linguagem incrivel"

frase_titulo = frase.istitle()
frase_maiuscula = frase.upper()
frase_limpa = "  ola mundo  ".strip()

print(frase_titulo)
print(frase_maiuscula)
print(frase_limpa)
