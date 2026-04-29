# TITULO: Anagrama Valido - Implementar
# TIPO: todo
# ID: 021

# =================================================================
# ENUNCIADO
# =================================================================
# Dois textos sao anagramas quando contem exatamente as mesmas
# letras, em qualquer ordem.
#
# Exemplos:
#   eh_anagrama("listen", "silent")          -> True
#   eh_anagrama("Astronomer", "Moon starer") -> True
#   eh_anagrama("hello", "world")            -> False
#
# Regras de negocio:
#   - Ignorar maiusculas e minusculas
#   - Ignorar espacos
#   - Strings com quantidades diferentes de letras nunca sao anagramas
# =================================================================

def eh_anagrama(a, b):
    # TAREFA: Normalize as duas strings (minusculo, sem espacos) e
    # compare-as ordenadas. Dois textos sao anagramas se, apos a
    # normalizacao, sorted(a) == sorted(b).
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert eh_anagrama("listen", "silent")          is True,  "caso 1 incorreto"
assert eh_anagrama("Listen", "Silent")          is True,  "caso 2 incorreto"
assert eh_anagrama("Astronomer", "Moon starer") is True,  "caso 3 incorreto"
assert eh_anagrama("hello", "world")            is False, "caso 4 incorreto"
assert eh_anagrama("abc", "cba")                is True,  "caso 5 incorreto"
assert eh_anagrama("abc", "abcd")               is False, "caso 6 incorreto"
print(f"listen / silent          -> {eh_anagrama('listen', 'silent')}")
print(f"Astronomer / Moon starer -> {eh_anagrama('Astronomer', 'Moon starer')}")
print(f"hello / world            -> {eh_anagrama('hello', 'world')}")
print("Exercicio concluido!")
