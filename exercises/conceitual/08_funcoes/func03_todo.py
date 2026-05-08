# TITULO: Funcoes - Conversor de Unidades
# TIPO: todo
# ID: 061

# =================================================================
# ENUNCIADO
# =================================================================
# Uma aplicacao de fisica precisa converter valores entre diferentes
# sistemas de medida.
#
# Conversoes e exemplos:
#   km_para_milhas(1)       -> ~0.621371
#   celsius_para_fahrenheit(0)   -> 32.0
#   celsius_para_fahrenheit(100) -> 212.0
#   kg_para_libras(1)       -> ~2.20462
# =================================================================

# TAREFA: Implemente as tres funcoes de conversao.

def km_para_milhas(km):
    pass

def celsius_para_fahrenheit(c):
    pass

def kg_para_libras(kg):
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert abs(km_para_milhas(1)            - 0.621371) < 0.0001, "km_para_milhas incorreto"
assert celsius_para_fahrenheit(0)       == 32.0,               "celsius_para_fahrenheit(0) incorreto"
assert celsius_para_fahrenheit(100)     == 212.0,              "celsius_para_fahrenheit(100) incorreto"
assert abs(kg_para_libras(1)            - 2.20462)  < 0.0001,  "kg_para_libras incorreto"
print(f"1 km       = {km_para_milhas(1):.6f} milhas")
print(f"0 C        = {celsius_para_fahrenheit(0)} F")
print(f"100 C      = {celsius_para_fahrenheit(100)} F")
print(f"1 kg       = {kg_para_libras(1):.5f} libras")
print("Exercicio concluido!")
