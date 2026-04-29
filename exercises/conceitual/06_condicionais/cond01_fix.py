# TITLE: Condicionais - Operador Errado
# TYPE: fix
# DESCRIPTION: A funcao classifica notas mas um operador de comparacao esta errado.
# ID: 012

def classificar_nota(nota):
    if nota > 10 or nota < 0:
        return "Invalida"
    if nota >= 9:
        return "Excelente"
    if nota >= 7:
        return "Bom"
    if nota > 5:        # BUG aqui
        return "Regular"
    return "Insuficiente"


# --- Validacao (nao modifique abaixo) ---
casos = [
    (10, "Excelente"),
    (9,  "Excelente"),
    (8,  "Bom"),
    (7,  "Bom"),
    (6,  "Regular"),
    (5,  "Regular"),   # este e o caso que falha com o bug
    (4,  "Insuficiente"),
    (0,  "Insuficiente"),
    (-1, "Invalida"),
    (11, "Invalida"),
]
for nota, esperado in casos:
    resultado = classificar_nota(nota)
    assert resultado == esperado, \
        f"classificar_nota({nota}): esperado '{esperado}', obtido '{resultado}'"
    print(f"  nota {nota:>2} -> {resultado}")
print("Exercicio concluido!")
