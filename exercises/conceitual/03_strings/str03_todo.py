# TITULO: Strings - Analise de Senha
# TIPO: todo
# ID: 041

# =================================================================
# ENUNCIADO
# =================================================================
# Um validador precisa produzir diferentes representacoes de uma
# senha para fins de analise e exibicao.
#
# Senha de entrada: "Python3!"
#
# Resultados esperados:
#   tamanho       -> 8             (quantidade de caracteres)
#   em_maiusculo  -> "PYTHON3!"   (toda em maiusculas)
#   sem_exclamacao -> "Python3"   (senha com "!" removido)
#   invertida     -> "!3nohtyP"   (senha com caracteres em ordem inversa)
# =================================================================

senha = "Python3!"

# TAREFA: Crie as quatro variaveis a partir de 'senha'.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert tamanho        == 8,          f"tamanho deveria ser 8, mas e {tamanho}"
assert em_maiusculo   == "PYTHON3!", f"em_maiusculo incorreto: {em_maiusculo!r}"
assert sem_exclamacao == "Python3",  f"sem_exclamacao incorreto: {sem_exclamacao!r}"
assert invertida      == "!3nohtyP", f"invertida incorreto: {invertida!r}"
print(f"tamanho        = {tamanho}")
print(f"em_maiusculo   = {em_maiusculo!r}")
print(f"sem_exclamacao = {sem_exclamacao!r}")
print(f"invertida      = {invertida!r}")
print("Exercicio concluido!")
