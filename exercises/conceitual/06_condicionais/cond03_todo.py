# TITULO: Condicionais - Calculo de Frete
# TIPO: todo
# ID: 053

# =================================================================
# ENUNCIADO
# =================================================================
# Uma loja online calcula o frete com base no peso e na distancia
# do pedido.
#
# Regras:
#   peso <= 5  e distancia <= 100  ->  frete = 15.00
#   peso <= 5  e distancia > 100   ->  frete = 25.00
#   peso > 5   e distancia <= 100  ->  frete = 35.00
#   peso > 5   e distancia > 100   ->  frete = 50.00
#
# Para peso=3.0 e distancia=150, o frete esperado e 25.00.
# =================================================================

peso      = 3.0
distancia = 150

# TAREFA: Calcule 'frete' aplicando as quatro regras de negocio.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert frete == 25.0, f"frete incorreto para peso=3.0, distancia=150: {frete}"
print(f"peso      = {peso}")
print(f"distancia = {distancia}")
print(f"frete     = R$ {frete:.2f}")
print("Exercicio concluido!")
