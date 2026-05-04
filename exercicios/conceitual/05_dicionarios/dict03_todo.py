# TITULO: Dicionarios - Contagem de Frequencia
# TIPO: todo
# ID: 049

# =================================================================
# ENUNCIADO
# =================================================================
# Um analisador de texto precisa contar quantas vezes cada palavra
# aparece em uma frase.
#
# Frase: "o gato comeu o peixe do gato velho"
#
# Resultados esperados:
#   palavras  -> ["o", "gato", "comeu", "o", "peixe", "do", "gato", "velho"]
#   contagem  -> {"o": 2, "gato": 2, "comeu": 1, "peixe": 1, "do": 1, "velho": 1}
# =================================================================

frase = "o gato comeu o peixe do gato velho"

# TAREFA: Crie a lista 'palavras' e o dicionario 'contagem' com a frequencia de cada palavra.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert isinstance(palavras, list),        "palavras deve ser uma lista"
assert isinstance(contagem, dict),        "contagem deve ser um dicionario"
assert contagem["o"]     == 2,            "contagem de 'o' incorreta"
assert contagem["gato"]  == 2,            "contagem de 'gato' incorreta"
assert contagem["comeu"] == 1,            "contagem de 'comeu' incorreta"
assert len(contagem)     == 6,            f"contagem deveria ter 6 chaves, mas tem {len(contagem)}"
print(f"palavras = {palavras}")
print(f"contagem = {contagem}")
print("Exercicio concluido!")
