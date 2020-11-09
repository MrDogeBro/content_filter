"""
translations.py

Handles the translations of charaters in messages
"""

import re
from itertools import combinations
from unicodedata import normalize


def return_translated(translation_table: dict, string: str):
    translated_str = string.translate(translation_table['single'])
    translated_str = normalize('NFKD', translated_str).encode(
        'ascii', 'ignore').decode().lower()
    translated_str = re.compile('|'.join(map(re.escape, translation_table['multi']))).sub(
        lambda match: translation_table['multi'][match.group(0)], translated_str)

    return translated_str


def return_possibilities(message):
    chars = []
    chars_combined = []
    combos = []
    results = []

    found_statements = re.findall(r'(?<=\().+?(?=\))', message)

    for statement in found_statements:
        chars.append((statement[:1], statement[2:]))

    for index, char in enumerate(chars):
        for letter in char:
            letter += str(index)
            chars_combined.append(letter)

    for combo in combinations(chars_combined, len(chars)):
        found_dup = False

        for letter in combo:
            if [letter[1:2] for letter in combo].count(letter[1:2]) > 1:
                found_dup = True

        if not found_dup:
            combos.append(tuple(letter[:1] for letter in combo))

    for combo in combos:
        modified_message = message

        for index, letter in enumerate(combo):
            modified_message = modified_message.replace(
                '({found_statements})'.format(found_statements=found_statements[index]), letter, 1)

        results.append(modified_message)

    return results
