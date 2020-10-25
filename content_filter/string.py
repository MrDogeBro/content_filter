"""
translations.py

Handles the translations of charaters in messages
"""

import re
from unicodedata import normalize


def return_translated(translation_table: dict, string: str):
    translated_str = string.translate(translation_table['single'])
    translated_str = normalize('NFKD', translated_str).encode(
        'ascii', 'ignore').decode().lower()
    translated_str = re.compile('|'.join(map(re.escape, translation_table['multi']))).sub(
        lambda match: translation_table['multi'][match.group(0)], translated_str)

    return translated_str


def return_possibilities():
    pass
