# TITULO: Funcoes - Retorno Incorreto
# TIPO: fix
# ID: 059

# =================================================================
# ENUNCIADO
# =================================================================
# Uma funcao calcula o valor absoluto de um numero, mas retorna
# um valor negativo quando o numero e positivo ou zero.
# =================================================================

def valor_absoluto(n):
    if n < 0:
        return -n
    return -n    # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert valor_absoluto(5)  == 5, f"valor_absoluto(5) deveria ser 5, mas e {valor_absoluto(5)}"
assert valor_absoluto(-3) == 3, f"valor_absoluto(-3) deveria ser 3, mas e {valor_absoluto(-3)}"
assert valor_absoluto(0)  == 0, f"valor_absoluto(0) deveria ser 0, mas e {valor_absoluto(0)}"
print(f"valor_absoluto(5)  = {valor_absoluto(5)}")
print(f"valor_absoluto(-3) = {valor_absoluto(-3)}")
print(f"valor_absoluto(0)  = {valor_absoluto(0)}")
print("Exercicio concluido!")
