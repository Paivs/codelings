# TITULO: Prefixo Comum
# TIPO: todo
# ID: 019

# =================================================================
# ENUNCIADO
# =================================================================
# Dado uma lista de strings, encontre o maior prefixo comum entre
# todas elas.
#
# Exemplos:
#   prefixo_comum(["flor", "floco", "fluido"]) -> "fl"
#   prefixo_comum(["carro", "carrossel", "carrinho"]) -> "carro"
#   prefixo_comum(["abc", "xyz"]) -> ""
#   prefixo_comum([]) -> ""
# =================================================================

def prefixo_comum(strings):
    # TAREFA: Implemente a funcao para encontrar o maior prefixo comum.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert prefixo_comum(["flor", "floco", "fluido"])         == "fl",     "prefixo 'fl' incorreto"
assert prefixo_comum(["carro", "carrossel", "carrinho"])  == "carro",  "prefixo 'carro' incorreto"
assert prefixo_comum(["abc", "xyz"])                      == "",       "sem prefixo comum"
assert prefixo_comum([])                                  == "",       "lista vazia deve retornar ''"
assert prefixo_comum(["python"])                          == "python", "unico elemento"
print("Exercicio concluido!")
