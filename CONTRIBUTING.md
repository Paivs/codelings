# Como Contribuir — Codelings

Obrigado pelo interesse em contribuir! Este guia cobre as três formas principais de contribuição: novos exercícios, novas linguagens e melhorias no motor.

---

## Exercícios

Os exercícios ficam em um repositório separado:  
**[codelings-exercises-ptbr](https://github.com/Paivs/codelings-exercises-ptbr)**

Para contribuir com exercícios, faça um fork desse repositório (não deste).

### Via CLI (recomendado)

```bash
python runner/novo_exercicio.py
```

O assistente guia você por linguagem, categoria, tipo, título e conteúdo — e abre o `$EDITOR` com o template já preenchido.

### Manualmente

Crie um arquivo em `exercises/<categoria>/<NN_topico>/` seguindo o formato abaixo. Use o caractere de comentário da linguagem (`#`, `//` ou `--`).

#### Exercício FIX

```python
# titulo: Variaveis - Erro de Digitacao
# tipo: fix
# id: 032

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
// titulo: Funcoes - Somar
// tipo: todo
// id: 033

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

- Cabeçalho com `titulo`, `tipo` e `id` (use `runner/novo_exercicio.py` para gerar o próximo ID automaticamente)
- Exercícios de `problemas` são sempre `TODO` e um por tópico
- Asserts com valores literais pré-calculados — nunca expressões que revelem a solução
- Marque a linha com bug com `# <- revise esta linha` nos FIX
- Adicione uma dica em `runner/hints.json` (pode incluir link da documentação)
- O exercício deve **falhar** antes da correção e **passar** depois

---

## Nova linguagem

### 1. Adicionar o runner em `runner/runners.py`

```python
# Linguagem interpretada
".rb": {"cmd": ["ruby", "{file}"]},

# Linguagem compilada com binário
".rs": {
    "compile": ["rustc", "{file}", "-o", "{bin}"],
    "run":     ["{bin}"],
},

# Linguagem compilada com diretório de saída
".java": {
    "compile": ["javac", "-d", "{tmpdir}", "{file}"],
    "run":     ["java", "-ea", "-cp", "{tmpdir}", "Exercicio"],
},
```

Placeholders disponíveis: `{file}`, `{bin}`, `{tmpdir}`, `{class}`.

### 2. Adicionar label e doc em `runner/runners.py`

```python
LANG_LABEL[".rb"] = "Ruby"
DOC_PADRAO[".rb"]  = "https://ruby-doc.org/"
```

### 3. Adicionar templates em `runner/novo_exercicio.py`

```python
LINGUAGENS["Ruby"] = {"ext": ".rb", "comment": "#", "compiled": False}

_CORPO[".rb"] = {
    "fix":  "def minha_funcao(x)\n  x + 1  # <- revise esta linha\nend\n",
    "todo": "def minha_funcao(x)\n  # TAREFA: implemente aqui.\nend\n",
}

_TESTES[".rb"] = 'raise "caso 1 incorreto" unless minha_funcao(1) == 2\nputs "Exercicio concluido!"\n'
```

### 4. Testar

Crie um exercício de teste com `python runner/novo_exercicio.py`, resolva-o manualmente e confirme que passa no motor.

---

## Motor

Os arquivos do motor ficam em `runner/`:

| Arquivo | Responsabilidade |
|---|---|
| `runners.py` | Execução dos exercícios (RUNNERS, DOC_PADRAO, LANG_LABEL) |
| `sync.py` | Orquestração do sync remoto |
| `providers.py` | Providers GitHub / GitLab / Gitea |
| `i18n.py` | Internacionalização e banner |
| `animations/` | Animações ASCII easter eggs |

- Abra uma issue descrevendo a mudança antes de implementar algo grande
- PRs com alterações no motor devem incluir testes manuais documentados
- Mantenha zero dependências externas — apenas stdlib Python

### Adicionando um novo provider

Implemente a classe em `runner/providers.py` herdando de `Provider`:

```python
class MeuProvider(Provider):
    def _parse(self, url: str) -> tuple[str, str]:
        # extrai owner e repo da URL
        ...

    def list_files(self) -> list[str]:
        # retorna paths relativos dos arquivos de exercício
        ...

    def fetch_file(self, path: str) -> bytes:
        # baixa e retorna o conteúdo de um arquivo
        ...
```

Depois registre-o em `detect_provider()`.

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
python runner/gen_exercicios.py
```

O script consulta o repositório remoto, compara checksums e restaura apenas os arquivos que divergirem.
