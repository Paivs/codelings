# TITULO: Listas - Podio
# TIPO: todo
# ID: 046

# =================================================================
# ENUNCIADO
# =================================================================
# Uma competicao precisa encontrar os tres melhores resultados e
# calcular a media do podio.
#
# Pontuacoes: [45, 82, 61, 90, 73, 55, 88]
#
# Resultados esperados:
#   ordenadas   -> [90, 88, 82, 73, 61, 55, 45]  (ordem decrescente)
#   podio       -> [90, 88, 82]                   (top 3)
#   media_podio -> 86.666...
# =================================================================

pontuacoes = [45, 82, 61, 90, 73, 55, 88]

# TAREFA: Crie 'ordenadas', 'podio' e 'media_podio' a partir de 'pontuacoes'.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert ordenadas   == [90, 88, 82, 73, 61, 55, 45], f"ordenadas incorretas: {ordenadas}"
assert podio       == [90, 88, 82],                  f"podio incorreto: {podio}"
assert abs(media_podio - (90 + 88 + 82) / 3) < 0.01, f"media_podio incorreta: {media_podio}"
print(f"ordenadas   = {ordenadas}")
print(f"podio       = {podio}")
print(f"media_podio = {media_podio:.2f}")
print("Exercicio concluido!")
