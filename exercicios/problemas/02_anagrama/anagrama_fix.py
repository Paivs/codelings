# TITULO: Anagrama Valido - Bug na Normalizacao
# TIPO: fix
# ID: 020

# =================================================================
# ENUNCIADO
# =================================================================
# Um verificador de anagramas compara duas strings, mas nao
# normaliza o texto antes da comparacao, causando falsos negativos
# quando ha maiusculas ou espacos.
#
# Corrija a funcao para que ela ignore maiusculas e espacos.
# =================================================================

def eh_anagrama(a, b):
    return sorted(a) == sorted(b)   # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert eh_anagrama("listen", "silent")          is True,  "caso 1 incorreto"
assert eh_anagrama("Listen", "Silent")          is True,  "deve ignorar maiusculas"
assert eh_anagrama("Astronomer", "Moon starer") is True,  "deve ignorar espacos"
assert eh_anagrama("hello", "world")            is False, "nao sao anagramas"
print(f"listen / silent          -> {eh_anagrama('listen', 'silent')}")
print(f"Listen / Silent          -> {eh_anagrama('Listen', 'Silent')}")
print(f"Astronomer / Moon starer -> {eh_anagrama('Astronomer', 'Moon starer')}")
print("Exercicio concluido!")
