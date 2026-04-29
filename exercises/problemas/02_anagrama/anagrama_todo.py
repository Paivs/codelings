# TITLE: Anagrama Valido - Implementar
# TYPE: todo
# DESCRIPTION: Implemente a funcao que verifica se dois textos sao anagramas.
# ID: 021

def eh_anagrama(a, b):
    """
    Retorna True se 'a' e 'b' sao anagramas entre si.
    Deve ignorar maiusculas/minusculas e espacos.

    eh_anagrama("listen", "silent")          -> True
    eh_anagrama("Listen", "Silent")          -> True
    eh_anagrama("Astronomer", "Moon starer") -> True
    eh_anagrama("hello", "world")            -> False
    """
    # TODO: Normalize as duas strings (minusculo, sem espacos) e compare.
    # Duas strings sao anagramas se, ordenadas, ficam iguais.
    pass


# --- Validacao (nao modifique abaixo) ---
assert eh_anagrama("listen", "silent")          is True
assert eh_anagrama("Listen", "Silent")          is True
assert eh_anagrama("Astronomer", "Moon starer") is True
assert eh_anagrama("hello", "world")            is False
assert eh_anagrama("abc", "cba")                is True
assert eh_anagrama("abc", "abcd")               is False
print(f"listen / silent          -> {eh_anagrama('listen', 'silent')}")
print(f"Listen / Silent          -> {eh_anagrama('Listen', 'Silent')}")
print(f"Astronomer / Moon starer -> {eh_anagrama('Astronomer', 'Moon starer')}")
print(f"hello / world            -> {eh_anagrama('hello', 'world')}")
print("Exercicio concluido!")
