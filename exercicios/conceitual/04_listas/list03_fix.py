# TITULO: Listas - Copia por Referencia
# TIPO: fix
# ID: 044

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema cria uma "copia" de uma lista para modifica-la de
# forma independente, mas na verdade as duas variaveis apontam
# para o mesmo objeto — qualquer alteracao em uma afeta a outra.
# =================================================================

original = [10, 20, 30]
copia    = original        # <- revise esta linha
copia.append(40)

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert original == [10, 20, 30],       f"original nao deveria ter sido alterado: {original}"
assert copia    == [10, 20, 30, 40],   f"copia incorreta: {copia}"
print(f"original = {original}")
print(f"copia    = {copia}")
print("Exercicio concluido!")
