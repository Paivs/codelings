# TITULO: Variaveis - Ficha de Produto
# TIPO: todo
# ID: 033

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de cadastro precisa registrar as informacoes de um
# produto em variaveis com os tipos e valores corretos.
#
# Dados do produto:
#   nome      -> "Teclado Mecanico"  (str)
#   preco     -> 349.90              (float)
#   estoque   -> 15                  (int)
#   disponivel -> True se estoque > 0, False caso contrario (bool)
# =================================================================

# TAREFA: Crie as quatro variaveis com os valores e tipos indicados.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert nome       == "Teclado Mecanico", "nome incorreto"
assert preco      == 349.90,             "preco incorreto"
assert estoque    == 15,                 "estoque incorreto"
assert disponivel is True,               "disponivel incorreto"
assert isinstance(nome,       str),   "nome deve ser str"
assert isinstance(preco,      float), "preco deve ser float"
assert isinstance(estoque,    int),   "estoque deve ser int"
assert isinstance(disponivel, bool),  "disponivel deve ser bool"
print(f"Produto  : {nome}")
print(f"Preco    : R$ {preco:.2f}")
print(f"Estoque  : {estoque} unidades")
print(f"Disponivel: {disponivel}")
print("Exercicio concluido!")
