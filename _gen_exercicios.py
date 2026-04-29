"""Script gerador — reescreve todos os exercicios no novo formato."""
from pathlib import Path

BASE = Path(__file__).parent

files = {}

# ── 001 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/01_variaveis/var01_fix.py"] = """\
# TITULO: Variaveis - Erro de Digitacao
# TIPO: fix
# ID: 001

# =================================================================
# ENUNCIADO
# =================================================================
# O sistema de cadastro abaixo deveria exibir os dados de um
# usuario, mas ha um erro de digitacao no nome de uma variavel.
#
# Corrija o codigo para que ele rode sem erros.
# =================================================================

nome   = "Ana"
iddade = 22
cidade = "Recife"

print(f"Nome  : {nome}")
print(f"Idade : {idade}")     # <- revise esta linha
print(f"Cidade: {cidade}")

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert nome   == "Ana",    "nome incorreto"
assert idade  == 22,       "idade incorreta"
assert cidade == "Recife", "cidade incorreta"
print("Exercicio concluido!")
"""

# ── 002 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/01_variaveis/var02_fix.py"] = """\
# TITULO: Variaveis - Incompatibilidade de Tipos
# TIPO: fix
# ID: 002

# =================================================================
# ENUNCIADO
# =================================================================
# Um formulario recebe o ano de nascimento como texto e tenta
# calcular ha quantos anos isso foi, mas o codigo quebra.
#
# Corrija o codigo para que o calculo funcione corretamente.
# =================================================================

ano_nascimento = "1999"
ano_atual      = 2024
anos_atras     = ano_atual - ano_nascimento    # <- revise esta linha

print(f"Voce nasceu ha {anos_atras} anos.")

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert anos_atras == 25, "calculo do tempo incorreto"
print("Exercicio concluido!")
"""

# ── 003 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/01_variaveis/var03_todo.py"] = """\
# TITULO: Variaveis - Sistema de Pedidos
# TIPO: todo
# ID: 003

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de pedidos precisa registrar as informacoes de uma
# compra para calcular o valor total.
#
# Variaveis necessarias:
#   produto    -> "Caderno"  (str)
#   preco      -> 12.50      (float, valor unitario em reais)
#   quantidade -> 3          (int)
# =================================================================

# TAREFA: Crie as tres variaveis acima com os valores e tipos corretos.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert produto    == "Caderno", "produto incorreto"
assert preco      == 12.50,     "preco incorreto"
assert quantidade == 3,         "quantidade incorreta"
assert isinstance(preco,      float), "preco deve ser float"
assert isinstance(quantidade, int),   "quantidade deve ser int"
total = preco * quantidade
print(f"Produto   : {produto}")
print(f"Preco     : R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total     : R$ {total:.2f}")
print("Exercicio concluido!")
"""

# ── 004 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/02_tipos/tipo01_fix.py"] = """\
# TITULO: Tipos - Entrada como String
# TIPO: fix
# ID: 004

# =================================================================
# ENUNCIADO
# =================================================================
# Um formulario captura o ano de nascimento e tenta calcular ha
# quantos anos o usuario nasceu, mas o codigo quebra.
#
# Lembre-se: valores vindos de input() sao sempre strings.
# Corrija o codigo para que o calculo funcione.
# =================================================================

entrada    = "2005"
ano_atual  = 2024
anos_atras = ano_atual - entrada    # <- revise esta linha

print(f"Voce nasceu ha {anos_atras} anos.")

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert anos_atras == 19, "calculo incorreto"
print("Exercicio concluido!")
"""

# ── 005 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/02_tipos/tipo02_todo.py"] = """\
# TITULO: Tipos - Conversao Entre Tipos
# TIPO: todo
# ID: 005

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de processamento de dados recebe valores em formatos
# variados e precisa converte-los para os tipos corretos.
#
# Conversoes necessarias:
#   "42"  ->  42      (int)
#   7     ->  7.0     (float)
#   0     ->  False   (bool)
#   99    ->  "99"    (str)
# =================================================================

# TAREFA: Crie as quatro variaveis abaixo aplicando a conversao correta.
# numero_inteiro -> converta a string "42" para int
# numero_float   -> converta o inteiro 7 para float
# valor_falso    -> converta o inteiro 0 para bool
# numero_texto   -> converta o inteiro 99 para str


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert numero_inteiro == 42,    "numero_inteiro incorreto"
assert numero_float   == 7.0,   "numero_float incorreto"
assert valor_falso    is False, "valor_falso incorreto"
assert numero_texto   == "99",  "numero_texto incorreto"
assert isinstance(numero_inteiro, int),   "numero_inteiro deve ser int"
assert isinstance(numero_float,   float), "numero_float deve ser float"
assert isinstance(valor_falso,    bool),  "valor_falso deve ser bool"
assert isinstance(numero_texto,   str),   "numero_texto deve ser str"
print(f"int  : {numero_inteiro!r}")
print(f"float: {numero_float!r}")
print(f"bool : {valor_falso!r}")
print(f"str  : {numero_texto!r}")
print("Exercicio concluido!")
"""

# ── 006 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/03_strings/str01_fix.py"] = """\
# TITULO: Strings - Metodo Inexistente
# TIPO: fix
# ID: 006

# =================================================================
# ENUNCIADO
# =================================================================
# Um gerador de cartoes de visita formata nomes e textos, mas
# um dos metodos de string usados nao existe em Python.
#
# Corrija o nome do metodo para que o codigo funcione.
# =================================================================

frase = "python e uma linguagem incrivel"

frase_titulo    = frase.totitle()     # <- revise esta linha
frase_maiuscula = frase.upper()
frase_limpa     = "  ola mundo  ".strip()

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert frase_titulo    == "Python E Uma Linguagem Incrivel", "frase_titulo incorreto"
assert frase_maiuscula == "PYTHON E UMA LINGUAGEM INCRIVEL", "frase_maiuscula incorreto"
assert frase_limpa     == "ola mundo",                       "frase_limpa incorreto"
print(frase_titulo)
print(frase_maiuscula)
print(frase_limpa)
print("Exercicio concluido!")
"""

# ── 007 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/03_strings/str02_todo.py"] = """\
# TITULO: Strings - Processamento de Texto
# TIPO: todo
# ID: 007

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de busca precisa processar uma frase para indexacao.
#
# Texto de entrada:
#   "a raposa marrom pula sobre o cao preguicoso"
#
# Resultados esperados:
#   texto_maiusculo     -> frase toda em maiusculas
#   palavras            -> lista com cada palavra separada
#   quantidade_palavras -> numero total de palavras (8)
#   novo_texto          -> frase com "cao" substituido por "gato"
# =================================================================

texto = "a raposa marrom pula sobre o cao preguicoso"

# TAREFA: Crie as quatro variaveis acima aplicando as transformacoes
# sobre 'texto'. Metodos uteis: .upper(), .split(), .replace().


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert texto_maiusculo    == "A RAPOSA MARROM PULA SOBRE O CAO PREGUICOSO", "texto_maiusculo incorreto"
assert isinstance(palavras, list),                                            "palavras deve ser uma lista"
assert quantidade_palavras == 8,                                              "quantidade de palavras incorreta"
assert novo_texto          == "a raposa marrom pula sobre o gato preguicoso", "novo_texto incorreto"
print(f"Maiusculo : {texto_maiusculo}")
print(f"Palavras  : {palavras}")
print(f"Quantidade: {quantidade_palavras}")
print(f"Novo texto: {novo_texto}")
print("Exercicio concluido!")
"""

# ── 008 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/04_listas/list01_fix.py"] = """\
# TITULO: Listas - Indice Fora do Intervalo
# TIPO: fix
# ID: 008

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de estoque tenta exibir a primeira, a segunda e a
# ultima fruta de uma lista, mas o indice do ultimo elemento
# esta errado.
#
# Corrija o acesso ao ultimo elemento da lista.
# =================================================================

frutas = ["maca", "banana", "laranja", "uva"]

print(f"Primeira: {frutas[0]}")
print(f"Segunda : {frutas[1]}")
print(f"Ultima  : {frutas[4]}")    # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert frutas[0]  == "maca",   "primeira fruta incorreta"
assert frutas[1]  == "banana", "segunda fruta incorreta"
assert frutas[-1] == "uva",    "ultima fruta incorreta"
print("Exercicio concluido!")
"""

# ── 009 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/04_listas/list02_todo.py"] = """\
# TITULO: Listas - Gerenciamento de Estoque
# TIPO: todo
# ID: 009

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de controle de estoque realiza operacoes sobre
# uma lista de codigos de produtos (representados por numeros).
#
# Lista inicial: [5, 2, 8, 1, 9, 3]
#
# Operacoes necessarias (nesta ordem):
#   1. Adicionar o numero 7 ao final da lista
#   2. Remover o numero 2 da lista
#   3. Ordenar a lista em ordem crescente
#   4. Calcular a soma total  -> guardar em 'total'
#   5. Contar os elementos    -> guardar em 'tamanho'
# =================================================================

numeros = [5, 2, 8, 1, 9, 3]

# TAREFA: Execute as cinco operacoes acima sobre a lista 'numeros'
# usando os metodos: append(), remove(), sort(), sum(), len().


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert numeros == [1, 3, 5, 7, 8, 9], "lista incorreta apos as operacoes"
assert total   == 33,                  "total incorreto"
assert tamanho == 6,                   "tamanho incorreto"
print(f"Lista  : {numeros}")
print(f"Total  : {total}")
print(f"Tamanho: {tamanho}")
print("Exercicio concluido!")
"""

# ── 010 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/05_dicionarios/dict01_fix.py"] = """\
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
"""

# ── 011 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/05_dicionarios/dict02_todo.py"] = """\
# TITULO: Dicionarios - Gestao de Estoque
# TIPO: todo
# ID: 011

# =================================================================
# ENUNCIADO
# =================================================================
# Um mercado gerencia o estoque de frutas em um dicionario.
# Realize as operacoes necessarias para atualizar o estoque.
#
# Estoque inicial: {"maca": 10, "banana": 5, "laranja": 8}
#
# Operacoes (nesta ordem):
#   1. Adicionar "uva" com quantidade 15
#   2. Atualizar "banana" para quantidade 12
#   3. Remover "laranja" do estoque
#   4. Somar todos os valores -> guardar em 'total_itens'
# =================================================================

estoque = {
    "maca"  : 10,
    "banana": 5,
    "laranja": 8,
}

# TAREFA: Execute as quatro operacoes acima sobre o dicionario 'estoque'.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert "uva"     in estoque,         "uva deve estar no estoque"
assert "laranja" not in estoque,     "laranja deve ter sido removida"
assert estoque.get("uva")    == 15,  "quantidade de uva incorreta"
assert estoque.get("banana") == 12,  "quantidade de banana incorreta"
assert total_itens           == 37,  "total de itens incorreto"
print(f"Estoque    : {estoque}")
print(f"Total itens: {total_itens}")
print("Exercicio concluido!")
"""

# ── 012 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/06_condicionais/cond01_fix.py"] = """\
# TITULO: Condicionais - Classificacao de Notas
# TIPO: fix
# ID: 012

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema escolar classifica notas em categorias. A funcao esta
# quase correta, mas um operador de comparacao esta errado,
# fazendo com que notas na fronteira sejam mal classificadas.
#
# Regras de negocio:
#   >= 9 -> "Excelente" | >= 7 -> "Bom"
#   >= 5 -> "Regular"   | >= 0 -> "Insuficiente" | fora -> "Invalida"
# =================================================================

def classificar_nota(nota):
    if nota > 10 or nota < 0:
        return "Invalida"
    if nota >= 9:
        return "Excelente"
    if nota >= 7:
        return "Bom"
    if nota > 5:              # <- revise esta linha
        return "Regular"
    return "Insuficiente"

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert classificar_nota(10) == "Excelente",    "nota 10 incorreta"
assert classificar_nota(9)  == "Excelente",    "nota 9 incorreta"
assert classificar_nota(8)  == "Bom",          "nota 8 incorreta"
assert classificar_nota(7)  == "Bom",          "nota 7 incorreta"
assert classificar_nota(6)  == "Regular",      "nota 6 incorreta"
assert classificar_nota(5)  == "Regular",      "nota 5 incorreta"
assert classificar_nota(4)  == "Insuficiente", "nota 4 incorreta"
assert classificar_nota(-1) == "Invalida",     "nota -1 incorreta"
assert classificar_nota(11) == "Invalida",     "nota 11 incorreta"
for n in [10, 9, 7, 5, 4, -1]:
    print(f"  nota {n:>2} -> {classificar_nota(n)}")
print("Exercicio concluido!")
"""

# ── 013 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/06_condicionais/cond02_todo.py"] = """\
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
    # TAREFA: Retorne True somente se todas as tres regras forem
    # satisfeitas ao mesmo tempo. Use os operadores 'and' e 'not'.
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
"""

# ── 014 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/07_loops/loop01_fix.py"] = """\
# TITULO: Loops - Range Incorreto
# TIPO: fix
# ID: 014

# =================================================================
# ENUNCIADO
# =================================================================
# Um relatorio precisa listar os numeros de 1 a 10, mas o loop
# esta gerando uma sequencia diferente da esperada.
#
# Corrija o range para que a lista contenha exatamente os inteiros
# de 1 a 10, inclusive.
# =================================================================

numeros = []
for i in range(0, 10):    # <- revise esta linha
    numeros.append(i)

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert numeros == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "lista incorreta"
print(f"Numeros: {numeros}")
print("Exercicio concluido!")
"""

# ── 015 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/07_loops/loop02_todo.py"] = """\
# TITULO: Loops - Analise de Dados
# TIPO: todo
# ID: 015

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de analise recebe uma lista de medicoes e precisa
# calcular estatisticas basicas usando loops for.
#
# Lista: [3, 7, 2, 9, 1, 5, 8, 4, 6]
#
# Resultados esperados:
#   soma  -> 45
#   maior -> 9
#   pares -> [2, 8, 4, 6]  (na ordem em que aparecem)
# =================================================================

numeros = [3, 7, 2, 9, 1, 5, 8, 4, 6]

# TAREFA: Use tres loops for separados para calcular 'soma', 'maior'
# e a lista 'pares'. Nao use sum(), max() ou list comprehensions.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert soma          == 45,           "soma incorreta"
assert maior         == 9,            "maior incorreto"
assert sorted(pares) == [2, 4, 6, 8], "pares incorretos"
print(f"Soma  : {soma}")
print(f"Maior : {maior}")
print(f"Pares : {pares}")
print("Exercicio concluido!")
"""

# ── 016 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/08_funcoes/func01_fix.py"] = """\
# TITULO: Funcoes - Return Ausente
# TIPO: fix
# ID: 016

# =================================================================
# ENUNCIADO
# =================================================================
# Uma funcao calcula a area de um retangulo, mas nao devolve
# o resultado para quem a chamou. Por isso, 'resultado' recebe
# None em vez do valor calculado.
#
# Adicione o comando necessario para a funcao devolver o valor.
# =================================================================

def area_retangulo(largura, altura):
    area = largura * altura
    # <- falta algo aqui

resultado = area_retangulo(5, 3)

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert resultado == 15, "resultado incorreto — verifique o retorno da funcao"
print(f"Area do retangulo 5x3: {resultado}")
print("Exercicio concluido!")
"""

# ── 017 ─────────────────────────────────────────────────────────────────────
files["exercicios/conceitual/08_funcoes/func02_todo.py"] = """\
# TITULO: Funcoes - Calculadora
# TIPO: todo
# ID: 017

# =================================================================
# ENUNCIADO
# =================================================================
# Um aplicativo de calculadora precisa das quatro operacoes basicas.
#
# Exemplos:
#   somar(3, 4)       -> 7
#   subtrair(10, 3)   -> 7
#   multiplicar(4, 5) -> 20
#   dividir(15, 3)    -> 5.0
#   dividir(10, 0)    -> None
#
# Regras de negocio:
#   - Cada funcao recebe dois numeros e retorna o resultado
#   - dividir() retorna None quando o divisor for zero
# =================================================================

# TAREFA: Implemente as quatro funcoes abaixo.
# somar       -> retorna a + b
# subtrair    -> retorna a - b
# multiplicar -> retorna a * b
# dividir     -> retorna a / b, ou None se b == 0

def somar(a, b):
    pass

def subtrair(a, b):
    pass

def multiplicar(a, b):
    pass

def dividir(a, b):
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert somar(3, 4)       == 7,    "somar incorreto"
assert subtrair(10, 3)   == 7,    "subtrair incorreto"
assert multiplicar(4, 5) == 20,   "multiplicar incorreto"
assert dividir(15, 3)    == 5,    "dividir incorreto"
assert dividir(10, 0)    is None, "divisao por zero deve retornar None"
print(f"somar(3, 4)       = {somar(3, 4)}")
print(f"subtrair(10, 3)   = {subtrair(10, 3)}")
print(f"multiplicar(4, 5) = {multiplicar(4, 5)}")
print(f"dividir(15, 3)    = {dividir(15, 3)}")
print(f"dividir(10, 0)    = {dividir(10, 0)}")
print("Exercicio concluido!")
"""

# ── 018 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/01_palindromo/palindrome_fix.py"] = """\
# TITULO: Palindromo - Bug na Inversao
# TIPO: fix
# ID: 018

# =================================================================
# ENUNCIADO
# =================================================================
# Um verificador de palindromos foi implementado, mas ha um bug
# na operacao que inverte a string para comparacao.
#
# Corrija a operacao de inversao da string.
# =================================================================

def eh_palindromo(texto):
    limpo = texto.lower().replace(" ", "")
    return limpo == limpo[1:]   # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert eh_palindromo("radar")  is True,  "radar deveria ser palindromo"
assert eh_palindromo("arara")  is True,  "arara deveria ser palindromo"
assert eh_palindromo("python") is False, "python nao e palindromo"
assert eh_palindromo("A man a plan a canal Panama") is True, "frase palindromo incorreta"
print(f"radar  -> {eh_palindromo('radar')}")
print(f"arara  -> {eh_palindromo('arara')}")
print(f"python -> {eh_palindromo('python')}")
print("Exercicio concluido!")
"""

# ── 019 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/01_palindromo/palindrome_todo.py"] = """\
# TITULO: Palindromo - Implementar
# TIPO: todo
# ID: 019

# =================================================================
# ENUNCIADO
# =================================================================
# Um verificador de textos precisa identificar palindromos — palavras
# ou frases que se leem da mesma forma de tras para frente.
#
# Exemplos:
#   eh_palindromo("radar")                       -> True
#   eh_palindromo("python")                      -> False
#   eh_palindromo("A man a plan a canal Panama") -> True
#
# Regras de negocio:
#   - Ignorar maiusculas e minusculas
#   - Ignorar espacos
#   - String vazia e considerada palindromo
# =================================================================

def eh_palindromo(texto):
    # TAREFA: Normalize o texto (minusculo, sem espacos) e verifique
    # se ele e igual ao seu reverso. Use fatiamento [::-1] para inverter.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert eh_palindromo("radar")  is True,  "radar deve ser palindromo"
assert eh_palindromo("arara")  is True,  "arara deve ser palindromo"
assert eh_palindromo("python") is False, "python nao e palindromo"
assert eh_palindromo("A man a plan a canal Panama") is True, "frase palindromo incorreta"
assert eh_palindromo("")       is True,  "string vazia deve ser palindromo"
print(f"radar   -> {eh_palindromo('radar')}")
print(f"python  -> {eh_palindromo('python')}")
print(f"A man a plan... -> {eh_palindromo('A man a plan a canal Panama')}")
print("Exercicio concluido!")
"""

# ── 020 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/02_anagrama/anagrama_fix.py"] = """\
# TITULO: Anagrama Valido - Bug na Normalizacao
# TIPO: fix
# ID: 020

# =================================================================
# ENUNCIADO
# =================================================================
# Um verificador de anagramas compara duas strings, mas nao
# normaliza o texto antes da comparacao, causando falsos negativos
# quando ha maiusculas ou espacos.
#
# Corrija a funcao para que ela ignore maiusculas e espacos.
# =================================================================

def eh_anagrama(a, b):
    return sorted(a) == sorted(b)   # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert eh_anagrama("listen", "silent")          is True,  "caso 1 incorreto"
assert eh_anagrama("Listen", "Silent")          is True,  "deve ignorar maiusculas"
assert eh_anagrama("Astronomer", "Moon starer") is True,  "deve ignorar espacos"
assert eh_anagrama("hello", "world")            is False, "nao sao anagramas"
print(f"listen / silent          -> {eh_anagrama('listen', 'silent')}")
print(f"Listen / Silent          -> {eh_anagrama('Listen', 'Silent')}")
print(f"Astronomer / Moon starer -> {eh_anagrama('Astronomer', 'Moon starer')}")
print("Exercicio concluido!")
"""

# ── 021 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/02_anagrama/anagrama_todo.py"] = """\
# TITULO: Anagrama Valido - Implementar
# TIPO: todo
# ID: 021

# =================================================================
# ENUNCIADO
# =================================================================
# Dois textos sao anagramas quando contem exatamente as mesmas
# letras, em qualquer ordem.
#
# Exemplos:
#   eh_anagrama("listen", "silent")          -> True
#   eh_anagrama("Astronomer", "Moon starer") -> True
#   eh_anagrama("hello", "world")            -> False
#
# Regras de negocio:
#   - Ignorar maiusculas e minusculas
#   - Ignorar espacos
#   - Strings com quantidades diferentes de letras nunca sao anagramas
# =================================================================

def eh_anagrama(a, b):
    # TAREFA: Normalize as duas strings (minusculo, sem espacos) e
    # compare-as ordenadas. Dois textos sao anagramas se, apos a
    # normalizacao, sorted(a) == sorted(b).
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert eh_anagrama("listen", "silent")          is True,  "caso 1 incorreto"
assert eh_anagrama("Listen", "Silent")          is True,  "caso 2 incorreto"
assert eh_anagrama("Astronomer", "Moon starer") is True,  "caso 3 incorreto"
assert eh_anagrama("hello", "world")            is False, "caso 4 incorreto"
assert eh_anagrama("abc", "cba")                is True,  "caso 5 incorreto"
assert eh_anagrama("abc", "abcd")               is False, "caso 6 incorreto"
print(f"listen / silent          -> {eh_anagrama('listen', 'silent')}")
print(f"Astronomer / Moon starer -> {eh_anagrama('Astronomer', 'Moon starer')}")
print(f"hello / world            -> {eh_anagrama('hello', 'world')}")
print("Exercicio concluido!")
"""

# ── 022 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/03_prefixo_comum/prefixo_fix.py"] = """\
# TITULO: Prefixo Comum - Bug no Corte da String
# TIPO: fix
# ID: 022

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de autocomplete encontra o maior prefixo comum entre
# palavras, mas ha um bug: ao encurtar o prefixo, ele remove do
# lado errado da string.
#
# Corrija a direcao do corte.
# =================================================================

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while prefix and not s.startswith(prefix):
            prefix = prefix[1:]   # <- revise esta linha
    return prefix

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert longest_common_prefix(["flower", "flow", "flight"])       == "fl",    "caso 1 incorreto"
assert longest_common_prefix(["dog", "racecar", "car"])           == "",     "caso 2 incorreto"
assert longest_common_prefix(["interview", "inter", "internal"]) == "inter", "caso 3 incorreto"
assert longest_common_prefix(["a"])                               == "a",    "caso 4 incorreto"
assert longest_common_prefix([])                                  == "",     "caso 5 incorreto"
print('["flower","flow","flight"]      ->', longest_common_prefix(["flower","flow","flight"]))
print('["dog","racecar","car"]          ->', longest_common_prefix(["dog","racecar","car"]))
print('["interview","inter","internal"] ->', longest_common_prefix(["interview","inter","internal"]))
print("Exercicio concluido!")
"""

# ── 023 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/03_prefixo_comum/prefixo_todo.py"] = """\
# TITULO: Prefixo Comum - Implementar
# TIPO: todo
# ID: 023

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de autocomplete precisa encontrar o maior trecho
# inicial comum entre todas as palavras de uma lista.
#
# Exemplos:
#   longest_common_prefix(["flower", "flow", "flight"])       -> "fl"
#   longest_common_prefix(["dog", "racecar", "car"])          -> ""
#   longest_common_prefix(["interview", "inter", "internal"]) -> "inter"
#
# Regras de negocio:
#   - Lista vazia retorna ""
#   - Lista com uma palavra retorna a propria palavra
#   - Se nao houver prefixo comum, retorna ""
# =================================================================

def longest_common_prefix(strs):
    # TAREFA: Itere pelos caracteres da primeira string. Para cada
    # posicao i, verifique se todas as outras strings tem o mesmo
    # caractere nessa posicao. Pare ao encontrar uma divergencia ou
    # quando alguma string for mais curta que i.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert longest_common_prefix(["flower", "flow", "flight"])       == "fl",    "caso 1 incorreto"
assert longest_common_prefix(["dog", "racecar", "car"])           == "",     "caso 2 incorreto"
assert longest_common_prefix(["interview", "inter", "internal"]) == "inter", "caso 3 incorreto"
assert longest_common_prefix(["a"])                               == "a",    "caso 4 incorreto"
assert longest_common_prefix([])                                  == "",     "caso 5 incorreto"
assert longest_common_prefix(["abc", "abc", "abc"])               == "abc",  "caso 6 incorreto"
print('["flower","flow","flight"]      ->', longest_common_prefix(["flower","flow","flight"]))
print('["dog","racecar","car"]          ->', longest_common_prefix(["dog","racecar","car"]))
print("Exercicio concluido!")
"""

# ── 024 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/04_two_sum/two_sum_fix.py"] = """\
# TITULO: Two Sum - Bug no Calculo do Complemento
# TIPO: fix
# ID: 024

# =================================================================
# ENUNCIADO
# =================================================================
# A funcao two_sum encontra os indices de dois numeros que somam
# o alvo, mas o complemento esta sendo calculado de forma errada,
# fazendo a busca procurar o par incorreto.
#
# Corrija a operacao matematica que calcula o complemento.
# =================================================================

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        comp = target + n       # <- revise esta linha
        if comp in seen:
            return [seen[comp], i]
        seen[n] = i

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert two_sum([2, 7, 11, 15], 9) == [0, 1], "caso 1 incorreto"
assert two_sum([3, 2, 4], 6)      == [1, 2], "caso 2 incorreto"
assert two_sum([3, 3], 6)         == [0, 1], "caso 3 incorreto"
print("two_sum([2, 7, 11, 15], 9) =", two_sum([2, 7, 11, 15], 9))
print("two_sum([3, 2, 4], 6)      =", two_sum([3, 2, 4], 6))
print("Exercicio concluido!")
"""

# ── 025 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/04_two_sum/two_sum_todo.py"] = """\
# TITULO: Two Sum - Implementar
# TIPO: todo
# ID: 025

# =================================================================
# ENUNCIADO
# =================================================================
# Dado um array de inteiros e um valor alvo, encontre os indices
# de dois numeros que somados sejam iguais ao alvo.
#
# Exemplos:
#   two_sum([2, 7, 11, 15], 9)  ->  [0, 1]   # 2 + 7 = 9
#   two_sum([3, 2, 4], 6)       ->  [1, 2]   # 2 + 4 = 6
#   two_sum([3, 3], 6)          ->  [0, 1]   # 3 + 3 = 6
#
# Regras de negocio:
#   - Cada entrada tem exatamente uma solucao
#   - O mesmo elemento nao pode ser usado duas vezes
#   - Retorne os indices em ordem crescente [menor, maior]
# =================================================================

def two_sum(nums, target):
    # TAREFA: Use um dicionario para guardar cada numero ja visitado
    # e seu indice. Para cada nums[i], calcule o complemento
    # (target - nums[i]). Se o complemento ja estiver no dicionario,
    # retorne os dois indices.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert two_sum([2, 7, 11, 15], 9) == [0, 1], "caso 1 incorreto"
assert two_sum([3, 2, 4], 6)      == [1, 2], "caso 2 incorreto"
assert two_sum([3, 3], 6)         == [0, 1], "caso 3 incorreto"
print("two_sum([2, 7, 11, 15], 9) =", two_sum([2, 7, 11, 15], 9))
print("two_sum([3, 2, 4], 6)      =", two_sum([3, 2, 4], 6))
print("two_sum([3, 3], 6)         =", two_sum([3, 3], 6))
print("Exercicio concluido!")
"""

# ── 026 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/05_mover_zeros/mover_zeros_fix.py"] = """\
# TITULO: Mover Zeros - Bug no Valor de Preenchimento
# TIPO: fix
# ID: 026

# =================================================================
# ENUNCIADO
# =================================================================
# A funcao move todos os zeros para o final da lista, mas preenche
# as posicoes finais com o valor errado.
#
# Corrija o valor usado para preencher as posicoes dos zeros.
# =================================================================

def mover_zeros(nums):
    nao_zeros = [n for n in nums if n != 0]
    zeros     = len(nums) - len(nao_zeros)
    return nao_zeros + [1] * zeros   # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert mover_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0], "caso 1 incorreto"
assert mover_zeros([0])              == [0],               "caso 2 incorreto"
assert mover_zeros([1, 2, 3])        == [1, 2, 3],         "caso 3 incorreto"
assert mover_zeros([0, 0, 1])        == [1, 0, 0],         "caso 4 incorreto"
print("mover_zeros([0, 1, 0, 3, 12]) =", mover_zeros([0, 1, 0, 3, 12]))
print("mover_zeros([0, 0, 1])        =", mover_zeros([0, 0, 1]))
print("Exercicio concluido!")
"""

# ── 027 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/05_mover_zeros/mover_zeros_todo.py"] = """\
# TITULO: Mover Zeros - Implementar
# TIPO: todo
# ID: 027

# =================================================================
# ENUNCIADO
# =================================================================
# Dada uma lista de inteiros, mova todos os zeros para o final
# sem alterar a ordem relativa dos outros elementos.
#
# Exemplos:
#   mover_zeros([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
#   mover_zeros([0])               -> [0]
#   mover_zeros([1, 2, 3])         -> [1, 2, 3]
#
# Regras de negocio:
#   - A ordem dos elementos nao-zero deve ser preservada
#   - Retorne uma nova lista (nao modifique a original)
# =================================================================

def mover_zeros(nums):
    # TAREFA: Separe os elementos nao-zero em uma lista. Calcule
    # quantos zeros existem e concatene-os ao final.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert mover_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0], "caso 1 incorreto"
assert mover_zeros([0])              == [0],               "caso 2 incorreto"
assert mover_zeros([1, 2, 3])        == [1, 2, 3],         "caso 3 incorreto"
assert mover_zeros([0, 0, 1])        == [1, 0, 0],         "caso 4 incorreto"
assert mover_zeros([0, 0, 0])        == [0, 0, 0],         "caso 5 incorreto"
assert mover_zeros([4, 0, 2, 0, 5])  == [4, 2, 5, 0, 0],  "caso 6 incorreto"
print("mover_zeros([0, 1, 0, 3, 12]) =", mover_zeros([0, 1, 0, 3, 12]))
print("mover_zeros([4, 0, 2, 0, 5])  =", mover_zeros([4, 0, 2, 0, 5]))
print("Exercicio concluido!")
"""

# ── 028 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/06_fizzbuzz/fizzbuzz_fix.py"] = """\
# TITULO: FizzBuzz - Bug no Nome Retornado
# TIPO: fix
# ID: 028

# =================================================================
# ENUNCIADO
# =================================================================
# A funcao FizzBuzz retorna uma string errada para multiplos de 3.
# Em vez de "Fizz", ela retorna "Bizz".
#
# Corrija o valor retornado para multiplos de 3.
# =================================================================

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Bizz"    # <- revise esta linha
    if n % 5 == 0:
        return "Buzz"
    return str(n)

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert fizzbuzz(1)  == "1",        "caso 1 incorreto"
assert fizzbuzz(3)  == "Fizz",     "caso 2 incorreto"
assert fizzbuzz(5)  == "Buzz",     "caso 3 incorreto"
assert fizzbuzz(15) == "FizzBuzz", "caso 4 incorreto"
assert fizzbuzz(9)  == "Fizz",     "caso 5 incorreto"
print("FizzBuzz de 1 a 20:")
print(" ".join(fizzbuzz(i) for i in range(1, 21)))
print("Exercicio concluido!")
"""

# ── 029 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/06_fizzbuzz/fizzbuzz_todo.py"] = """\
# TITULO: FizzBuzz - Implementar
# TIPO: todo
# ID: 029

# =================================================================
# ENUNCIADO
# =================================================================
# FizzBuzz e um problema classico de programacao.
#
# Exemplos:
#   fizzbuzz(1)  -> "1"
#   fizzbuzz(3)  -> "Fizz"
#   fizzbuzz(5)  -> "Buzz"
#   fizzbuzz(15) -> "FizzBuzz"
#
# Regras de negocio (verificar nesta ordem):
#   1. Divisivel por 3 E por 5  -> "FizzBuzz"
#   2. Divisivel apenas por 3   -> "Fizz"
#   3. Divisivel apenas por 5   -> "Buzz"
#   4. Qualquer outro numero    -> str(n)
# =================================================================

def fizzbuzz(n):
    # TAREFA: Implemente as quatro regras usando o operador % (modulo).
    # A ordem das verificacoes importa: teste FizzBuzz antes de Fizz e Buzz.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert fizzbuzz(1)  == "1",        "caso 1 incorreto"
assert fizzbuzz(3)  == "Fizz",     "caso 2 incorreto"
assert fizzbuzz(5)  == "Buzz",     "caso 3 incorreto"
assert fizzbuzz(15) == "FizzBuzz", "caso 4 incorreto"
assert fizzbuzz(9)  == "Fizz",     "caso 5 incorreto"
assert fizzbuzz(10) == "Buzz",     "caso 6 incorreto"
assert fizzbuzz(30) == "FizzBuzz", "caso 7 incorreto"
print("FizzBuzz de 1 a 20:")
print(" ".join(fizzbuzz(i) for i in range(1, 21)))
print("Exercicio concluido!")
"""

# ── 030 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/07_fibonacci/fibonacci_fix.py"] = """\
# TITULO: Fibonacci - Bug no Range do Loop
# TIPO: fix
# ID: 030

# =================================================================
# ENUNCIADO
# =================================================================
# A funcao gera a sequencia de Fibonacci, mas o range do loop esta
# errado, fazendo com que mais termos do que o pedido sejam gerados.
#
# Corrija o range para que a funcao retorne exatamente n termos.
# =================================================================

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(n):           # <- revise esta linha
        seq.append(seq[-1] + seq[-2])
    return seq

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert fibonacci(1) == [0],                        "caso 1 incorreto"
assert fibonacci(2) == [0, 1],                     "caso 2 incorreto"
assert fibonacci(5) == [0, 1, 1, 2, 3],            "caso 3 incorreto"
assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13], "caso 4 incorreto"
print("fibonacci(8) =", fibonacci(8))
print("Exercicio concluido!")
"""

# ── 031 ─────────────────────────────────────────────────────────────────────
files["exercicios/problemas/07_fibonacci/fibonacci_todo.py"] = """\
# TITULO: Fibonacci - Implementar
# TIPO: todo
# ID: 031

# =================================================================
# ENUNCIADO
# =================================================================
# A sequencia de Fibonacci e uma das mais famosas da matematica.
# Cada termo e a soma dos dois anteriores.
#
# Exemplos:
#   fibonacci(1) -> [0]
#   fibonacci(2) -> [0, 1]
#   fibonacci(5) -> [0, 1, 1, 2, 3]
#   fibonacci(8) -> [0, 1, 1, 2, 3, 5, 8, 13]
#
# Regras de negocio:
#   - fibonacci(0) retorna lista vazia []
#   - fibonacci(1) retorna [0]
#   - Os demais termos sao calculados como seq[-1] + seq[-2]
# =================================================================

def fibonacci(n):
    # TAREFA: Trate os casos base (n <= 0 e n == 1) e use um loop
    # para adicionar termos ate a lista ter exatamente n elementos.
    # Comece com seq = [0, 1] e acrescente um termo por iteracao.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert fibonacci(0) == [],                         "caso 1 incorreto"
assert fibonacci(1) == [0],                        "caso 2 incorreto"
assert fibonacci(2) == [0, 1],                     "caso 3 incorreto"
assert fibonacci(5) == [0, 1, 1, 2, 3],            "caso 4 incorreto"
assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13], "caso 5 incorreto"
print("fibonacci(10) =", fibonacci(10))
print("Exercicio concluido!")
"""

for rel, content in files.items():
    p = BASE / rel
    p.write_text(content, encoding="utf-8")
    print(f"  OK  {p.name}")

print(f"\nTotal: {len(files)} arquivos escritos")
