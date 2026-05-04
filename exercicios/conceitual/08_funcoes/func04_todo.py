# TITULO: Funcoes - Validador de Dados
# TIPO: todo
# ID: 062

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de cadastro precisa validar os campos de entrada antes
# de salvar os dados.
#
# Exemplos:
#   eh_email_valido("user@example.com") -> True
#   eh_email_valido("invalido")         -> False
#   eh_cpf_valido("12345678901")        -> True
#   eh_cpf_valido("123")               -> False
#   eh_maior_de_idade(18)              -> True
#   eh_maior_de_idade(17)              -> False
#
# Regras:
#   eh_email_valido  -> True se contem "@" e "." apos o "@"
#   eh_cpf_valido    -> True se tem exatamente 11 digitos numericos
#   eh_maior_de_idade -> True se idade >= 18
# =================================================================

# TAREFA: Implemente as tres funcoes de validacao.

def eh_email_valido(email):
    pass

def eh_cpf_valido(cpf):
    pass

def eh_maior_de_idade(idade):
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert eh_email_valido("user@example.com") is True,  "email valido recusado"
assert eh_email_valido("invalido")         is False, "email invalido aceito"
assert eh_email_valido("sem@ponto")        is False, "email sem ponto apos @ aceito"
assert eh_cpf_valido("12345678901")        is True,  "CPF valido recusado"
assert eh_cpf_valido("123")               is False, "CPF curto aceito"
assert eh_cpf_valido("1234567890a")       is False, "CPF com letra aceito"
assert eh_maior_de_idade(18)              is True,  "18 anos deve ser maior de idade"
assert eh_maior_de_idade(17)              is False, "17 anos nao deve ser maior de idade"
print("Todos os casos validados!")
print("Exercicio concluido!")
