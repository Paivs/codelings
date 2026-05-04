# TITULO: Tipos - Conversao Entre Tipos
# TIPO: todo
# ID: 005

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de processamento de dados recebe valores em formatos
# variados e precisa converte-los para os tipos corretos.
#
# Conversoes necessarias:
#   "42"  ->  42      (int)
#   7     ->  7.0     (float)
#   0     ->  False   (bool)
#   99    ->  "99"    (str)
# =================================================================

# TAREFA: Crie as quatro variaveis abaixo com as conversoes corretas.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert numero_inteiro == 42,    "numero_inteiro incorreto"
assert numero_float   == 7.0,   "numero_float incorreto"
assert valor_falso    is False, "valor_falso incorreto"
assert numero_texto   == "99",  "numero_texto incorreto"
assert isinstance(numero_inteiro, int),   "numero_inteiro deve ser int"
assert isinstance(numero_float,   float), "numero_float deve ser float"
assert isinstance(valor_falso,    bool),  "valor_falso deve ser bool"
assert isinstance(numero_texto,   str),   "numero_texto deve ser str"
print(f"int  : {numero_inteiro!r}")
print(f"float: {numero_float!r}")
print(f"bool : {valor_falso!r}")
print(f"str  : {numero_texto!r}")
print("Exercicio concluido!")
