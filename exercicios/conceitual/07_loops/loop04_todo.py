# TITULO: Loops - Estatisticas de Temperatura
# TIPO: todo
# ID: 058

# =================================================================
# ENUNCIADO
# =================================================================
# Uma estacao meteorologica precisa calcular estatisticas das
# temperaturas registradas ao longo do dia usando loops,
# sem recorrer as funcoes prontas max(), min() ou sum().
#
# Temperaturas: [22.5, 18.0, 31.2, 25.8, 15.3, 29.1]
#
# Resultados esperados:
#   maior      -> 31.2
#   menor      -> 15.3
#   soma_total -> 141.9
#   media      -> 23.65
# =================================================================

temperaturas = [22.5, 18.0, 31.2, 25.8, 15.3, 29.1]

# TAREFA: Calcule 'maior', 'menor', 'soma_total' e 'media' usando loops.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert maior == 31.2,                       f"maior incorreto: {maior}"
assert menor == 15.3,                       f"menor incorreto: {menor}"
assert abs(soma_total - 141.9) < 0.01,      f"soma_total incorreta: {soma_total}"
assert abs(media - 23.65)      < 0.01,      f"media incorreta: {media}"
print(f"maior      = {maior}")
print(f"menor      = {menor}")
print(f"soma_total = {soma_total}")
print(f"media      = {media:.2f}")
print("Exercicio concluido!")
