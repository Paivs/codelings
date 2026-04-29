# Guia de Criacao de Exercicios — Pythonlings

Este documento define as convencoes obrigatorias para criar e manter exercicios.
Qualquer agente ou colaborador deve segui-lo antes de escrever ou revisar um exercicio.

---

## Estrutura de diretorios

```
exercicios/
├── conceitual/          # Conceitos basicos da linguagem
│   ├── 01_variaveis/
│   ├── 02_tipos/
│   ├── 03_strings/
│   ├── 04_listas/
│   ├── 05_dicionarios/
│   ├── 06_condicionais/
│   ├── 07_loops/
│   └── 08_funcoes/
└── problemas/           # Algoritmos e problemas classicos
    ├── 01_palindromo/
    ├── 02_anagrama/
    ├── 03_prefixo_comum/
    ├── 04_two_sum/
    ├── 05_mover_zeros/
    ├── 06_fizzbuzz/
    └── 07_fibonacci/
```

Sempre use `exercicios/` (portugues). Nunca `exercises/`.

---

## Nomenclatura de arquivos

| Tipo      | Padrao             | Exemplo               |
|-----------|--------------------|-----------------------|
| FIX       | `nome_fix.py`      | `palindrome_fix.py`   |
| TODO      | `nome_todo.py`     | `two_sum_todo.py`     |
| Topico    | `NN_nome/`         | `01_palindromo/`      |

---

## Cabecalho obrigatorio

Todo exercicio comeca com exatamente estas tres linhas:

```python
# TITULO: Nome descritivo do exercicio
# TIPO: fix        # ou: todo
# ID: NNN          # numero unico sequencial de 3 digitos
```

Termos em portugues: `TITULO`, `TIPO`. Nunca `TITLE`, `TYPE`.

---

## Estrutura do arquivo

### Exercicio FIX

```python
# TITULO: ...
# TIPO: fix
# ID: NNN

# =================================================================
# ENUNCIADO
# =================================================================
# Contexto narrativo do problema (uma ou duas frases).
#
# O que o aluno deve fazer:
# - Encontrar e corrigir o bug no codigo abaixo.
# =================================================================

[codigo com bug — marque a linha suspeita com "# <- revise esta linha"]

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert ..., "mensagem generica"
print("Exercicio concluido!")
```

### Exercicio TODO

```python
# TITULO: ...
# TIPO: todo
# ID: NNN

# =================================================================
# ENUNCIADO
# =================================================================
# Contexto narrativo do problema.
#
# Exemplos:
#   funcao(entrada1) -> saida1
#   funcao(entrada2) -> saida2
#
# Regras de negocio:
#   - Regra 1
#   - Regra 2
# =================================================================

def funcao(params):
    # TAREFA: Uma descricao clara e completa do que implementar.
    # Inclua o algoritmo sugerido quando necessario.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert funcao(entrada1) == saida1, "caso 1 incorreto"
assert funcao(entrada2) == saida2, "caso 2 incorreto"
print("Exercicio concluido!")
```

---

## Regras obrigatorias

### 1. Um unico TAREFA por exercicio
Nunca use multiplos comentarios `# TAREFA:` no mesmo arquivo.
Se o exercicio tem multiplas funcoes, coloque o `# TAREFA:` antes da primeira
e descreva todas no mesmo bloco.

### 2. Separacao visual clara
Sempre use os blocos `# ===` para delimitar `ENUNCIADO` e `TESTES`.
O codigo fica entre os dois blocos, sem delimitador proprio.

### 3. Sem solucoes nos asserts
**Errado:**
```python
assert total == sum(estoque.values()), f"esperado {sum(estoque.values())}"
```
**Certo:**
```python
assert total == 37, "total incorreto"
```
Pre-calcule os valores esperados. Nunca coloque expressoes ou f-strings
que revelem a logica da solucao nas mensagens de erro.

### 4. Valores fixos nos testes
Use sempre valores literais e pre-calculados:
```python
assert numeros == [1, 3, 5, 7, 8, 9], "lista incorreta"   # correto
assert numeros == sorted(numeros), "..."                    # errado
```

### 5. Bugs discretos nos FIX
Marque a linha com bug usando `# <- revise esta linha`.
Nao explique o bug no comentario. O aluno deve descobri-lo.

### 6. ENUNCIADO com contexto real
Coloque uma narrativa ou caso de uso, nao apenas instrucoes tecnicas.
```
# Um sistema escolar exibe dados de alunos, mas...   (bom)
# Corrija o codigo abaixo para nao dar erro.         (ruim)
```

### 7. Exemplos obrigatorios nos TODO
Inclua sempre 2-3 exemplos no bloco ENUNCIADO com entrada e saida.

---

## Terminologia (sempre em portugues nos arquivos)

| Ingles       | Portugues nos arquivos |
|--------------|------------------------|
| `exercises/` | `exercicios/`          |
| `# TODO:`    | `# TAREFA:`            |
| `# TITLE:`   | `# TITULO:`            |
| `# TYPE:`    | `# TIPO:`              |
| hint         | dica (apenas no terminal e hints.json) |

---

## IDs

- Conceitual: 001 a 017
- Problemas:  018 a 031
- Ao adicionar novos exercicios, use o proximo ID disponivel.
- IDs sao permanentes e nunca reutilizados.

---

## Dicas (hints.json)

Ficam em `hints.json` na raiz, indexadas pelo caminho relativo com `/`:

```json
{
  "exercicios/conceitual/01_variaveis/var01_fix.py": "Dica aqui..."
}
```

- Exibidas so quando o aluno pressiona `h` no terminal.
- Devem apontar uma direcao sem revelar a solucao completa.

---

## Checklist antes de commitar um exercicio

- [ ] Cabecalho tem TITULO, TIPO e ID
- [ ] Bloco ENUNCIADO presente com contexto narrativo
- [ ] Bloco TESTES presente com a linha `(nao modifique abaixo)`
- [ ] Apenas um `# TAREFA:` (TODO) ou `# <- revise esta linha` (FIX)
- [ ] Asserts com mensagens genericas e valores fixos pre-calculados
- [ ] Dica adicionada em `hints.json`
- [ ] Exercicio falha antes da correcao e passa depois
