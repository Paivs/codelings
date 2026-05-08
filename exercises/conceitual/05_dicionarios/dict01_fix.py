# TITULO: Dicionarios - Chave Inexistente
# TIPO: fix
# ID: 010

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema escolar exibe dados de um aluno, mas tenta acessar
# o campo 'email' que nao existe no cadastro, causando um erro.
#
# Corrija a linha marcada para que, quando o email nao estiver
# cadastrado, a variavel 'email' receba o valor "nao informado".
# =================================================================

aluno = {
    "nome" : "Carlos",
    "nota" : 8.5,
    "turma": "A",
}

email = aluno["email"]    # <- revise esta linha

print(f"Nome : {aluno['nome']}")
print(f"Nota : {aluno['nota']}")
print(f"Email: {email}")

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert email == "nao informado", "email deveria ser 'nao informado' quando ausente"
print("Exercicio concluido!")
