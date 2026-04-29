# TITLE: Strings - Manipulacao de Texto
# TYPE: todo
# DESCRIPTION: Manipule a string 'texto' conforme os TODO abaixo.
# ID: 007

texto = "a raposa marrom pula sobre o cao preguicoso"

# TODO: Armazene em 'texto_maiusculo' o texto todo em letras maiusculas

# TODO: Armazene em 'palavras' uma lista com todas as palavras do texto
#       (use o metodo .split())

# TODO: Armazene em 'quantidade_palavras' o numero de palavras na lista

# TODO: Armazene em 'novo_texto' o texto com "cao" substituido por "gato"


# --- Validacao (nao modifique abaixo) ---
assert texto_maiusculo == texto.upper(), "texto_maiusculo incorreto"
assert isinstance(palavras, list), "'palavras' deveria ser uma lista"
assert quantidade_palavras == 8, f"Esperado 8 palavras, obtido {quantidade_palavras}"
assert "gato" in novo_texto, "'novo_texto' deveria conter 'gato'"
assert "cao" not in novo_texto, "'novo_texto' nao deveria mais conter 'cao'"
print(f"Original   : {texto}")
print(f"Maiusculo  : {texto_maiusculo}")
print(f"Palavras   : {palavras}")
print(f"Quantidade : {quantidade_palavras}")
print(f"Novo texto : {novo_texto}")
print("Exercicio concluido!")
