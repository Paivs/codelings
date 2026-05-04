# Codelings

<img width="610" height="343" alt="image" src="https://github.com/user-attachments/assets/6ac6b1ae-d02e-4061-9f48-47c16883f188" />


Aprenda programação corrigindo erros e completando trechos de código — inspirado no [Rustlings](https://github.com/rust-lang/rustlings).

Funciona com qualquer linguagem: basta ter o runtime instalado.

## Linguagens suportadas

| Linguagem  | Extensão | Runtime necessário |
|------------|----------|--------------------|
| Python     | `.py`    | `python3`          |
| JavaScript | `.js`    | `node`             |
| TypeScript | `.ts`    | `deno`             |
| Go         | `.go`    | `go`               |
| Rust       | `.rs`    | `rustc`            |
| Ruby       | `.rb`    | `ruby`             |
| Lua        | `.lua`   | `lua`              |
| C          | `.c`     | `gcc`              |
| Java       | `.java`  | `javac` + `java`   |

## Requisitos

- Python 3.8 ou superior (apenas para rodar o motor)
- O runtime da linguagem que você quer praticar

## Como iniciar

```bash
python codelings.py
```

No Windows, clique duas vezes em `start.bat`.  
No Linux/macOS, você pode usar `start.sh` ou executar diretamente.

## Como funciona

1. O menu lista as partes e os tópicos disponíveis
2. Selecione um exercício pelo número
3. Abra o arquivo indicado no seu editor preferido
4. Salve o arquivo — o resultado aparece automaticamente na tela
5. Interprete o erro, corrija o código, salve novamente
6. Repita até o exercício passar
7. `[H]` para exibir a dica quando houver erro
8. `Ctrl+C` para voltar ao menu a qualquer momento

O progresso é salvo automaticamente em `.progress.json`.

## Tipos de exercício

### FIX

O arquivo já contém código com um bug intencional. O objetivo é encontrar e corrigir o erro.

```python
# TITULO: Variaveis - Erro de Digitacao
# TIPO: fix
# ID: 001

nome   = "Ana"
iddade = 22          # <- revise esta linha
print(f"Idade: {idade}")
```

### TODO

O arquivo contém código parcialmente implementado. O objetivo é preencher os trechos que faltam.

```javascript
// TITULO: Funcoes - Somar
// TIPO: todo
// ID: 042

function somar(a, b) {
    // TAREFA: implemente aqui.
}
```

Cada exercício TODO termina com uma seção de testes que verifica se a implementação está correta.

## Adicionando exercícios

Use o CLI interativo:

```bash
python novo_exercicio.py
```

O assistente guia você por linguagem, categoria, tipo, título e conteúdo — e abre o `$EDITOR` com o template já preenchido.

Ou crie manualmente um arquivo dentro de `exercicios/<categoria>/<topico>/` seguindo o formato de cabeçalho (comentário na sintaxe da linguagem):

```
TITULO: Nome do Exercício
TIPO: fix   (ou: todo)
ID: 042
```

O sistema descobre exercícios automaticamente pela estrutura de pastas.

## Estrutura de pastas

```
codelings/
├── codelings.py          ← motor principal
├── novo_exercicio.py     ← CLI para criar exercícios
├── hints.json            ← dicas por arquivo
└── exercicios/
    ├── conceitual/
    │   ├── 01_variaveis/
    │   │   ├── var01_fix.py
    │   │   └── var02_todo.js
    │   └── ...
    └── problemas/
        ├── 01_palindromo/
        │   └── palindrome_todo.py
        └── ...
```

## Adicionando suporte a uma nova linguagem

Adicione uma entrada em `RUNNERS` no `codelings.py`:

```python
# Linguagem interpretada
".kt": {"cmd": ["kotlinc-jvm", "-script", "{file}"]},

# Linguagem compilada (usa {bin} para o executável)
".cpp": {"compile": ["g++", "{file}", "-o", "{bin}"],
         "run":     ["{bin}"]},

# Linguagem compilada com diretório de saída (usa {tmpdir} e {class})
".java": {"compile": ["javac", "-d", "{tmpdir}", "{file}"],
          "run":     ["java", "-ea", "-cp", "{tmpdir}", "Exercicio"]},
```

E adicione o template correspondente em `novo_exercicio.py` nos dicionários `LINGUAGENS`, `DOC_PADRAO`, `_CORPO` e `_TESTES`.

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para o guia completo de contribuição.

## Licença

Distribuído sob a [GNU GPL v3](LICENSE).
