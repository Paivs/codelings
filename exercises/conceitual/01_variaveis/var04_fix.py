# TITULO: Variaveis - Troca de Valores
# TIPO: fix
# ID: 032

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema precisa trocar os valores de duas variaveis entre si,
# mas a logica de troca esta errada — a variavel temporaria recebe
# o valor incorreto, fazendo as duas variaveis ficarem com o mesmo
# valor apos a operacao.
# =================================================================

a = 100
b = 200
temp = b       # <- revise esta linha
a = b
b = temp

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert a == 200, f"a deveria ser 200, mas e {a}"
assert b == 100, f"b deveria ser 100, mas e {b}"
print(f"a = {a}")
print(f"b = {b}")
print("Exercicio concluido!")
