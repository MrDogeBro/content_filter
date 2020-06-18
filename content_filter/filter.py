# filter.py

import re
import json
import os

exceptionList = []
additionalList = []
customWordList = []
useDefaultList = True

def _makeListsLower(listName):
    if listName == 'exceptionList':
        global exceptionList
        listName = [i.lower() for i in listName]

    elif listName == 'additionalList':
        global exceptionList
        listName = [i.lower() for i in listName]

    else:
        pass

def _changeListChars(listName):
    if listName == 'exceptionList':
        global exceptionList
        exceptionList = [i.replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace('+', 't').replace('!', 'i').replace('@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#') for i in exceptionList]

    elif listName == 'additionalList':
        global additionalList
        additionalList = [i.replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace('+', 't').replace('!', 'i').replace('@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#') for i in additionalList]

    elif listName == 'customList':
        global customWordList
        customWordList = [i.replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace('+', 't').replace('!', 'i').replace('@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#').replace(' ', '') for i in customWordList]

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
    if useDefaultList:
        filterContentFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/filter.json')

        filterMsgContent = message.lower()

        # gets all of the words to filter for
        with open(filterContentFile) as f:
            filterData = json.load(f)

        # goes through all of the words in the filter and checks if any are in the message
        for word in filterData['dontFilter']:
            # checks for words that should not be filtered in teh message
            if word in message.lower():
                filterMsgContent = filterMsgContent.replace(word, '') # gets rid of the words that shouldn't be filtered so that the filter wont find them

        # goes through all of the words in the filter and checks if any are in the message
        for word in exceptionList:
            # checks for words that should not be filtered in teh message
            for string in filterData['mainFilter']:
                if string in exceptionList:
                    try:
                        filterData['mainFilter'].pop(filterData['mainFilter'].index(string))

                    except:
                        filterMsgContent = filterMsgContent.replace(word, '') # gets rid of the words that shouldn't be filtered so that the filter wont find them

            # checks for words that should not be filtered in teh message
            try:
                filterData['conditionalFilter'].pop(word)

            except:
                filterMsgContent = filterMsgContent.replace(word, '') # gets rid of the words that shouldn't be filtered so that the filter wont find them

        # sets up a var that will be used to look for words in that replaces all irregular charaters with the charater they might be used for as a bad word
        filterMsgContent = filterMsgContent.replace('a$', 'a##').replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace('+', 't').replace('!', 'i').replace('@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#')

        # goes through all of the words in the filter and checks if any are in the message
        for word in filterData['mainFilter']:
            if (re.search('+[.!-]*'.join(c for c in word), filterMsgContent.replace(' ', ''))):
                return True # exits the check so that it doesn't fire multiple 
                
        # goes through all of the words in the filter and checks if any are in the message
        for word in additionalList:
            if (re.search('+[.!-]*'.join(c for c in word), filterMsgContent.replace(' ', ''))):
                return True # exits the check so that it doesn't fire multiple times

        # goes through all of the words in the filter and checks if any are in the message
        for word in filterData['conditionFilter']:
            if ' ' + word in filterMsgContent or word in filterMsgContent[:len(word)]:
                return True # exits the check so that it doesn't fire multiple times

        return False

    else:
        filterMsgContent = message.lower()

        # goes through all of the words in the filter and checks if any are in the message
        for word in exceptionList:
            # checks for words that should not be filtered in teh message
            try:
                customWordList.pop(word)

            except:
                filterMsgContent = filterMsgContent.replace(word, '') # gets rid of the words that shouldn't be filtered so that the filter wont find them

        # sets up a var that will be used to look for words in that replaces all irregular charaters with the charater they might be used for as a bad word
        filterMsgContent = filterMsgContent.replace('a$', 'a##').replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace('+', 't').replace('!', 'i').replace('@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#')

        # goes through all of the words in the filter and checks if any are in the message
        for word in customWordList:
            if (re.search('+[.!-]*'.join(c for c in word), filterMsgContent.replace(' ', ''))):
                return True # exits the check so that it doesn't fire multiple 
                
        # goes through all of the words in the filter and checks if any are in the message
        for word in additionalList:
            if (re.search('+[.!-]*'.join(c for c in word), filterMsgContent.replace(' ', ''))):
                return True # exits the check so that it doesn't fire multiple times

        return False