"""
filter.py

The main file that is the hub of all operations
"""

import json
import typing as t
from pathlib import Path

from content_filter.check import Check
from content_filter.string import return_translated


class Filter:
    """The filter object which contains the filter settings,
    data, and functions.

    Args:
        list_file (str, optional): The path to a file that will be used as the filter
            list in place of the default filter
        word_list (str, optional): A list of words to be used as the filter in place
            of the default filter

    Raises:
        TypeError: Something other than a :class:`list` was not passed in for word_list.
        FileNotFoundError: The input file for list_file does not exist.
        ValueError: The custom file input is not a JSON file.
    """

    def __init__(
        self,
        list_file: t.Optional[str] = None,
        word_list: t.Optional[t.List[str]] = None,
    ):
        self.exception_list: t.List[str] = []
        self.additional_list: t.List[str] = []
        self.custom_list = (
            [word.replace(" ", "") for word in word_list]
            if isinstance(word_list, list)
            else []
        )
        self._use_default_list = True
        self._use_custom_file: t.Dict[str, t.Any] = {}
        self._filter_file = Path.joinpath(
            Path(__file__).resolve().parent, "data/filter.json"
        )

        # ==== LOAD TRANSLATIONS ====

        translations_file = Path.joinpath(
            Path(__file__).resolve().parent, "data/replacements.json"
        )

        with open(str(translations_file)) as f:
            loaded_translations: t.Dict[str, t.Dict[str, str]] = json.load(f)

        self._translation_table = {
            "single": str.maketrans(loaded_translations["single_char"]),
            "multi": loaded_translations["multi_char"],
        }

        # ==== CUSTOM FILE CHECK ====

        if list_file:
            if not Path(list_file).is_absolute():
                rel_list_file = Path.joinpath(Path.cwd(), list_file)

            self.custom_json_file = Path(rel_list_file if rel_list_file else list_file)

            if self.custom_json_file.suffix != ".json":
                raise ValueError(
                    "list_file expected .json file but got "
                    + self.custom_json_file.suffix
                )

            with open(str(self.custom_json_file)) as f:
                self._use_custom_file = json.load(f)

            self._use_default_list = False

        # ==== CUSTOM LIST CHECK ====

        if word_list and not isinstance(word_list, list):
            raise TypeError(
                "word_list expects list but got " + str(type(word_list).__name__)
            )

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
            self.custom_list = [
                return_translated(self._translation_table, i) for i in self.custom_list
            ]

        self.exception_list = [
            return_translated(self._translation_table, i) for i in self.exception_list
        ]
        self.additional_list = [
            return_translated(self._translation_table, i) for i in self.additional_list
        ]

    def _check_type(self, obj: t.List[t.Any]) -> bool:
        return bool(obj) and all(isinstance(elem, str) for elem in obj)

    def add_exceptions(self, words: t.List[str]) -> None:
        """Allows the user to remove words to the list of pre-defined words
        to filter for.

        Args:
            words (list): A list of strings that will be removed from the default filter
                checking.

        Raises:
            TypeError: Words input are not a list of strings.
        """

        if not self._check_type(words) or not isinstance(words, list):
            raise TypeError("Words input are not a list of strings")

        self.exception_list.extend(words)

        self._lists_to_lower()
        self._lists_translate()

    def add_words(self, words: t.List[str]) -> None:
        """Allows the user to add words to the list of pre-defined words
        to filter for.

        Args:
            words (list): A list of strings that will be added to the default filter
                checking.

        Raises:
            TypeError: Words input are not a list of strings.
        """

        if not self._check_type(words) or not isinstance(words, list):
            raise TypeError("Words input are not a list of strings")

        self.additional_list.extend(words)

        self._lists_to_lower()
        self._lists_translate()

    def reload_file(self) -> None:
        """Updates the filter list when using a custom JSON file. If any
        changes have been made to the file, they will be applied.

        Raises:
            RuntimeError: Not using a custom JSON file.
        """

        if not self._use_custom_file:
            raise RuntimeError("A custom JSON file to use was never provided")

        with open(str(self.custom_json_file)) as f:
            self._use_custom_file = json.load(f)

    def check(self, message: str) -> Check:
        """Checks the provided message for any words that should be filtered.

        Args:
            message (str): The message to be filtered. This should be a string.

        Raises:
            TypeError: Message is not a string

        Returns:
            .Check: A check object which contains the results of the filter.
        """

        if type(message) is not str:
            raise TypeError("Message provided is not a string")

        return Check(
            message,
            self.exception_list,
            self.additional_list,
            self.custom_list,
            self._use_default_list,
            self._use_custom_file,
            self._translation_table,
            self._filter_file,
        )

    @property
    def list_file(self) -> Path:
        """Gives you the path to the list file if using a custom filter file.

        Raises:
            RuntimeError: Not using a custom JSON file.

        Returns:
            :class:`pathlib.Path`: A path object to the custom json file.
        """

        if not self._use_custom_file:
            raise RuntimeError("A custom JSON file to use was never provided")

        return self.custom_json_file

    def __repr__(self) -> str:
        return "<Filter: custom_list={custom_list}, list_file={lf_apostrophe}{list_file}{lf_apostrophe}>".format(
            custom_list=self.custom_list,
            list_file=self.custom_json_file,
            lf_apostrophe="'" if self.custom_json_file else "",
        )
