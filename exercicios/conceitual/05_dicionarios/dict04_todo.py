# TITULO: Dicionarios - Registro de Alunos
# TIPO: todo
# ID: 050

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema escolar precisa calcular a media de cada aluno,
# listar os aprovados e identificar o melhor desempenho.
#
# Notas:
#   Alice -> [8.5, 9.0, 7.5]
#   Bruno -> [6.0, 7.0, 6.5]
#   Carol -> [9.5, 9.0, 10.0]
#
# Resultados esperados:
#   medias       -> {"Alice": 8.333..., "Bruno": 6.5, "Carol": 9.5}
#   aprovados    -> ["Alice", "Carol"]  (media >= 7.0)
#   melhor_aluno -> "Carol"
# =================================================================

notas = {
    "Alice": [8.5, 9.0, 7.5],
    "Bruno": [6.0, 7.0, 6.5],
    "Carol": [9.5, 9.0, 10.0],
}

# TAREFA: Calcule 'medias', 'aprovados' e 'melhor_aluno' a partir de 'notas'.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert abs(medias["Alice"] - 25/3)   < 0.01, f"media de Alice incorreta: {medias['Alice']}"
assert abs(medias["Bruno"] - 6.5)    < 0.01, f"media de Bruno incorreta: {medias['Bruno']}"
assert abs(medias["Carol"] - 9.5)    < 0.01, f"media de Carol incorreta: {medias['Carol']}"
assert "Alice" in aprovados,                  "Alice deveria estar aprovada"
assert "Carol" in aprovados,                  "Carol deveria estar aprovada"
assert "Bruno" not in aprovados,              "Bruno nao deveria estar aprovado"
assert melhor_aluno == "Carol",               f"melhor_aluno incorreto: {melhor_aluno}"
print(f"medias       = {medias}")
print(f"aprovados    = {aprovados}")
print(f"melhor_aluno = {melhor_aluno}")
print("Exercicio concluido!")
