# Como Contribuir — Codelings

Obrigado pelo interesse em contribuir! Este guia cobre as três formas principais de contribuição: novos exercícios, novas linguagens e melhorias no motor.

---

## Exercícios

### Via CLI (recomendado)

```bash
python novo_exercicio.py
```

O assistente guia você por linguagem, categoria, tipo, título e conteúdo — e abre o `$EDITOR` com o template já preenchido.

### Manualmente

Crie um arquivo em `exercicios/<categoria>/<NN_topico>/` seguindo o formato abaixo. Use o caractere de comentário da linguagem (`#`, `//` ou `--`).

#### Exercício FIX

```python
# TITULO: Variaveis - Erro de Digitacao
# TIPO: fix
# ID: 032

# =================================================================
# ENUNCIADO
# =================================================================
# Contexto narrativo do problema.
# O que o aluno deve fazer para corrigir.
# =================================================================

def funcao(x):
    return x + 1   # <- revise esta linha

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert funcao(2) == 4, "caso incorreto"
print("Exercicio concluido!")
```

#### Exercício TODO

```javascript
// TITULO: Funcoes - Somar
// TIPO: todo
// ID: 033

// =================================================================
// ENUNCIADO
// =================================================================
// Contexto narrativo. Inclua sempre exemplos de entrada/saída
// e regras de negócio.
//
// Exemplos:
//   somar(2, 3) -> 5
//   somar(0, 1) -> 1
// =================================================================

function somar(a, b) {
    // TAREFA: implemente aqui.
}

// =================================================================
// TESTES (nao modifique abaixo)
// =================================================================
console.assert(somar(2, 3) === 5, "caso 1 incorreto");
console.log("Exercicio concluido!");
```

### Regras obrigatórias

- Cabeçalho com `TITULO`, `TIPO` e `ID` (próximo ID disponível — verifique com `python -c "import codelings; print(max(int(l.split()[-1]) for f in __import__('pathlib').Path('exercicios').rglob('*') if f.is_file() for l in f.read_text().splitlines()[:8] if 'ID:' in l) + 1)"` ou via `novo_exercicio.py`)
- Exercícios de `problemas` são sempre `TODO` e um por tópico
- Asserts com valores literais pré-calculados — nunca expressões que revelem a solução
- Marque a linha com bug com `# <- revise esta linha` nos FIX
- Adicione uma dica em `hints.json` (pode incluir link da documentação)
- O exercício deve **falhar** antes da correção e **passar** depois

Consulte [AGENTS.md](AGENTS.md) para o guia completo de convenções.

---

## Nova linguagem

### 1. Adicionar o runner em `codelings.py`

```python
# Linguagem interpretada
RUNNERS[".rb"] = {"cmd": ["ruby", "{file}"]}

# Linguagem compilada com binário
RUNNERS[".rs"] = {
    "compile": ["rustc", "{file}", "-o", "{bin}"],
    "run":     ["{bin}"],
}

# Linguagem compilada com diretório de saída
RUNNERS[".java"] = {
    "compile": ["javac", "-d", "{tmpdir}", "{file}"],
    "run":     ["java", "-ea", "-cp", "{tmpdir}", "Exercicio"],
}
```

Placeholders disponíveis: `{file}`, `{bin}`, `{tmpdir}`, `{class}`.

### 2. Adicionar label e doc em `codelings.py`

```python
LANG_LABEL[".rb"] = "Ruby"
DOC_PADRAO[".rb"] = "https://ruby-doc.org/"
```

### 3. Adicionar templates em `novo_exercicio.py`

```python
LINGUAGENS["Ruby"] = {"ext": ".rb", "comment": "#", "compiled": False}
DOC_PADRAO[".rb"]  = "https://ruby-doc.org/"

_CORPO[".rb"] = {
    "fix":  "def minha_funcao(x)\n  x + 1  # <- revise esta linha\nend\n",
    "todo": "def minha_funcao(x)\n  # TAREFA: implemente aqui.\nend\n",
}

_TESTES[".rb"] = 'raise "caso 1 incorreto" unless minha_funcao(1) == 2\nputs "Exercicio concluido!"\n'
```

### 4. Testar

Crie um exercício de teste com `python novo_exercicio.py`, resolva-o manualmente e confirme que passa no motor.

---

## Motor (`codelings.py`, `novo_exercicio.py`)

- Abra uma issue descrevendo a mudança antes de implementar algo grande
- PRs com alterações no motor devem incluir testes manuais documentados
- Mantenha zero dependências externas — apenas stdlib Python

---

## Fluxo de Pull Request

1. Faça um fork do repositório
2. Crie uma branch: `git checkout -b feat/minha-contribuicao`
3. Implemente e teste localmente
4. Commit com mensagem clara: `feat: adiciona suporte a Kotlin`
5. Abra o PR descrevendo o que foi adicionado e como testar

---

## Restaurar exercícios ao estado original

Se um exercício foi modificado acidentalmente:

```bash
python _gen_exercicios.py
```

O script consulta o repositório remoto, compara checksums e restaura apenas os arquivos que divergirem.
