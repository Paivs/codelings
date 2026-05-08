# TITULO: Dicionarios - Gestao de Estoque
# TIPO: todo
# ID: 011

# =================================================================
# ENUNCIADO
# =================================================================
# Um mercado gerencia o estoque de frutas em um dicionario.
# Realize as operacoes necessarias para atualizar o estoque.
#
# Estoque inicial: {"maca": 10, "banana": 5, "laranja": 8}
#
# Operacoes (nesta ordem):
#   1. Adicionar "uva" com quantidade 15
#   2. Atualizar "banana" para quantidade 12
#   3. Remover "laranja" do estoque
#   4. Somar todos os valores -> guardar em 'total_itens'
# =================================================================

estoque = {
    "maca"  : 10,
    "banana": 5,
    "laranja": 8,
}

# TAREFA: Execute as quatro operacoes acima sobre o dicionario 'estoque'.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert "uva"     in estoque,         "uva deve estar no estoque"
assert "laranja" not in estoque,     "laranja deve ter sido removida"
assert estoque.get("uva")    == 15,  "quantidade de uva incorreta"
assert estoque.get("banana") == 12,  "quantidade de banana incorreta"
assert total_itens           == 37,  "total de itens incorreto"
print(f"Estoque    : {estoque}")
print(f"Total itens: {total_itens}")
print("Exercicio concluido!")
