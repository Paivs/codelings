# TITULO: Variaveis - Calculadora de Gorjeta
# TIPO: todo
# ID: 034

# =================================================================
# ENUNCIADO
# =================================================================
# Um restaurante precisa calcular automaticamente o valor da gorjeta
# e o total da conta para o cliente.
#
# Dados de entrada:
#   conta             -> 85.50
#   percentual_gorjeta -> 10
#
# Resultados esperados:
#   gorjeta -> 8.55   (valor da gorjeta)
#   total   -> 94.05  (conta + gorjeta)
# =================================================================

conta              = 85.50
percentual_gorjeta = 10

# TAREFA: Calcule 'gorjeta' e 'total' a partir das variaveis fornecidas.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert abs(gorjeta - 8.55)  < 0.01, f"gorjeta incorreta: {gorjeta}"
assert abs(total   - 94.05) < 0.01, f"total incorreto: {total}"
print(f"Conta   : R$ {conta:.2f}")
print(f"Gorjeta : R$ {gorjeta:.2f}")
print(f"Total   : R$ {total:.2f}")
print("Exercicio concluido!")
