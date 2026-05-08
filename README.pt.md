# Codelings

<img width="610" height="343" alt="image" src="https://github.com/user-attachments/assets/6ac6b1ae-d02e-4061-9f48-47c16883f188" />

Aprenda programação corrigindo erros e completando trechos de código — inspirado no [Rustlings](https://github.com/rust-lang/rustlings).

Funciona com qualquer linguagem: basta ter o runtime instalado.

> **English?** See the [English README](README.md).

---

## Linguagens Suportadas

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

## Como Iniciar

```bash
python codelings.py
```

No **Windows**, clique duas vezes em `start.windows.bat`.  
No **Linux/macOS**, use `start.linux.sh` ou execute diretamente.

## Como Funciona

1. O menu lista as partes e os tópicos disponíveis
2. Selecione um exercício pelo número
3. Abra o arquivo indicado no seu editor preferido
4. Salve o arquivo — o resultado aparece automaticamente na tela
5. Interprete o erro, corrija o código, salve novamente
6. Repita até o exercício passar
7. Pressione `[H]` para exibir a dica quando houver erro
8. `Ctrl+C` para voltar ao menu a qualquer momento

O progresso é salvo automaticamente em `.progress.json`.

## Tipos de Exercício

### FIX

O arquivo já contém código com um bug intencional. O objetivo é encontrar e corrigir o erro.

```python
# titulo: Variaveis - Erro de Digitacao
# tipo: fix
# id: 001

nome   = "Ana"
iddade = 22          # <- revise esta linha
print(f"Idade: {idade}")
```

### TODO

O arquivo contém código parcialmente implementado. O objetivo é preencher os trechos que faltam.

```javascript
// titulo: Funcoes - Somar
// tipo: todo
// id: 042

function somar(a, b) {
    // TODO: implemente aqui.
}
```

Cada exercício TODO termina com uma seção de testes que verifica se a implementação está correta.

## Idioma da Interface

O Codelings detecta automaticamente o locale do seu sistema. Você pode sobrescrever com `--lang`:

```bash
python codelings.py --lang pt_BR  # Português
python codelings.py --lang en     # English
python codelings.py --lang es     # Español
python codelings.py --lang fr     # Français
```

O idioma escolhido é salvo em `config.json` e persiste entre as sessões.

## Exercícios Remotos

Você pode sincronizar exercícios de um repositório GitHub:

```bash
python codelings.py --remote https://github.com/usuario/repo
python codelings.py --sync
```

Depois de configurado, use a opção `S` no menu principal para sincronizar a qualquer momento.

## Adicionando Exercícios

Use o CLI interativo:

```bash
python runner/novo_exercicio.py
```

O assistente guia você por linguagem, categoria, tipo, título e conteúdo — e abre o `$EDITOR` com o template já preenchido.

Ou crie manualmente um arquivo dentro de `exercises/<categoria>/<topico>/` seguindo o formato de cabeçalho (comentário na sintaxe da linguagem):

```
titulo: Nome do Exercício
tipo: fix   (ou: todo)
id: 042
```

O motor descobre exercícios automaticamente pela estrutura de pastas.

## Estrutura de Pastas

```
codelings/
├── codelings.py           ← entry point (menus, interface)
├── novo_exercicio.py      ← CLI para criar exercícios
├── runner/
│   ├── runners.py         ← motor de execução dos exercícios
│   ├── sync.py            ← sincronização remota
│   ├── i18n.py            ← internacionalização
│   ├── hints.json         ← dicas por exercício
│   └── translations/
│       ├── pt_BR.json
│       ├── en.json
│       ├── es.json
│       └── fr.json
└── exercises/
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

## Adicionando Suporte a uma Nova Linguagem

Adicione uma entrada em `RUNNERS` no `runner/runners.py`:

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

Adicione também o template correspondente em `novo_exercicio.py` nos dicionários `LINGUAGENS`, `DOC_PADRAO`, `_CORPO` e `_TESTES`.

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para o guia completo de contribuição.

## Licença

Distribuído sob a [GNU GPL v3](LICENSE).
