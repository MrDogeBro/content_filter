"""
filter.py

The main file that is the hub of all operations
"""

import json
from pathlib import Path

from content_filter.check import Check
from content_filter.string import return_translated


class Filter:
    """The filter object which contains the filter settings,
    data, and functions.

    Paramaters:
    ----------
        Optional[list_file]:
            The path to a file that will be used as the filter
            list in place of the default filter

        Optional[word_list]:
            A list of words to be used as the filter in place
            of the default filter
    """

    def __init__(self, list_file=None, word_list=None):
        self.exception_list = []  # type: list
        self.additional_list = []  # type: list
        self.custom_list = [word.replace(' ', '') for word in word_list] if isinstance(
            word_list, list) else []
        self._use_default_list = True
        self._use_custom_file = False
        self.custom_json_file = None
        self._translation_table = None
        self._filter_file = Path.joinpath(
            Path(__file__).resolve().parent, 'data/filter.json')

        # ==== LOAD TRANSLATIONS ====

        translations_file = Path.joinpath(
            Path(__file__).resolve().parent, 'data/replacements.json')

        with open(translations_file) as f:
            loaded_translations = json.load(f)

        self._translation_table = {
            'single': str.maketrans(loaded_translations['single_char']),
            'multi': loaded_translations['multi_char']
        }

        # ==== CUSTOM FILE CHECK ====

        if list_file:
            if not Path(list_file).is_absolute():
                rel_list_file = Path.joinpath(Path.cwd(), list_file)

            self.custom_json_file = Path(
                rel_list_file if rel_list_file else list_file)

            with open(self.custom_json_file) as f:
                self._use_custom_file = json.load(f)

            self._use_default_list = False

        # ==== CUSTOM LIST CHECK ====

        if word_list and not isinstance(word_list, list):
            raise TypeError('word_list expects list but got ' +
                            str(type(word_list).__name__))

        # ==== CHECKING LISTS ====
        self._lists_to_lower()
        self._lists_translate()

    def _lists_to_lower(self) -> None:
        if self.custom_list:
            self.custom_list = [i.lower() for i in self.custom_list]

        self.exception_list = [i.lower() for i in self.exception_list]
        self.additional_list = [i.lower() for i in self.additional_list]

    def _lists_translate(self) -> None:
        if self.custom_list:
            self.custom_list = [return_translated(
                self._translation_table, i) for i in self.custom_list]

        self.exception_list = [return_translated(
            self._translation_table, i) for i in self.exception_list]
        self.additional_list = [return_translated(
            self._translation_table, i) for i in self.additional_list]

    def add_exceptions(self, words: list) -> None:
        """Allows the user to remove words to the list of pre-defined words
        to filter for.

        Paramaters:
        ----------
            words:
                A list of strings that will be removed from the default filter
                checking.
        """

        self.exception_list.extend(words)

        self._lists_to_lower()
        self._lists_translate()

    def add_words(self, words: list) -> None:
        """Allows the user to add words to the list of pre-defined words
        to filter for.

        Paramaters:
        ----------
            words:
                A list of strings that will be added to the default filter
                checking.
        """

        self.additional_list.extend(words)

        self._lists_to_lower()
        self._lists_translate()

    def reload_file(self) -> None:
        """Allows the user to update the filter list when using a custom
        JSON file so that if anything in the JSON file changed the changes
        are applied to the filter.
        """

        if not self._use_custom_file:
            raise RuntimeError('A Custom JSON file to use was never provided')

        with open(self.custom_json_file) as f:
            self._use_custom_file = json.load(f)

    def check(self, message) -> Check:
        """Checks the provided message for any words that should be filtered.

        Paramaters:
        ----------
            message:
                The message to be filtered. This should be a string.

        Returns:
        -------
            A check object which contains an as_bool property and an as_list
            property which can be used to retreive the results in either form.
        """

        return Check(message, self.exception_list, self.additional_list, self.custom_list, self._use_default_list, self._use_custom_file, self._translation_table, self._filter_file)

    @property
    def list_file(self) -> Path:
        """Returns the path to the list file if using a custom filter file."""

        return self.custom_json_file

    def __repr__(self):
        return '<Filter: custom_list={custom_list}, list_file={lf_apostrophe}{list_file}{lf_apostrophe}>'.format(custom_list=self.custom_list, list_file=self.custom_json_file, lf_apostrophe='\'' if self.custom_json_file else '')
