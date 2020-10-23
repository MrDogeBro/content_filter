"""
translations.py

Handles the translations of charaters in messages
"""

import re


def return_translated(translation_table: dict, string: str):
    translated_str = re.compile('|'.join(map(re.escape, translation_table['multi']))).sub(
        lambda match: translation_table['multi'][match.group(0)], string)
    translated_str = translated_str.translate(translation_table['single'])

    return translated_str
