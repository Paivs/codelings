# TITULO: Condicionais - Controle de Acesso
# TIPO: todo
# ID: 013

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema precisa verificar se um usuario pode acessar a
# plataforma com base em tres criterios simultaneos.
#
# Exemplos:
#   pode_acessar(20, True,  False) -> True
#   pode_acessar(16, True,  False) -> False  (menor de idade)
#   pode_acessar(20, False, False) -> False  (sem cadastro)
#   pode_acessar(20, True,  True)  -> False  (banido)
#
# Regras de negocio:
#   - Deve ter 18 anos ou mais
#   - Deve ter cadastro ativo
#   - Nao pode estar banido
#   Todas as tres condicoes precisam ser verdadeiras ao mesmo tempo.
# =================================================================

def pode_acessar(idade, tem_cadastro, esta_banido):
    # TAREFA: Implemente a funcao seguindo as tres regras de negocio.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert pode_acessar(20, True,  False) is True,  "usuario valido deveria ter acesso"
assert pode_acessar(16, True,  False) is False, "menor de idade nao deveria ter acesso"
assert pode_acessar(20, False, False) is False, "sem cadastro nao deveria ter acesso"
assert pode_acessar(20, True,  True)  is False, "banido nao deveria ter acesso"
assert pode_acessar(17, False, True)  is False, "multiplas restricoes"
assert pode_acessar(18, True,  False) is True,  "exatamente 18 anos deveria ter acesso"
print("Todos os casos validados!")
print("Exercicio concluido!")
