"""Providers de exercícios remotos.

Cada provider sabe como listar e baixar arquivos de um serviço de hospedagem
específico. A função `detect_provider` escolhe automaticamente pelo padrão da URL.
"""

import json
import re
import urllib.error
import urllib.parse
import urllib.request


_EXERCISE_PREFIXES = ('exercises/', 'exercicios/')
_HINTS_PATH = 'hints.json'
_UA = {'User-Agent': 'codelings'}


def _fetch(url: str, timeout: int = 15) -> bytes:
    req = urllib.request.Request(url, headers=_UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _is_exercise_file(path: str) -> bool:
    return any(path.startswith(p) for p in _EXERCISE_PREFIXES) or path == _HINTS_PATH


class Provider:
    def __init__(self, url: str, branch: str = 'main'):
        self.branch = branch
        self.owner, self.repo = self._parse(url)

    def _parse(self, url: str) -> tuple[str, str]:
        raise NotImplementedError

    def list_files(self) -> list[str]:
        """Retorna paths relativos dos arquivos de exercício no repositório."""
        raise NotImplementedError

    def fetch_file(self, path: str) -> bytes:
        raise NotImplementedError

    def label(self) -> str:
        return f"{self.owner}/{self.repo}"


class GithubProvider(Provider):
    def _parse(self, url: str) -> tuple[str, str]:
        url = url.rstrip('/')
        m = re.search(r'github\.com[:/]([^/]+)/([^/.]+)', url)
        if not m:
            raise ValueError(f"URL GitHub inválida: {url}")
        repo = m.group(2).removesuffix('.git')
        return m.group(1), repo

    def list_files(self) -> list[str]:
        api = (
            f"https://api.github.com/repos/{self.owner}/{self.repo}"
            f"/git/trees/{self.branch}?recursive=1"
        )
        tree = json.loads(_fetch(api))['tree']
        return [item['path'] for item in tree
                if item['type'] == 'blob' and _is_exercise_file(item['path'])]

    def fetch_file(self, path: str) -> bytes:
        url = f"https://raw.githubusercontent.com/{self.owner}/{self.repo}/{self.branch}/{path}"
        return _fetch(url)


class GitlabProvider(Provider):
    def __init__(self, url: str, branch: str = 'main'):
        m = re.match(r'(https?://[^/]+)', url)
        self.host = m.group(1) if m else 'https://gitlab.com'
        super().__init__(url, branch)

    def _parse(self, url: str) -> tuple[str, str]:
        url = url.rstrip('/')
        m = re.search(r'https?://[^/]+/([^/]+)/([^/.]+)', url)
        if not m:
            raise ValueError(f"URL GitLab inválida: {url}")
        return m.group(1), m.group(2).removesuffix('.git')

    @property
    def _project_id(self) -> str:
        return urllib.parse.quote(f"{self.owner}/{self.repo}", safe='')

    def list_files(self) -> list[str]:
        files, page = [], 1
        while True:
            api = (
                f"{self.host}/api/v4/projects/{self._project_id}/repository/tree"
                f"?recursive=true&ref={self.branch}&per_page=100&page={page}"
            )
            items = json.loads(_fetch(api))
            files += [i['path'] for i in items
                      if i['type'] == 'blob' and _is_exercise_file(i['path'])]
            if len(items) < 100:
                break
            page += 1
        return files

    def fetch_file(self, path: str) -> bytes:
        url = f"{self.host}/{self.owner}/{self.repo}/-/raw/{self.branch}/{path}"
        return _fetch(url)


class GiteaProvider(Provider):
    """Cobre Gitea e Forgejo (mesma API)."""

    def __init__(self, url: str, branch: str = 'main'):
        m = re.match(r'(https?://[^/]+)', url)
        self.host = m.group(1) if m else ''
        super().__init__(url, branch)

    def _parse(self, url: str) -> tuple[str, str]:
        url = url.rstrip('/')
        m = re.search(r'https?://[^/]+/([^/]+)/([^/.]+)', url)
        if not m:
            raise ValueError(f"URL Gitea/Forgejo inválida: {url}")
        return m.group(1), m.group(2).removesuffix('.git')

    def _branch_sha(self) -> str:
        api = f"{self.host}/api/v1/repos/{self.owner}/{self.repo}/branches/{self.branch}"
        data = json.loads(_fetch(api))
        return data['commit']['id']

    def list_files(self) -> list[str]:
        sha = self._branch_sha()
        api = (
            f"{self.host}/api/v1/repos/{self.owner}/{self.repo}"
            f"/git/trees/{sha}?recursive=true"
        )
        data = json.loads(_fetch(api))
        return [item['path'] for item in data.get('tree', [])
                if item.get('type') == 'blob' and _is_exercise_file(item['path'])]

    def fetch_file(self, path: str) -> bytes:
        url = f"{self.host}/{self.owner}/{self.repo}/raw/branch/{self.branch}/{path}"
        return _fetch(url)


def detect_provider(url: str, branch: str = 'main') -> Provider:
    """Detecta o provider pelo padrão da URL."""
    if 'github.com' in url:
        return GithubProvider(url, branch)
    if re.search(r'gitlab\.', url):
        return GitlabProvider(url, branch)
    return GiteaProvider(url, branch)
