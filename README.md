# Pythonlings

Aprenda Python corrigindo erros e completando trechos de código — inspirado no [Rustlings](https://github.com/rust-lang/rustlings).

## Requisitos

- Windows 11
- Python 3.8 ou superior
- Nenhuma dependência externa

## Como iniciar

Clique duas vezes em `start.bat`, ou execute no terminal:

```
python pythonlings.py
```

## Como funciona

1. O menu lista as partes e os tópicos disponíveis
2. Selecione um exercício pelo número
3. Abra o arquivo indicado no seu editor preferido
4. Salve o arquivo — o resultado aparece automaticamente na tela
5. Interprete o erro, corrija o código, salve novamente
6. Repita até o exercício passar
7. `Ctrl+C` para voltar ao menu a qualquer momento

O progresso é salvo automaticamente em `.progress.json`.

## Tipos de exercício

### FIX

O arquivo já contém código com um bug intencional. O objetivo é encontrar e corrigir o erro.

```python
# TITLE: Variaveis - Erro de Digitacao
# TYPE: fix
# DESCRIPTION: Ha um erro de digitacao no nome de uma variavel.
# HINT: Python diferencia maiusculas de minusculas.

nome = "Ana"
iddade = 22          # <- bug aqui

print(f"Idade: {idade}")
```

O exercício é concluído quando o código roda sem erros.

### TODO

O arquivo contém código parcialmente implementado com marcadores `# TODO:`. O objetivo é preencher os trechos que faltam.

```python
# TITLE: Funcoes - Calculadora Simples
# TYPE: todo

def somar(a, b):
    # TODO: Retorne a soma de a e b
    pass
```

Cada exercício TODO tem uma seção de validação ao final com `assert`s que verificam se a implementação está correta. O exercício é concluído quando todas as asserções passam.

## Exercícios

### Conceitual

| Tópico        | FIX | TODO |
|---------------|-----|------|
| Variáveis     | 2   | 1    |
| Tipos         | 1   | 1    |
| Strings       | 1   | 1    |
| Listas        | 1   | 1    |
| Dicionários   | 1   | 1    |
| Condicionais  | 1   | 1    |
| Loops         | 1   | 1    |
| Funções       | 1   | 1    |

### Problemas

| Tópico      | Exercícios                              |
|-------------|-----------------------------------------|
| Clássicos   | FizzBuzz, Fibonacci, Palíndromo (FIX)   |
| Algoritmos  | Two Sum, Longest Common Prefix, Inverter Palavras (FIX) |

## Adicionando exercícios

Crie um arquivo `.py` dentro de `exercises/<parte>/<topico>/` seguindo o formato de cabeçalho:

```python
# TITLE: Nome do Exercício
# TYPE: fix        # ou: todo
# DESCRIPTION: Uma linha descrevendo o que o aluno deve fazer.
# HINT: Dica opcional exibida quando há erro.

# ... código do exercício
```

Para exercícios **TODO**, termine o arquivo com uma seção de validação usando `assert`:

```python
# --- Validacao (nao modifique abaixo) ---
assert resultado == esperado, f"Esperado {esperado}, obtido {resultado}"
print("Exercicio concluido!")
```

O sistema descobre exercícios automaticamente pela estrutura de pastas — não é necessário registrá-los em nenhum arquivo de configuração.

## Estrutura de pastas

```
pythonlings/
├── pythonlings.py
├── start.bat
└── exercises/
    ├── conceitual/
    │   ├── 01_variaveis/
    │   ├── 02_tipos/
    │   ├── 03_strings/
    │   ├── 04_listas/
    │   ├── 05_dicionarios/
    │   ├── 06_condicionais/
    │   ├── 07_loops/
    │   └── 08_funcoes/
    └── problemas/
        ├── 01_classicos/
        └── 02_algoritmos/
```
