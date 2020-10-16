import json
import re


def defaultCheck(message, customWordList, exceptionList, additionalList, useDefaultList, useCustomFile, file=None):
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
    filterMsgContent = filterMsgContent.replace('a$', 'a##').replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace(
        '+', 't').replace('!', 'i').replace('@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#')

    if not customWordList:
        # goes through all of the words in the filter and checks if any are in the message
        for word in filterData['mainFilter']:
            if (re.search('+[.!-]*'.join(c for c in word['find']), filterMsgContent.replace(' ', ''))):
                return True  # exits the check so that it doesn't fire multiple

        # goes through all of the words in the filter and checks if any are in the message
        for word in additionalList:
            if (re.search('+[.!-]*'.join(c for c in word), filterMsgContent.replace(' ', ''))):
                return True  # exits the check so that it doesn't fire multiple times

        # goes through all of the words in the filter and checks if any are in the message
        for word in filterData['conditionFilter']:
            if ' ' + word['find'] in filterMsgContent or word['find'] in filterMsgContent[:len(word['find'])]:
                return True  # exits the check so that it doesn't fire multiple times

    else:
        # goes through all of the words in the filter and checks if any are in the message
        for word in exceptionList:
            # checks for words that should not be filtered in the message
            try:
                customWordList.pop(word)

            except:
                # gets rid of the words that shouldn't be filtered so that the filter wont find them
                filterMsgContent = filterMsgContent.replace(word, '')

        # sets up a var that will be used to look for words in that replaces all irregular charaters with the charater they might be used for as a bad word
        filterMsgContent = filterMsgContent.replace('a$', 'a##').replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace(
            '+', 't').replace('!', 'i').replace('@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#')

        # goes through all of the words in the filter and checks if any are in the message
        for word in customWordList:
            if (re.search('+[.!-]*'.join(c for c in word), filterMsgContent.replace(' ', ''))):
                return True  # exits the check so that it doesn't fire multiple

        # goes through all of the words in the filter and checks if any are in the message
        for word in additionalList:
            if (re.search('+[.!-]*'.join(c for c in word), filterMsgContent.replace(' ', ''))):
                return True  # exits the check so that it doesn't fire multiple times

    return False


def listCheck(message, customWordList, exceptionList, additionalList, useDefaultList, useCustomFile, file=None):

    filterMsgContent = message.lower()
    wordsFoundList = []
    filterData = None

    if useDefaultList:
        # gets all of the words to filter for
        with open(file) as f:
            filterData = json.load(f)

    elif useCustomFile:
        filterData = useCustomFile

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
    filterMsgContent = filterMsgContent.replace('a$', 'a##').replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace(
        '+', 't').replace('!', 'i').replace('@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#')

    if not customWordList:
        # goes through all of the words in the filter and checks if any are in the message
        for word in filterData['mainFilter']:
            wordFound = re.findall(
                '+[.!-]*'.join(c for c in word['find']), filterMsgContent.replace(' ', ''))

            if (wordFound):
                wordsFoundList.append(
                    {'word': word['word'], 'censored': word['censored'], 'count': len(wordFound)})

        # goes through all of the words in the filter and checks if any are in the message
        for word in additionalList:
            wordFound = re.findall(
                '+[.!-]*'.join(c for c in word), filterMsgContent.replace(' ', ''))

            if (wordFound):
                wordsFoundList.append(
                    {'word': word['word'], 'censored': word['censored'], 'count': len(wordFound)})

        # goes through all of the words in the filter and checks if any are in the message
        for word in filterData['conditionFilter']:
            wordFound = ' ' + \
                word['find'] in filterMsgContent or word['find'] in filterMsgContent[:len(
                    word['find'])]

            if wordFound:
                wordFoundRegex = re.findall(word['find'], filterMsgContent)
                wordsFoundList.append(
                    {'word': word['word'], 'censored': word['censored'], 'count': len(wordFoundRegex)})

    else:
        # goes through all of the words in the filter and checks if any are in the message
        for word in exceptionList:
            # checks for words that should not be filtered in teh message
            try:
                customWordList.pop(word)

            except:
                # gets rid of the words that shouldn't be filtered so that the filter wont find them
                filterMsgContent = filterMsgContent.replace(word, '')

        # sets up a var that will be used to look for words in that replaces all irregular charaters with the charater they might be used for as a bad word
        filterMsgContent = filterMsgContent.replace('a$', 'a##').replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace("'", '').replace(
            '+', 't').replace('!', 'i').replace('@', 'a').replace('1', 'i').replace('0', 'o').replace('3', 'e').replace('$', 's').replace('*', '#')

        # goes through all of the words in the filter and checks if any are in the message
        for word in customWordList:
            wordFound = re.findall(
                '+[.!-]*'.join(c for c in word), filterMsgContent.replace(' ', ''))

            if (wordFound):
                wordsFoundList.append(
                    {'word': word, 'count': len(wordFound)})

        # goes through all of the words in the filter and checks if any are in the message
        for word in additionalList:
            wordFound = re.findall(
                '+[.!-]*'.join(c for c in word), filterMsgContent.replace(' ', ''))

            if (wordFound):
                wordsFoundList.append(
                    {'word': word, 'count': len(wordFound)})

    return wordsFoundList
