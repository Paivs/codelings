# TITULO: Palindromo - Bug na Inversao
# TIPO: fix
# ID: 018

# =================================================================
# ENUNCIADO
# =================================================================
# Um verificador de palindromos foi implementado, mas ha um bug
# na operacao que inverte a string para comparacao.
#
# Corrija a operacao de inversao da string.
# =================================================================

def eh_palindromo(texto):
    limpo = texto.lower().replace(" ", "")
    return limpo == limpo[1:]   # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert eh_palindromo("radar")  is True,  "radar deveria ser palindromo"
assert eh_palindromo("arara")  is True,  "arara deveria ser palindromo"
assert eh_palindromo("python") is False, "python nao e palindromo"
assert eh_palindromo("A man a plan a canal Panama") is True, "frase palindromo incorreta"
print(f"radar  -> {eh_palindromo('radar')}")
print(f"arara  -> {eh_palindromo('arara')}")
print(f"python -> {eh_palindromo('python')}")
print("Exercicio concluido!")
