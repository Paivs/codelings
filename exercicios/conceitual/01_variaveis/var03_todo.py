# TITULO: Variaveis - Sistema de Pedidos
# TIPO: todo
# ID: 003

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de pedidos precisa registrar as informacoes de uma
# compra para calcular o valor total.
#
# Variaveis necessarias:
#   produto    -> "Caderno"  (str)
#   preco      -> 12.50      (float, valor unitario em reais)
#   quantidade -> 3          (int)
# =================================================================

# TAREFA: Crie as tres variaveis acima com os valores e tipos corretos.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert produto    == "Caderno", "produto incorreto"
assert preco      == 12.50,     "preco incorreto"
assert quantidade == 3,         "quantidade incorreta"
assert isinstance(preco,      float), "preco deve ser float"
assert isinstance(quantidade, int),   "quantidade deve ser int"
total = preco * quantidade
print(f"Produto   : {produto}")
print(f"Preco     : R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total     : R$ {total:.2f}")
print("Exercicio concluido!")
