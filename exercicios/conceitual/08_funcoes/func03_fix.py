# TITULO: Funcoes - Argumentos Trocados
# TIPO: fix
# ID: 060

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema calcula o preco com desconto, mas os argumentos foram
# passados na ordem errada na chamada da funcao — o percentual foi
# passado como preco e vice-versa, gerando um resultado incorreto.
# =================================================================

def calcular_desconto(preco, percentual):
    return preco * (1 - percentual / 100)

resultado = calcular_desconto(20, 100.0)    # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert abs(resultado - 80.0) < 0.01, f"resultado deveria ser 80.0, mas e {resultado}"
print(f"resultado = R$ {resultado:.2f}")
print("Exercicio concluido!")
