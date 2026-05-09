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
- Internet connection on first run (to download exercises)

## Getting Started

```bash
python codelings.py
```

On first run, exercises are downloaded automatically from the default repository.  
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
8. Press `[E]` to open the file in your editor directly from the terminal
9. `Ctrl+C` to go back to the menu at any time

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

## Editor

By default, `[E]` opens the current exercise in VS Code. To use a different editor:

```bash
python codelings.py --editor vim
python codelings.py --editor nano
python codelings.py --editor subl
```

The preference is saved to `config.json`.

## Remote Exercises

Exercises are stored in a separate repository and downloaded automatically.  
The default source is [codelings-exercises-ptbr](https://github.com/Paivs/codelings-exercises-ptbr).

To use a different exercise repository:

```bash
python codelings.py --remote https://github.com/user/repo
python codelings.py --remote https://gitlab.com/user/repo
python codelings.py --remote https://git.yourcompany.com/user/repo
```

Supported providers: **GitHub**, **GitLab** (cloud and self-hosted), **Gitea / Forgejo** (self-hosted).  
The provider is detected automatically from the URL.

To sync at any time, use the `S` option in the main menu or:

```bash
python codelings.py --sync
```

## Adding Exercises

Use the interactive CLI:

```bash
python runner/novo_exercicio.py
```

The wizard guides you through language, category, type, title and content — and opens `$EDITOR` with the template already filled in.

Or create a file manually inside `exercises/<category>/<topic>/` following the header format (comment in the language syntax):

```
title: Exercise Name
type: fix   (or: todo)
id: 042
```

The engine discovers exercises automatically from the folder structure.

## Restoring Exercises

If an exercise was accidentally modified:

```bash
python runner/gen_exercicios.py
```

The script fetches the remote version, compares checksums, and restores only the files that differ.

## Project Structure

```
codelings/
├── codelings.py               ← entry point (menus, UI)
├── runner/
│   ├── __init__.py            ← ANSI constants, BASE path
│   ├── runners.py             ← exercise execution engine
│   ├── sync.py                ← remote sync orchestration
│   ├── providers.py           ← GitHub / GitLab / Gitea providers
│   ├── i18n.py                ← internationalization
│   ├── hints.json             ← hints per exercise (downloaded)
│   ├── novo_exercicio.py      ← CLI to create exercises
│   ├── gen_exercicios.py      ← exercise restore tool
│   ├── animations/            ← ASCII animation easter eggs
│   └── translations/
│       ├── en.json
│       ├── pt_BR.json
│       ├── es.json
│       └── fr.json
└── exercises/                 ← downloaded on first run (not versioned)
    ├── conceitual/
    │   ├── 01_variaveis/
    │   └── ...
    └── problemas/
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

Also add the corresponding template in `runner/novo_exercicio.py` in the `LINGUAGENS`, `DOC_PADRAO`, `_CORPO` and `_TESTES` dicts.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution guide.

## License

Distributed under the [GNU GPL v3](LICENSE).
