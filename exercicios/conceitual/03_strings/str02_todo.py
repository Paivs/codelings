# TITULO: Strings - Processamento de Texto
# TIPO: todo
# ID: 007

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de busca precisa processar uma frase para indexacao.
#
# Texto de entrada:
#   "a raposa marrom pula sobre o cao preguicoso"
#
# Resultados esperados:
#   texto_maiusculo     -> frase toda em maiusculas
#   palavras            -> lista com cada palavra separada
#   quantidade_palavras -> numero total de palavras (8)
#   novo_texto          -> frase com "cao" substituido por "gato"
# =================================================================

texto = "a raposa marrom pula sobre o cao preguicoso"

# TAREFA: Crie as quatro variaveis aplicando as transformacoes sobre 'texto'.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert texto_maiusculo    == "A RAPOSA MARROM PULA SOBRE O CAO PREGUICOSO", "texto_maiusculo incorreto"
assert isinstance(palavras, list),                                            "palavras deve ser uma lista"
assert quantidade_palavras == 8,                                              "quantidade de palavras incorreta"
assert novo_texto          == "a raposa marrom pula sobre o gato preguicoso", "novo_texto incorreto"
print(f"Maiusculo : {texto_maiusculo}")
print(f"Palavras  : {palavras}")
print(f"Quantidade: {quantidade_palavras}")
print(f"Novo texto: {novo_texto}")
print("Exercicio concluido!")
