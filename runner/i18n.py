import json
import locale
import os
from pathlib import Path

from runner import BOLD, DIM, CY, W, Y, RST

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
    slogan = t('banner.slogan')

    logo = [
        r"  ____          _      _ _               ",
        r" / ___|___   __| | ___| (_)_ __   __ _ ___",
        r"| |   / _ \ / _` |/ _ \ | | '_ \/ _` / __|",
        r"| |__| (_) | (_| |  __/ | | | | | (_| \__ " + "\\",
        r" \____\___/ \__,_|\___|_|_|_| |_|\__, |___/",
        r"                                  |___/    ",
    ]

    pad = 3
    inner = max(
        max(len(l) for l in logo) + pad * 2,
        len(slogan) + pad * 2,
        len(subtitle) + pad * 2,
    )

    cb = f'{BOLD}{CY}'

    def fence(left, right):
        return f'{cb}{left}{"═" * inner}{right}{RST}'

    def row(text, center=False, fg=''):
        s = text.center(inner) if center else (' ' * pad + text).ljust(inner)
        return f'{cb}║{RST}{fg}{s}{cb}║{RST}'

    blank = f'{cb}║{" " * inner}║{RST}'

    parts = [
        '',
        fence('╔', '╗'),
        blank,
        *[row(l, fg=f'{BOLD}{W}') for l in logo],
        blank,
        fence('╠', '╣'),
        row(slogan, center=True, fg=f'{BOLD}{Y}'),
        row(subtitle, center=True, fg=f'{DIM}{W}'),
        fence('╚', '╝'),
        '',
    ]
    return '\n'.join('  ' + p for p in parts)


def get_compact_banner() -> str:
    return f"\n  {BOLD}{CY}CODELINGS{RST}  {DIM}{'─' * 51}{RST}\n"


def setup_i18n(lang: str) -> None:
    global _LANG, _TRANSLATIONS
    _LANG = lang
    _TRANSLATIONS = _load_translations(lang)
