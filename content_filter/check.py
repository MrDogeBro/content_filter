"""
check.py

Checks message to see if they contain any words in the filter
"""

import json
import re

from .string import return_translated, return_possibilities


def defaultCheck(message, customWordList, exceptionList, additionalList, useDefaultList, useCustomFile, replacement_table, file=None):
    filterMsgContent = message.lower()
    filterData = None

    if useDefaultList:
        # gets all of the words to filter for
        with open(file) as f:
            filterData = json.load(f)

    elif useCustomFile:
        filterData = useCustomFile

    if not customWordList:
        if filterData['dontFilter'] is not None:
            # goes through all of the words in the filter and checks if any are in the message
            for word in filterData['dontFilter']:
                # checks for words that should not be filtered in teh message
                if word in message.lower():
                    # gets rid of the words that shouldn't be filtered so that the filter wont find them
                    filterMsgContent = filterMsgContent.replace(word, '')

        else:
            # gets default list of words
            with open(file) as f:
                defaultListFile = json.load(f)

            # goes through all of the words in the filter and checks if any are in the message
            for word in defaultListFile['dontFilter']:
                # checks for words that should not be filtered in teh message
                if word in message.lower():
                    # gets rid of the words that shouldn't be filtered so that the filter wont find them
                    filterMsgContent = filterMsgContent.replace(word, '')

    # goes through all of the words in the filter and checks if any are in the message
    for word in exceptionList:
        # checks for words that should not be filtered in the message
        if not customWordList:
            for string in filterData['mainFilter']:
                if string in exceptionList:
                    try:
                        filterData['mainFilter'].pop(
                            filterData['mainFilter'].index(string))

                    except:
                        # gets rid of the words that shouldn't be filtered so that the filter wont find them
                        filterMsgContent = filterMsgContent.replace(word, '')

            # checks for words that should not be filtered in the message
            try:
                filterData['conditionalFilter'].pop(word)

            except:
                # gets rid of the words that shouldn't be filtered so that the filter wont find them
                filterMsgContent = filterMsgContent.replace(word, '')

        else:
            # checks for words that should not be filtered in the message
            try:
                customWordList.pop(word)

            except:
                # gets rid of the words that shouldn't be filtered so that the filter wont find them
                filterMsgContent = filterMsgContent.replace(word, '')

    # sets up a var that will be used to look for words in that replaces all irregular charaters with the charater they might be used for as a bad word
    filterMsgContent = return_translated(replacement_table, filterMsgContent)
    filterMsgCombos = return_possibilities(filterMsgContent)

    for msgCombo in filterMsgCombos:
        if not customWordList:
            # goes through all of the words in the filter and checks if any are in the message
            for word in filterData['mainFilter']:
                if (re.search('+[.!-]*'.join(c for c in word['find']), msgCombo.replace(' ', ''))):
                    return True  # exits the check so that it doesn't fire multiple

            # goes through all of the words in the filter and checks if any are in the message
            for word in additionalList:
                if (re.search('+[.!-]*'.join(c for c in word), msgCombo.replace(' ', ''))):
                    return True  # exits the check so that it doesn't fire multiple times

            # goes through all of the words in the filter and checks if any are in the message
            for word in filterData['conditionFilter']:
                if word['require_space']:
                    if ' ' + word['find'] in msgCombo or word['find'] in msgCombo[:len(word['find'])]:
                        return True  # exits the check so that it doesn't fire multiple times
                else:
                    if word['find'] in msgCombo or word['find'] in msgCombo[:len(word['find'])]:
                        return True  # exits the check so that it doesn't fire multiple times

        else:
            # goes through all of the words in the filter and checks if any are in the message
            for word in exceptionList:
                # checks for words that should not be filtered in the message
                try:
                    customWordList.pop(word)

                except:
                    # gets rid of the words that shouldn't be filtered so that the filter wont find them
                    msgCombo = msgCombo.replace(word, '')

            # goes through all of the words in the filter and checks if any are in the message
            for word in customWordList:
                if (re.search('+[.!-]*'.join(c for c in word), msgCombo.replace(' ', ''))):
                    return True  # exits the check so that it doesn't fire multiple

            # goes through all of the words in the filter and checks if any are in the message
            for word in additionalList:
                if (re.search('+[.!-]*'.join(c for c in word), msgCombo.replace(' ', ''))):
                    return True  # exits the check so that it doesn't fire multiple times

    return False


def listCheck(message, customWordList, exceptionList, additionalList, useDefaultList, useCustomFile, replacement_table, file=None):
    filterMsgContent = message.lower()
    wordsFoundList = []
    filterData = None

    if useDefaultList:
        # gets all of the words to filter for
        with open(file) as f:
            filterData = json.load(f)

    elif useCustomFile:
        filterData = useCustomFile

    if not customWordList:
        if filterData['dontFilter'] is not None:
            # goes through all of the words in the filter and checks if any are in the message
            for word in filterData['dontFilter']:
                # checks for words that should not be filtered in teh message
                if word in message.lower():
                    # gets rid of the words that shouldn't be filtered so that the filter wont find them
                    filterMsgContent = filterMsgContent.replace(word, '')

        else:
            # gets default list of words
            with open(file) as f:
                defaultListFile = json.load(f)

            # goes through all of the words in the filter and checks if any are in the message
            for word in defaultListFile['dontFilter']:
                # checks for words that should not be filtered in teh message
                if word in message.lower():
                    # gets rid of the words that shouldn't be filtered so that the filter wont find them
                    filterMsgContent = filterMsgContent.replace(word, '')

    # goes through all of the words in the filter and checks if any are in the message
    for word in exceptionList:
        if not customWordList:
            # checks for words that should not be filtered in teh message
            for string in filterData['mainFilter']:
                if string in exceptionList:
                    try:
                        filterData['mainFilter'].pop(
                            filterData['mainFilter'].index(string))

                    except:
                        # gets rid of the words that shouldn't be filtered so that the filter wont find them
                        filterMsgContent = filterMsgContent.replace(word, '')

            # checks for words that should not be filtered in the message
            try:
                filterData['conditionalFilter'].pop(word)

            except:
                # gets rid of the words that shouldn't be filtered so that the filter wont find them
                filterMsgContent = filterMsgContent.replace(word, '')

        else:
            # checks for words that should not be filtered in the message
            try:
                customWordList.pop(word)

            except:
                # gets rid of the words that shouldn't be filtered so that the filter wont find them
                filterMsgContent = filterMsgContent.replace(word, '')

    # sets up a var that will be used to look for words in that replaces all irregular charaters with the charater they might be used for as a bad word
    filterMsgContent = return_translated(replacement_table, filterMsgContent)
    filterMsgCombos = return_possibilities(filterMsgContent)

    for msgCombo in filterMsgCombos:
        if not customWordList:
            # goes through all of the words in the filter and checks if any are in the message
            for word in filterData['mainFilter']:
                wordFound = [(m.start(), m.end()) for m in re.finditer(
                    '+[.!-]*'.join(c for c in word['find']), msgCombo.replace(' ', ''))]

                if (wordFound):
                    wordsFoundList.append(
                        {'word': word['word'], 'censored': word['censored'], 'count': len(wordFound), 'indexes': wordFound})

            # goes through all of the words in the filter and checks if any are in the message
            for word in additionalList:
                wordFound = [(m.start(), m.end()) for m in re.finditer(
                    '+[.!-]*'.join(c for c in word), msgCombo.replace(' ', ''))]

                if (wordFound):
                    wordsFoundList.append(
                        {'word': word, 'count': len(wordFound), 'indexes': wordFound})

            # goes through all of the words in the filter and checks if any are in the message
            for word in filterData['conditionFilter']:
                if word['require_space']:
                    wordFound = ' ' + \
                        word['find'] in msgCombo or word['find'] in msgCombo[:len(
                            word['find'])]

                    if wordFound:
                        wordFoundRegex = [(m.start(), m.end()) for m in re.finditer(
                            word['find'], msgCombo)]
                        wordsFoundList.append(
                            {'word': word['word'], 'censored': word['censored'], 'count': len(wordFoundRegex), 'indexes': wordFoundRegex})
                else:
                    wordFound = word['find'] in msgCombo or word['find'] in msgCombo[:len(
                        word['find'])]

                    if wordFound:
                        wordFoundRegex = [(m.start(), m.end()) for m in re.finditer(
                            word['find'], msgCombo)]
                        wordsFoundList.append(
                            {'word': word['word'], 'censored': word['censored'], 'count': len(wordFoundRegex), 'indexes': wordFoundRegex})

        else:
            # goes through all of the words in the filter and checks if any are in the message
            for word in exceptionList:
                # checks for words that should not be filtered in teh message
                try:
                    customWordList.pop(word)

                except:
                    # gets rid of the words that shouldn't be filtered so that the filter wont find them
                    msgCombo = msgCombo.replace(word, '')

            # goes through all of the words in the filter and checks if any are in the message
            for word in customWordList:
                wordFound = [(m.start(), m.end()) for m in re.finditer(
                    '+[.!-]*'.join(c for c in word), msgCombo.replace(' ', ''))]

                if (wordFound):
                    wordsFoundList.append(
                        {'word': word, 'count': len(wordFound), 'indexes': wordFound})

            # goes through all of the words in the filter and checks if any are in the message
            for word in additionalList:
                wordFound = [(m.start(), m.end()) for m in re.finditer(
                    '+[.!-]*'.join(c for c in word), msgCombo.replace(' ', ''))]

                if (wordFound):
                    wordsFoundList.append(
                        {'word': word, 'count': len(wordFound), 'indexes': wordFound})

    to_remove = []

    for match in wordsFoundList:
        if [w['word'] for w in wordsFoundList].count(match['word']) > 1:
            if wordsFoundList.count(match) > 1 and to_remove.count(match) < (wordsFoundList.count(match) - 1):
                to_remove.append(match)

            else:
                indexLen = ([i['count'] for i in wordsFoundList if i['word'] == match['word']], [
                            i for i in wordsFoundList if i['word'] == match['word']])

                if indexLen[1][indexLen[0].index(max(indexLen[0]))] != match and to_remove.count(match) < wordsFoundList.count(match):
                    to_remove.append(match)

    for rem in to_remove:
        wordsFoundList.remove(rem)

    return wordsFoundList
