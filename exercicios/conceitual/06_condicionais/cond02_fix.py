# TITULO: Condicionais - Fronteira de Idade
# TIPO: fix
# ID: 051

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema verifica se uma pessoa pode votar com base na idade,
# mas a condicao exclui quem tem exatamente 18 anos, que deveria
# ser permitido.
# =================================================================

def pode_votar(idade):
    if idade > 18:      # <- revise esta linha
        return True
    return False

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert pode_votar(18) is True,  "quem tem 18 anos deve poder votar"
assert pode_votar(17) is False, "quem tem 17 anos nao pode votar"
assert pode_votar(21) is True,  "quem tem 21 anos deve poder votar"
print(f"pode_votar(18) = {pode_votar(18)}")
print(f"pode_votar(17) = {pode_votar(17)}")
print(f"pode_votar(21) = {pode_votar(21)}")
print("Exercicio concluido!")
