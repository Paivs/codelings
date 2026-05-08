# Codelings

<img width="610" height="343" alt="image" src="https://github.com/user-attachments/assets/6ac6b1ae-d02e-4061-9f48-47c16883f188" />

Learn programming by fixing bugs and completing code — inspired by [Rustlings](https://github.com/rust-lang/rustlings).

Works with any language: just have the runtime installed.

> **Português?** Veja o [README em português](README.pt.md).

---

## Supported Languages

| Language   | Extension | Required runtime  |
|------------|-----------|-------------------|
| Python     | `.py`     | `python3`         |
| JavaScript | `.js`     | `node`            |
| TypeScript | `.ts`     | `deno`            |
| Go         | `.go`     | `go`              |
| Rust       | `.rs`     | `rustc`           |
| Ruby       | `.rb`     | `ruby`            |
| Lua        | `.lua`    | `lua`             |
| C          | `.c`      | `gcc`             |
| Java       | `.java`   | `javac` + `java`  |

## Requirements

- Python 3.8 or higher (only to run the engine)
- The runtime for the language you want to practice

## Getting Started

```bash
python codelings.py
```

On **Windows**, double-click `start.windows.bat`.  
On **Linux/macOS**, run `start.linux.sh` or execute directly.

## How It Works

1. The menu lists available sections and topics
2. Select an exercise by number
3. Open the indicated file in your editor
4. Save the file — the result appears automatically on screen
5. Read the error, fix the code, save again
6. Repeat until the exercise passes
7. Press `[H]` to show the hint when there's an error
8. `Ctrl+C` to go back to the menu at any time

Progress is saved automatically in `.progress.json`.

## Exercise Types

### FIX

The file already contains code with an intentional bug. The goal is to find and fix the error.

```python
# title: Variables - Typo
# type: fix
# id: 001

name   = "Ana"
agge   = 22          # <- review this line
print(f"Age: {age}")
```

### TODO

The file contains partially implemented code. The goal is to fill in the missing parts.

```javascript
// title: Functions - Sum
// type: todo
// id: 042

function sum(a, b) {
    // TODO: implement here.
}
```

Each TODO exercise ends with a test section that verifies the implementation is correct.

## Interface Language

Codelings auto-detects your system locale. You can override it with `--lang`:

```bash
python codelings.py --lang en     # English
python codelings.py --lang pt_BR  # Portuguese
python codelings.py --lang es     # Spanish
python codelings.py --lang fr     # French
```

The chosen language is saved to `config.json` and persists across runs.

## Remote Exercises

You can sync exercises from a GitHub repository:

```bash
python codelings.py --remote https://github.com/user/repo
python codelings.py --sync
```

Once configured, use the `S` option in the main menu to sync at any time.

## Adding Exercises

Use the interactive CLI:

```bash
python novo_exercicio.py
```

The wizard guides you through language, category, type, title and content — and opens `$EDITOR` with the template already filled in.

Or create a file manually inside `exercises/<category>/<topic>/` following the header format (comment in the language syntax):

```
title: Exercise Name
type: fix   (or: todo)
id: 042
```

The engine discovers exercises automatically from the folder structure.

## Project Structure

```
codelings/
├── codelings.py           ← entry point (menus, UI)
├── novo_exercicio.py      ← CLI to create exercises
├── runner/
│   ├── runners.py         ← exercise execution engine
│   ├── sync.py            ← remote sync
│   ├── i18n.py            ← internationalization
│   ├── hints.json         ← hints per exercise
│   └── translations/
│       ├── en.json
│       ├── pt_BR.json
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

## Adding Support for a New Language

Add an entry to `RUNNERS` in `runner/runners.py`:

```python
# Interpreted language
".kt": {"cmd": ["kotlinc-jvm", "-script", "{file}"]},

# Compiled language (uses {bin} for the executable)
".cpp": {"compile": ["g++", "{file}", "-o", "{bin}"],
         "run":     ["{bin}"]},

# Compiled with output directory (uses {tmpdir} and {class})
".java": {"compile": ["javac", "-d", "{tmpdir}", "{file}"],
          "run":     ["java", "-ea", "-cp", "{tmpdir}", "Exercicio"]},
```

Also add the corresponding template in `novo_exercicio.py` in the `LINGUAGENS`, `DOC_PADRAO`, `_CORPO` and `_TESTES` dicts.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution guide.

## License

Distributed under the [GNU GPL v3](LICENSE).
