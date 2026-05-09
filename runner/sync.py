import hashlib
import json
import urllib.error
from pathlib import Path

from runner import BASE, R, G, Y, CY, BOLD, RST
from runner.i18n import t
from runner.providers import detect_provider, GithubProvider

CONFIG_FILE = BASE / 'config.json'
_RUNNER_DIR = Path(__file__).parent
DEFAULT_EXERCISES_REMOTE = 'https://github.com/Paivs/codelings-exercises-ptbr'


def _load_config() -> dict:
    try:
        return json.loads(CONFIG_FILE.read_text(encoding='utf-8'))
    except Exception:
        return {}


def _save_config(cfg: dict) -> None:
    CONFIG_FILE.write_text(
        json.dumps(cfg, indent=2, ensure_ascii=False) + '\n', encoding='utf-8'
    )


def _parse_github_url(url: str) -> tuple[str, str]:
    """Mantido para compatibilidade com código existente."""
    try:
        p = GithubProvider(url)
        return p.owner, p.repo
    except Exception:
        raise ValueError(t('error.invalid_url', url=url))


def sync_from_remote(cfg: dict | None = None, verbose: bool = True) -> bool:
    if cfg is None:
        cfg = _load_config()
    remote_url = cfg.get('remote_url', '') or DEFAULT_EXERCISES_REMOTE

    branch = cfg.get('branch', 'main')
    try:
        provider = detect_provider(remote_url, branch)
    except ValueError as e:
        print(f"\n  {R}{e}{RST}\n")
        return False

    if verbose:
        print(f"\n  {CY}{t('sync.syncing', owner=provider.owner, repo=provider.repo, branch=branch)}{RST}")

    try:
        paths = provider.list_files()
    except urllib.error.HTTPError as e:
        print(f"  {R}{t('sync.http_error', code=e.code, reason=e.reason)}{RST}")
        return False
    except Exception as e:
        print(f"  {R}{t('sync.conn_error', e=e)}{RST}")
        return False

    updated = skipped = errors = 0
    for path in paths:
        if path == 'hints.json':
            local = _RUNNER_DIR / 'hints.json'
        else:
            normalized = path.replace('exercicios/', 'exercises/', 1)
            local = BASE / normalized
        try:
            content = provider.fetch_file(path)
        except Exception as e:
            if verbose:
                print(f"  {Y}  ! {path}: {e}{RST}")
            errors += 1
            continue

        remote_sha = hashlib.sha256(content).hexdigest()
        if local.exists() and hashlib.sha256(local.read_bytes()).hexdigest() == remote_sha:
            skipped += 1
            continue

        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(content)
        updated += 1
        if verbose:
            print(f"  {G}  ✓ {path}{RST}")

    if verbose:
        status = f"{G}{BOLD}" if not errors else f"{Y}{BOLD}"
        if errors:
            msg = t('sync.done_errors', updated=updated, skipped=skipped, errors=errors)
        else:
            msg = t('sync.done_ok', updated=updated, skipped=skipped)
        print(f"\n  {status}{msg}{RST}\n")
    return True
