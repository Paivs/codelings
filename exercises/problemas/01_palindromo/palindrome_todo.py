# TITULO: Palindromo - Implementar
# TIPO: todo
# ID: 019

# =================================================================
# ENUNCIADO
# =================================================================
# Um verificador de textos precisa identificar palindromos — palavras
# ou frases que se leem da mesma forma de tras para frente.
#
# Exemplos:
#   eh_palindromo("radar")                       -> True
#   eh_palindromo("python")                      -> False
#   eh_palindromo("A man a plan a canal Panama") -> True
#
# Regras de negocio:
#   - Ignorar maiusculas e minusculas
#   - Ignorar espacos
#   - String vazia e considerada palindromo
# =================================================================

def eh_palindromo(texto):
    # TAREFA: Normalize o texto (minusculo, sem espacos) e verifique
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert eh_palindromo("radar")  is True,  "radar deve ser palindromo"
assert eh_palindromo("arara")  is True,  "arara deve ser palindromo"
assert eh_palindromo("python") is False, "python nao e palindromo"
assert eh_palindromo("A man a plan a canal Panama") is True, "frase palindromo incorreta"
assert eh_palindromo("")       is True,  "string vazia deve ser palindromo"
print(f"radar   -> {eh_palindromo('radar')}")
print(f"python  -> {eh_palindromo('python')}")
print(f"A man a plan... -> {eh_palindromo('A man a plan a canal Panama')}")
print("Exercicio concluido!")
