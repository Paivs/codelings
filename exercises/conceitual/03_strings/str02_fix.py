# TITULO: Strings - Fatiamento Incorreto
# TIPO: fix
# ID: 039

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema extrai os tres primeiros caracteres de um codigo para
# usar como prefixo de identificacao, mas o fatiamento esta pegando
# a parte errada da string.
# =================================================================

codigo   = "ABC123"
prefixo  = codigo[3:]    # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert prefixo == "ABC", f"prefixo deveria ser 'ABC', mas e {prefixo!r}"
print(f"codigo  = {codigo!r}")
print(f"prefixo = {prefixo!r}")
print("Exercicio concluido!")
