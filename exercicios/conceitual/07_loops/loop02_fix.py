# TITULO: Loops - Inicializacao Dentro do Loop
# TIPO: fix
# ID: 055

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema acumula a soma de uma lista de numeros, mas o resultado
# esta sempre igual ao ultimo elemento porque o acumulador e zerado
# a cada iteracao do loop.
# =================================================================

numeros = [3, 7, 2, 9, 1]
for n in numeros:
    total = 0       # <- revise esta linha
    total += n

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert total == 22, f"total deveria ser 22, mas e {total}"
print(f"numeros = {numeros}")
print(f"total   = {total}")
print("Exercicio concluido!")
