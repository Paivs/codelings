# TITULO: Strings - Formatacao de CPF
# TIPO: fix
# ID: 040

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema formata CPF no padrao NNN.NNN.NNN-NN, mas o ultimo
# bloco esta com os indices errados e nao captura os dois digitos
# finais corretamente.
# =================================================================

cpf       = "12345678901"
formatado = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[10:]}"    # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert formatado == "123.456.789-01", f"formatado incorreto: {formatado!r}"
print(f"cpf       = {cpf}")
print(f"formatado = {formatado}")
print("Exercicio concluido!")
