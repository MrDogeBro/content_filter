"""
check.py

Checks message to see if they contain any words in the filter
"""

import json
import re

from content_filter.string import return_translated, return_possibilities


class Check:
    """Check object which checks a message and can return the results
    as either a list or a bool."""

    def __init__(self, message, exception_list, additional_list, custom_list, use_default_list, use_custom_file, translation_table, filter_file):
        self.message = message
        self._exception_list = exception_list
        self._additional_list = additional_list
        self._custom_list = custom_list
        self._use_default_list = use_default_list
        self._use_custom_file = use_custom_file
        self._translation_table = translation_table
        self._filter_file = filter_file

        self._check_results = self._check_message()

    @property
    def as_bool(self) -> bool:
        """Returns the results of the check as a bool."""

        return bool(self._check_results)

    @property
    def as_list(self) -> list:
        """Returns the results of the check as a list."""

        return self._check_results

    def _check_message(self) -> list:
        words_found = []
        filter_data = {}

        # sets up a var that will be used to look for words in that replaces all irregular charaters with the charater they might be used for as a bad word
        msg_content = return_translated(
            self._translation_table, self.message.lower())
        msg_combos = return_possibilities(msg_content)

        if self._use_default_list:
            # gets all of the words to filter for
            with open(self._filter_file) as f:
                filter_data = json.load(f)

        elif self._use_custom_file:
            filter_data = self._use_custom_file

        for index, combo in enumerate(msg_combos):
            if not self._custom_list:
                if filter_data['dontFilter'] is not None:
                    # goes through all of the words in the filter and checks if any are in the message
                    for word in filter_data['dontFilter']:
                        # checks for words that should not be filtered in teh message
                        if word in combo:
                            # gets rid of the words that shouldn't be filtered so that the filter wont find them
                            msg_combos[index] = msg_combos[index].replace(
                                word, '')

                else:
                    # gets default list of words
                    with open(self._filter_file) as f:
                        default_list = json.load(f)

                    # goes through all of the words in the filter and checks if any are in the message
                    for word in default_list['dontFilter']:
                        # checks for words that should not be filtered in the message
                        if word in combo:
                            # gets rid of the words that shouldn't be filtered so that the filter wont find them
                            msg_combos[index] = msg_combos[index].replace(
                                word, '')

            # goes through all of the words in the filter and checks if any are in the message
            for word in self._exception_list:
                if not self._custom_list:
                    # checks for words that should not be filtered in the message
                    for string in filter_data['mainFilter']:
                        if string['find'] in self._exception_list:
                            try:
                                filter_data['mainFilter'].pop(
                                    filter_data['mainFilter'].index(string))

                            except:
                                # gets rid of the words that shouldn't be filtered so that the filter wont find them
                                msg_combos[index] = msg_combos[index].replace(
                                    word, '')

                    # checks for words that should not be filtered in the message
                    for string in filter_data['conditionFilter']:
                        if string['find'] in self._exception_list:
                            try:
                                filter_data['conditionFilter'].pop(
                                    filter_data['conditionFilter'].index(string))

                            except:
                                # gets rid of the words that shouldn't be filtered so that the filter wont find them
                                msg_combos[index] = msg_combos[index].replace(
                                    word, '')

                    if word in combo:
                        msg_combos[index] = msg_combos[index].replace(word, '')

                else:
                    # checks for words that should not be filtered in the message
                    try:
                        self._custom_list.pop(word)

                    except:
                        # gets rid of the words that shouldn't be filtered so that the filter wont find them
                        msg_combos[index] = msg_combos[index].replace(word, '')

        for combo in msg_combos:
            if not self._custom_list:
                # goes through all of the words in the filter and checks if any are in the message
                for word in filter_data['mainFilter']:
                    word_found = [(m.start(), m.end()) for m in re.finditer(
                        '+[.!-]*'.join(c for c in word['find']), combo.replace(' ', ''))]

                    if (word_found):
                        words_found.append(
                            {'word': word['word'], 'censored': word['censored'], 'count': len(word_found), 'indexes': word_found})

                # goes through all of the words in the filter and checks if any are in the message
                for word in self._additional_list:
                    word_found = [(m.start(), m.end()) for m in re.finditer(
                        '+[.!-]*'.join(c for c in word), combo.replace(' ', ''))]

                    if (word_found):
                        words_found.append(
                            {'word': word, 'count': len(word_found), 'indexes': word_found})

                # goes through all of the words in the filter and checks if any are in the message
                for word in filter_data['conditionFilter']:
                    if word['require_space']:
                        condition_found = ' ' + \
                            word['find'] in combo or word['find'] in combo[:len(
                                word['find'])]

                        if condition_found:
                            word_found_regex = [(m.start(), m.end()) for m in re.finditer(
                                word['find'], combo)]
                            words_found.append(
                                {'word': word['word'], 'censored': word['censored'], 'count': len(word_found_regex), 'indexes': word_found_regex})
                    else:
                        condition_found = word['find'] in combo or word['find'] in combo[:len(
                            word['find'])]

                        if condition_found:
                            word_found_regex = [(m.start(), m.end()) for m in re.finditer(
                                word['find'], combo)]
                            words_found.append(
                                {'word': word['word'], 'censored': word['censored'], 'count': len(word_found_regex), 'indexes': word_found_regex})

            else:
                # goes through all of the words in the filter and checks if any are in the message
                for word in self._exception_list:
                    # checks for words that should not be filtered in teh message
                    try:
                        self._custom_list.pop(word)

                    except:
                        # gets rid of the words that shouldn't be filtered so that the filter wont find them
                        combo = combo.replace(word, '')

                # goes through all of the words in the filter and checks if any are in the message
                for word in self._custom_list:
                    word_found = [(m.start(), m.end()) for m in re.finditer(
                        '+[.!-]*'.join(c for c in word), combo.replace(' ', ''))]

                    if (word_found):
                        words_found.append(
                            {'word': word, 'count': len(word_found), 'indexes': word_found})

                # goes through all of the words in the filter and checks if any are in the message
                for word in self._additional_list:
                    word_found = [(m.start(), m.end()) for m in re.finditer(
                        '+[.!-]*'.join(c for c in word), combo.replace(' ', ''))]

                    if (word_found):
                        words_found.append(
                            {'word': word, 'count': len(word_found), 'indexes': word_found})

        to_remove: list = []

        for match in words_found:
            if [w['word'] for w in words_found].count(match['word']) > 1:
                if words_found.count(match) > 1 and to_remove.count(match) < (words_found.count(match) - 1):
                    to_remove.append(match)

                else:
                    index_len = ([i['count'] for i in words_found if i['word'] == match['word']], [
                        i for i in words_found if i['word'] == match['word']])

                    if index_len[1][index_len[0].index(max(index_len[0]))] != match and to_remove.count(match) < words_found.count(match):
                        to_remove.append(match)

        for rem in to_remove:
            words_found.remove(rem)

        return words_found

    def __repr__(self):
        return '<Check: message=\'{message}\'>'.format(message=self.message)
