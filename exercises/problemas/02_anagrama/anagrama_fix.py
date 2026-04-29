# TITLE: Anagrama Valido - Bug na Normalizacao
# TYPE: fix
# DESCRIPTION: A funcao detecta anagramas mas ignora maiusculas e espacos incorretamente.
# ID: 020

def eh_anagrama(a, b):
    """Retorna True se 'a' e 'b' sao anagramas (ignora maiusculas e espacos)."""
    return sorted(a) == sorted(b)   # BUG: compara sem normalizar


assert eh_anagrama("listen", "silent")       is True,  "listen/silent sao anagramas"
assert eh_anagrama("Listen", "Silent")       is True,  "deve ignorar maiusculas"
assert eh_anagrama("Astronomer", "Moon starer") is True, "deve ignorar espacos"
assert eh_anagrama("hello", "world")         is False, "hello/world nao sao anagramas"
print(f"listen / silent       -> {eh_anagrama('listen', 'silent')}")
print(f"Listen / Silent       -> {eh_anagrama('Listen', 'Silent')}")
print(f"Astronomer / Moon starer -> {eh_anagrama('Astronomer', 'Moon starer')}")
print("Exercicio concluido!")
