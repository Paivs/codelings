import json
import locale
import os
from pathlib import Path

from runner import BOLD, CY, RST

_LANG: str = 'pt_BR'
_TRANSLATIONS: dict = {}

_TRANSLATIONS_DIR = Path(__file__).parent / 'translations'


def _detect_lang(cfg: dict) -> str:
    if 'lang' in cfg:
        return cfg['lang']
    try:
        loc = locale.getdefaultlocale()[0] or ''
    except Exception:
        loc = os.environ.get('LANG', '')
    if loc.startswith('pt'):
        return 'pt_BR'
    if loc.startswith('es'):
        return 'es'
    if loc.startswith('fr'):
        return 'fr'
    return 'en'


def _load_translations(lang: str) -> dict:
    path = _TRANSLATIONS_DIR / f'{lang}.json'
    if not path.exists():
        path = _TRANSLATIONS_DIR / 'pt_BR.json'
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return {}


def t(key: str, **kwargs) -> str:
    text = _TRANSLATIONS.get(key, key)
    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, ValueError):
            return text
    return text


def get_banner() -> str:
    subtitle = t('banner.subtitle')
    inner = f"    CODELINGS  -  {subtitle}"
    padded = inner.ljust(50)
    return (
        f"\n{BOLD}{CY}"
        "  ╔══════════════════════════════════════════════════╗\n"
        "  ║                                                  ║\n"
        f"  ║{padded}║\n"
        "  ║                                                  ║\n"
        "  ╚══════════════════════════════════════════════════╝\n"
        f"{RST}"
    )


def setup_i18n(lang: str) -> None:
    global _LANG, _TRANSLATIONS
    _LANG = lang
    _TRANSLATIONS = _load_translations(lang)
