# TITULO: Tipos - Formulario de Cadastro
# TIPO: todo
# ID: 037

# =================================================================
# ENUNCIADO
# =================================================================
# Um formulario web recebe todos os valores como texto e precisa
# converte-los para os tipos corretos antes de salvar no banco.
#
# Valores recebidos:
#   nome_raw   -> "Alice"
#   idade_raw  -> "28"
#   altura_raw -> "1.65"
#   ativo_raw  -> "1"
#
# Conversoes necessarias:
#   nome   -> str  (mesmo valor de nome_raw)
#   idade  -> int
#   altura -> float
#   ativo  -> bool (converta para int antes de converter para bool)
# =================================================================

nome_raw    = "Alice"
idade_raw   = "28"
altura_raw  = "1.65"
ativo_raw   = "1"

# TAREFA: Converta cada variavel _raw para o tipo correto.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert nome   == "Alice",    "nome incorreto"
assert idade  == 28,         "idade incorreta"
assert altura == 1.65,       "altura incorreta"
assert ativo  is True,       "ativo incorreto"
assert isinstance(nome,   str),   "nome deve ser str"
assert isinstance(idade,  int),   "idade deve ser int"
assert isinstance(altura, float), "altura deve ser float"
assert isinstance(ativo,  bool),  "ativo deve ser bool"
print(f"nome   = {nome!r}")
print(f"idade  = {idade!r}")
print(f"altura = {altura!r}")
print(f"ativo  = {ativo!r}")
print("Exercicio concluido!")
