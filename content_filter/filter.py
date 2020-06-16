# filter.py

import re
import json
import os

exceptionList = []
additionalList = []
useDefaultFile = True

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
    else:
        pass

def addExceptions(words=None):
    global exceptionList

    if isinstance(words, list):
        exceptionList.extend(words)

    else:
        exceptionList.extend([words])

    _makeListsLower('exceptionList')

def addWords(words=None):
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
        if word in message.lower():
            filterMsgContent = filterMsgContent.replace(word, '') # gets rid of the words that shouldn't be filtered so that the filter wont find them

    # sets up a var that will be used to look for words in that replaces all irregular charaters with the charater they might be used for as a bad word
    filterMsgContent = filterMsgContent.replace('a$', 'a##').replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace('+', 't').replace('!', 'i').replace('@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#')

    # goes through all of the words in the filter and checks if any are in the message
    for word in filterData['mainFilter']:
        if (re.search('+[.!-i]*'.join(c for c in word), filterMsgContent.replace(' ', ''))):
            return True # exits the check so that it doesn't fire multiple 
            
    # goes through all of the words in the filter and checks if any are in the message
    for word in additionalList:
        if (re.search('+[.!-i]*'.join(c for c in word), filterMsgContent.replace(' ', ''))):
            return True # exits the check so that it doesn't fire multiple times

    # goes through all of the words in the filter and checks if any are in the message
    for word in filterData['conditionFilter']:
        if ' ' + word in filterMsgContent or word in filterMsgContent[:len(word)]:
            return True # exits the check so that it doesn't fire multiple times

    return False