# TITLE: Condicionais - Verificacao de Acesso
# TYPE: todo
# DESCRIPTION: Complete a funcao que decide se um usuario pode acessar o sistema.
# ID: 013

def pode_acessar(idade, tem_cadastro, esta_banido):
    """
    Retorna True somente se TODAS as condicoes forem atendidas:
      - Deve ter 18 anos ou mais
      - Deve ter cadastro
      - Nao deve estar banido
    """
    # TODO: Implemente e retorne o resultado (True ou False)
    pass


# --- Validacao (nao modifique abaixo) ---
assert pode_acessar(20, True,  False) is True,  "Usuario valido deveria ter acesso"
assert pode_acessar(16, True,  False) is False, "Menor de idade nao deveria ter acesso"
assert pode_acessar(20, False, False) is False, "Sem cadastro nao deveria ter acesso"
assert pode_acessar(20, True,  True)  is False, "Banido nao deveria ter acesso"
assert pode_acessar(17, False, True)  is False, "Multiplas restricoes"
assert pode_acessar(18, True,  False) is True,  "Exatamente 18 anos deve ter acesso"
print("Todos os casos validados!")
print("Exercicio concluido!")
