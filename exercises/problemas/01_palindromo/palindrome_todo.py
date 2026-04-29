# TITLE: Palindromo - Implementar
# TYPE: todo
# DESCRIPTION: Implemente a funcao que verifica se um texto e um palindromo.
# ID: 019

def eh_palindromo(texto):
    """
    Retorna True se 'texto' e um palindromo.
    Deve ignorar maiusculas/minusculas e espacos.

    eh_palindromo("radar")                       -> True
    eh_palindromo("python")                      -> False
    """
    # TODO: Normalize o texto (minusculo, sem espacos) e compare com o reverso.
    
    invertido = ""
    
    for i in range(len(texto) - 1, -1, -1):
        invertido = invertido + texto[i]
    
    print(invertido)
        
    
    return invertido == texto.replace(" ", "").strip().lower()
    
    


# --- Validacao (nao modifique abaixo) ---
assert eh_palindromo("radar")  is True,  "radar e palindromo"
assert eh_palindromo("arara")  is True,  "arara e palindromo"
assert eh_palindromo("python") is False, "python nao e palindromo"
assert eh_palindromo("a")      is True,  "letra unica e palindromo"
assert eh_palindromo("")       is True,  "string vazia e palindromo"
print(f"radar   -> {eh_palindromo('radar')}")
print(f"python  -> {eh_palindromo('python')}")
print(f"A man a plan a canal Panama -> {eh_palindromo('A man a plan a canal Panama')}")
print("Exercicio concluido!")
