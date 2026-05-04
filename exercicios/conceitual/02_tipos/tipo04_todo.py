# TITULO: Tipos - Verificacao de Tipos
# TIPO: todo
# ID: 038

# =================================================================
# ENUNCIADO
# =================================================================
# Um validador de dados precisa confirmar se cada campo chegou com
# o tipo esperado antes de processar o registro.
#
# Campos recebidos:
#   codigo    -> 1042      (esperado: int)
#   descricao -> "Produto A" (esperado: str)
#   preco     -> 29.90     (esperado: float)
#   ativo     -> True      (esperado: bool)
#
# Resultados esperados:
#   codigo_ok    -> True
#   descricao_ok -> True
#   preco_ok     -> True
#   todos_ok     -> True (somente se todos os quatro campos estiverem corretos)
# =================================================================

codigo    = 1042
descricao = "Produto A"
preco     = 29.90
ativo     = True

# TAREFA: Verifique o tipo de cada campo e calcule 'todos_ok'.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert codigo_ok    is True,  "codigo_ok incorreto"
assert descricao_ok is True,  "descricao_ok incorreto"
assert preco_ok     is True,  "preco_ok incorreto"
assert todos_ok     is True,  "todos_ok incorreto"
assert isinstance(codigo_ok,    bool), "codigo_ok deve ser bool"
assert isinstance(descricao_ok, bool), "descricao_ok deve ser bool"
assert isinstance(preco_ok,     bool), "preco_ok deve ser bool"
assert isinstance(todos_ok,     bool), "todos_ok deve ser bool"
print(f"codigo_ok    = {codigo_ok}")
print(f"descricao_ok = {descricao_ok}")
print(f"preco_ok     = {preco_ok}")
print(f"todos_ok     = {todos_ok}")
print("Exercicio concluido!")
