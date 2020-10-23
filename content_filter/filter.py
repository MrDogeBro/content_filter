"""
filter.py

The main file that is the hub of all operations
"""

import json
import os

from .check import defaultCheck, listCheck

exceptionList = []
additionalList = []
customWordList = []
useDefaultList = True
useCustomFile = False
customJSONFile = None
setup_finished = False
replacement_table = None


def _makeListsLower(listName):
    if listName == 'exceptionList':
        global exceptionList
        listName = [i.lower() for i in listName]

    elif listName == 'additionalList':
        global exceptionList
        listName = [i.lower() for i in listName]

    else:
        pass


def setup():
    global setup_finished
    global replacement_table

    if not setup_finished:
        replacement_file = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'data/replacements.json')

        with open(replacement_file) as f:
            loaded_replacements = json.load(f)

        replacement_table = {
            'single': str.maketrans(loaded_replacements['single_char']),
            'multi': loaded_replacements['multi_char']
        }

        setup_finished = True


def _changeListChars(listName):
    if listName == 'exceptionList':
        global exceptionList
        exceptionList = [i.replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace('+', 't').replace(
            '!', 'i').replace('@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#') for i in exceptionList]

    elif listName == 'additionalList':
        global additionalList
        additionalList = [i.replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace('+', 't').replace(
            '!', 'i').replace('@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#') for i in additionalList]

    elif listName == 'customList':
        global customWordList
        customWordList = [i.replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace('+', 't').replace('!', 'i').replace(
            '@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#').replace(' ', '') for i in customWordList]

    else:
        pass


def useCustomList(wordList):
    """Allows the user to define a custom list of words to filter for.
    Keep in mind that this will completely override the default filter,
    meaning that any words defined in the default filter will now have
    to be manually added by the user if they desire for those words to
    be filtered. If you would just like to add on or remove from the
    existing, please check out our [GitHub](https://github.com/MrDogeBro/content_filter)

    Paramaters:
    ----------
    words:
        The words that the filter will check for. This can be in the
        form of a single string or an array of strings.
    """
    global customWordList
    global useDefaultList

    if isinstance(wordList, list):
        customWordList = wordList

    else:
        customWordList = [wordList]

    useDefaultList = False
    _changeListChars('customList')


def addExceptions(words=None):
    """Allows the user to remove words to the list of pre-defined words
    to filter for. If you would like to completely override the existing
    filter, please check out our [GitHub](https://github.com/MrDogeBro/content_filter)

    Paramaters:
    ----------
    words:
        The words that will be removed from the default filter to
        check for. This can be in the form of a single string or an
        array of strings.
    """
    global exceptionList

    if isinstance(words, list):
        exceptionList.extend(words)

    else:
        exceptionList.extend([words])

    _makeListsLower('exceptionList')


def addWords(words=None):
    """Allows the user to add words to the list of pre-defined words
    to filter for. If you would like to completely override the existing
    filter, please check out our [GitHub](https://github.com/MrDogeBro/content_filter)

    Paramaters:
    ----------
    words:
        The words that will be added to the default filter to check
        for. This can be in the form of a single string or an array
        of strings.
    """
    global additionalList

    if isinstance(words, list):
        additionalList.extend(words)

    else:
        additionalList.extend([words])

    _makeListsLower('additionalList')
    _changeListChars('additionalList')


def useCustomListFile(file, currentFile):
    """Allows the user to define a custom list of words to filter for
    from a json file. Keep in mind that this will completely override
    the default filter, meaning that any words defined in the default
    filter will now have to be manually added by the user if they
    desire for those words to be filtered. For the structure the json
    file needs to follow or if you would just like to add on or remove
    from the existing list, please check out our [GitHub](https://github.com/MrDogeBro/content_filter)

    Paramaters:
    ----------
    file:
        A json file that defines a list of words to filter for. To find
        out the json file structure, check out our Github (linked above)
    currentFile:
        The current file that is calling the function. You pass this in
        by passing in __file__
    """

    global useCustomFile, useDefaultList, customJSONFile

    customJSONFile = os.path.join(os.path.dirname(
        os.path.abspath(currentFile)), file)

    with open(customJSONFile) as f:
        useCustomFile = json.load(f)

    useDefaultList = False


def updateListFromFile():
    """Allows the user to update the filter list when using a custom
    JSON file so that if anything in the JSON file changed the changes
    are applied to the filter.
    """

    global useCustomFile

    if useCustomFile:
        with open(customJSONFile) as f:
            useCustomFile = json.load(f)

    else:
        raise RuntimeError('A Custom JSON file to use was never provided')


def checkMessage(message):
    """Checks the provided message for any words that should be filtered and
    returns a value based on if it was able to identify anything.

    Paramaters:
    ----------
    message:
        The message that should be scanned for any language that matches
        any of the language that the filter is looking for. This value
        should be passed in as a string.

    Returns:
    -------
        Returns a `bool` value. True is returned if the filter found
        something in the text provided. False is returned if the filter
        did not find anything of interest in the text provided.
    """

    if not setup_finished:
        setup()

    filterContentFile = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'data/filter.json')

    return defaultCheck(message, customWordList, exceptionList, additionalList,
                        useDefaultList, useCustomFile, replacement_table, filterContentFile)


def checkMessageList(message):
    """Checks the provided message for any words that should be filtered and
    returns a list of words that were identified with some data about the word.

    Paramaters:
    ----------
    message:
        The message that should be scanned for any language that matches
        any of the language that the filter is looking for. This value
        should be passed in as a string.

    Returns:
    -------
        Returns a list value. List with words found, count of the words
        found, and a censored version of the words is returned if the filter
        found something in the text provided. False is returned if the filter
        did not find anything of interest in the text provided.
    """

    if not setup_finished:
        setup()

    filterContentFile = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'data/filter.json')

    return listCheck(message, customWordList, exceptionList, additionalList,
                     useDefaultList, useCustomFile, replacement_table, filterContentFile)
