# TITLE: Palindromo - Bug na Inversao
# TYPE: fix
# DESCRIPTION: A funcao que verifica palindromos tem um bug na inversao da string.
# ID: 018

def eh_palindromo(texto):
    """Retorna True se o texto e um palindromo (ignora maiusculas e espacos)."""
    limpo = texto.lower().replace(" ", "")
    return limpo == limpo[1:]   # BUG: [1:] remove o primeiro caractere, nao inverte


assert eh_palindromo("radar")  is True,  "radar e palindromo"
assert eh_palindromo("arara")  is True,  "arara e palindromo"
assert eh_palindromo("python") is False, "python nao e palindromo"
assert eh_palindromo("A man a plan a canal Panama") is True, "frase palindromo"
print(f"radar  -> {eh_palindromo('radar')}")
print(f"arara  -> {eh_palindromo('arara')}")
print(f"python -> {eh_palindromo('python')}")
print("Exercicio concluido!")
