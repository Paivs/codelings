# TITULO: Condicionais - Elif Ausente
# TIPO: fix
# ID: 052

# =================================================================
# ENUNCIADO
# =================================================================
# Um classificador de velocidade retorna o resultado errado para
# valores baixos. Quando a velocidade e menor que 60, o sistema
# deveria retornar "lento", mas acaba retornando "moderado" porque
# todas as condicoes sao avaliadas independentemente.
# =================================================================

def classificar(v):
    resultado = ""
    if v < 60:
        resultado = "lento"
    if v < 120:        # <- revise esta linha
        resultado = "moderado"
    if v >= 120:
        resultado = "rapido"
    return resultado

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert classificar(30)  == "lento",    f"classificar(30) deveria ser 'lento', mas e {classificar(30)!r}"
assert classificar(80)  == "moderado", f"classificar(80) deveria ser 'moderado', mas e {classificar(80)!r}"
assert classificar(150) == "rapido",   f"classificar(150) deveria ser 'rapido', mas e {classificar(150)!r}"
print(f"classificar(30)  = {classificar(30)!r}")
print(f"classificar(80)  = {classificar(80)!r}")
print(f"classificar(150) = {classificar(150)!r}")
print("Exercicio concluido!")
