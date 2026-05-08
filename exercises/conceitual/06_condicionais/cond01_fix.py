# TITULO: Condicionais - Classificacao de Notas
# TIPO: fix
# ID: 012

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema escolar classifica notas em categorias. A funcao esta
# quase correta, mas um operador de comparacao esta errado,
# fazendo com que notas na fronteira sejam mal classificadas.
#
# Regras de negocio:
#   >= 9 -> "Excelente" | >= 7 -> "Bom"
#   >= 5 -> "Regular"   | >= 0 -> "Insuficiente" | fora -> "Invalida"
# =================================================================

def classificar_nota(nota):
    if nota > 10 or nota < 0:
        return "Invalida"
    if nota >= 9:
        return "Excelente"
    if nota >= 7:
        return "Bom"
    if nota > 5:              # <- revise esta linha
        return "Regular"
    return "Insuficiente"

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert classificar_nota(10) == "Excelente",    "nota 10 incorreta"
assert classificar_nota(9)  == "Excelente",    "nota 9 incorreta"
assert classificar_nota(8)  == "Bom",          "nota 8 incorreta"
assert classificar_nota(7)  == "Bom",          "nota 7 incorreta"
assert classificar_nota(6)  == "Regular",      "nota 6 incorreta"
assert classificar_nota(5)  == "Regular",      "nota 5 incorreta"
assert classificar_nota(4)  == "Insuficiente", "nota 4 incorreta"
assert classificar_nota(-1) == "Invalida",     "nota -1 incorreta"
assert classificar_nota(11) == "Invalida",     "nota 11 incorreta"
for n in [10, 9, 7, 5, 4, -1]:
    print(f"  nota {n:>2} -> {classificar_nota(n)}")
print("Exercicio concluido!")
