# TITLE: Dicionarios - Criando e Manipulando
# TYPE: todo
# DESCRIPTION: Manipule o dicionario de estoque conforme os TODO abaixo.
# ID: 011

estoque = {
    "maca": 10,
    "banana": 5,
    "laranja": 8,
}

# TODO: Adicione "uva" com quantidade 15

# TODO: Atualize a quantidade de "banana" para 12

# TODO: Remova "laranja" do dicionario

# TODO: Armazene em 'total_itens' a soma de todos os valores do estoque


# --- Validacao (nao modifique abaixo) ---
assert "uva" in estoque, "'uva' deveria estar no estoque"
assert estoque["uva"] == 15, f"'uva' deveria ter 15, mas tem {estoque.get('uva')}"
assert estoque["banana"] == 12, f"'banana' deveria ter 12, mas tem {estoque.get('banana')}"
assert "laranja" not in estoque, "'laranja' nao deveria mais estar no estoque"
assert total_itens == sum(estoque.values()), \
    f"'total_itens' deveria ser {sum(estoque.values())}, mas e {total_itens}"
print(f"Estoque      : {estoque}")
print(f"Total itens  : {total_itens}")
print("Exercicio concluido!")
