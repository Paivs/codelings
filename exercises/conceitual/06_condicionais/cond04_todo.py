# TITULO: Condicionais - Conceito por Nota
# TIPO: todo
# ID: 054

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema escolar converte notas numericas em conceitos de A a D.
#
# Regras:
#   nota >= 9.0  ->  "A"
#   nota >= 7.0  ->  "B"
#   nota >= 5.0  ->  "C"
#   nota < 5.0   ->  "D"
#
# Para nota=7.5, o conceito esperado e "B".
# =================================================================

nota = 7.5

# TAREFA: Determine o 'conceito' correspondente a 'nota' usando as quatro regras.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert conceito == "B", f"conceito incorreto para nota=7.5: {conceito!r}"
print(f"nota    = {nota}")
print(f"conceito = {conceito!r}")
print("Exercicio concluido!")
