import hashlib
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

from runner import BASE, R, G, Y, CY, BOLD, RST
from runner.i18n import t

CONFIG_FILE = BASE / 'config.json'
_RUNNER_DIR = Path(__file__).parent


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
    url = url.rstrip('/')
    m = re.search(r'github\.com[:/]([^/]+)/([^/.]+)', url)
    if not m:
        raise ValueError(t('error.invalid_url', url=url))
    repo = m.group(2)
    if repo.endswith('.git'):
        repo = repo[:-4]
    return m.group(1), repo


def sync_from_remote(cfg: dict | None = None, verbose: bool = True) -> bool:
    if cfg is None:
        cfg = _load_config()
    remote_url = cfg.get('remote_url', '')
    if not remote_url:
        print(f"\n  {R}{t('sync.no_remote')}{RST}")
        print(f"  {t('sync.use_remote')}\n")
        return False

    branch = cfg.get('branch', 'main')
    try:
        owner, repo = _parse_github_url(remote_url)
    except ValueError as e:
        print(f"\n  {R}{e}{RST}\n")
        return False

    api_url = (
        f"https://api.github.com/repos/{owner}/{repo}"
        f"/git/trees/{branch}?recursive=1"
    )
    if verbose:
        print(f"\n  {CY}{t('sync.syncing', owner=owner, repo=repo, branch=branch)}{RST}")

    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'codelings'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            tree = json.loads(resp.read().decode())['tree']
    except urllib.error.HTTPError as e:
        print(f"  {R}{t('sync.http_error', code=e.code, reason=e.reason)}{RST}")
        return False
    except Exception as e:
        print(f"  {R}{t('sync.conn_error', e=e)}{RST}")
        return False

    raw_base = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}"
    to_sync = [
        item for item in tree
        if item['type'] == 'blob'
        and (
            item['path'].startswith('exercises/')
            or item['path'].startswith('exercicios/')  # legacy remote repos
            or item['path'] == 'hints.json'
        )
    ]

    updated = skipped = errors = 0
    for item in to_sync:
        path = item['path']
        if path == 'hints.json':
            local = _RUNNER_DIR / 'hints.json'
        else:
            normalized = path.replace('exercicios/', 'exercises/', 1)
            local = BASE / normalized
        try:
            req = urllib.request.Request(
                f"{raw_base}/{path}", headers={'User-Agent': 'codelings'}
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
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
