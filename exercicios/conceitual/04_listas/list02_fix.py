# TITULO: Listas - Remocao por Valor vs Indice
# TIPO: fix
# ID: 043

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema remove o primeiro elemento de uma fila por posicao,
# mas usa um metodo que busca por valor em vez de por indice.
# Como o valor 0 nao existe na lista, o programa lanca um erro.
# =================================================================

fila = ["Carlos", "Ana", "Bruno", "Diana"]
fila.remove(0)    # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert fila == ["Ana", "Bruno", "Diana"], f"fila incorreta: {fila}"
assert len(fila) == 3,                    f"tamanho incorreto: {len(fila)}"
print(f"fila = {fila}")
print("Exercicio concluido!")
