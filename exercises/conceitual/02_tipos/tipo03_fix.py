# TITULO: Tipos - Divisao Retorna Zero
# TIPO: fix
# ID: 036

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema calcula a media de itens, mas o resultado esta errado
# porque a operacao de divisao descarta a parte decimal.
# =================================================================

total  = 7
itens  = 2
media  = total // itens    # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert media == 3.5, f"media deveria ser 3.5, mas e {media}"
print(f"total = {total}")
print(f"itens = {itens}")
print(f"media = {media}")
print("Exercicio concluido!")
