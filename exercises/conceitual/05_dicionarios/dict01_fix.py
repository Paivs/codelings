# TITLE: Dicionarios - Chave Inexistente
# TYPE: fix
# DESCRIPTION: O codigo tenta acessar uma chave que nao existe no dicionario.
# ID: 010

aluno = {
    "nome": "Carlos",
    "nota": 8.5,
    "turma": "A",
}

print(f"Nome  : {aluno['nome']}")
print(f"Nota  : {aluno['nota']}")
print(f"Email : {aluno['email']}")
