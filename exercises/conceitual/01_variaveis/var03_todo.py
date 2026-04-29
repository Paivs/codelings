# TITLE: Variaveis - Atribuicao Basica
# TYPE: todo
# DESCRIPTION: Crie as variaveis conforme os comentarios TODO para a validacao passar.
# ID: 003

# TODO: Crie uma variavel 'produto' com o valor "Caderno" (string)

# TODO: Crie uma variavel 'preco' com o valor 12.50 (float)

# TODO: Crie uma variavel 'quantidade' com o valor 3 (inteiro)


# --- Validacao (nao modifique abaixo) ---
assert produto == "Caderno", f"'produto' deveria ser 'Caderno', mas e '{produto}'"
assert preco == 12.50, f"'preco' deveria ser 12.50, mas e {preco}"
assert isinstance(preco, float), f"'preco' deveria ser float, mas e {type(preco).__name__}"
assert quantidade == 3, f"'quantidade' deveria ser 3, mas e {quantidade}"
assert isinstance(quantidade, int), f"'quantidade' deveria ser int, mas e {type(quantidade).__name__}"
total = preco * quantidade
print(f"Produto   : {produto}")
print(f"Preco     : R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total     : R$ {total:.2f}")
print("Exercicio concluido!")
