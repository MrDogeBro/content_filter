# Python Content Filter

[![Build Status](https://travis-ci.com/MrDogeBro/content_filter.svg?token=K4YBJnRBuxqyhssWYMJt&branch=master)](https://travis-ci.com/github/MrDogeBro/content_filter) [![PyPi version](https://img.shields.io/pypi/v/content-filter.svg)](https://pypi.python.org/pypi/content-filter/) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/content-filter.svg)](https://pypi.python.org/pypi/content-filter/) [![](https://img.shields.io/github/license/MrDogeBro/content_filter.svg)](https://github.com/MrDogeBro/content_filter/blob/master/LICENSE)

A basic but robust content filter for python. Content Filter allows you to easily detect if a piece of text
contains any language it shouldn't. It also allows you to add your own words to filter for, remove words to filter for, or define a whole new list of words to filter for.

## Table of Contents

1. [Getting Started](#getting-started)
   - [Python Version](#python-version)
   - [Installation](#installation)
1. [Usage](#usage)
   - [Filtering Messages](#filtering-messages)
   - [Adding Words to the Filter](#adding-words-to-the-filter)
   - [Removing Words from the Filter](#removing-words-from-the-filter)
   - [Using a Custom Filter](#using-a-custom-filter)
     - [Custom JSON File Structure](#custom-json-file-structure)
1. [Examples](#examples)
   - [Example #1](#example-1)
   - [Example #2](#example-2)
   - [Example #3](#example-3)
   - [Example #4](#example-4)
1. [Contributing](#contributing)
1. [Disclaimer](#disclaimer)
1. [License](#license)

## Getting Started

To get started, just make sure you have pip installed. If you use python, you probably already have pip installed as a lot of modules and libraries distribute via pip.

### Python Version

Please make sure that you have Python 3.4 or above installed or else the module will not work.

### Installation

To install Content Filter, enter the following command in any sort of terminal window or command prompt.

```bash
$ pip install content-filter
```

## Usage

Listed below are the different functions and their uses. If the function returns any value, the value it returns is also listed.

### Filtering Messages

To check a message with Content Filter, you have 2 options. You can either use the `checkMessage()` or `checkMessageList()` function which accepts the message as a string to scan as its argument.

```python
import content_filter

content_filter.checkMessage('message')
# Returns bool of wether it found language from the filter in the message

content_filter.checkMessageList('message')
# Returns a list of the words it found, the number of each word, and a censored version if it found anything and returns False if it did not.
```

### Adding Words to the Filter

To add words to the built in filter, use the `addWords()` function which accepts the words to add as its argument. This can either be a single word as a string or multiple words as an list of strings. You can add words in multiple places in your file with the same function.

```python
import content_filter

content_filter.addWords('singleword')
# Adds a single string to the list of words to filter for

content_filter.addWords(['word1', 'word2', 'word3'])
# Adds an list of strings to the list of words to filter for
```

### Removing Words from the Filter

To remove words from the built in filter, use the `addExceptions()` function which accepts the words to remove as its argument. This can either be a single word as a string or multiple words as an list of strings. You can remove words in multiple places in your file with the same function.

```python
import content_filter

content_filter.addExceptions('singleword')
# Adds a single string to the list of words to filter for

content_filter.addExceptions(['word1', 'word2', 'word3'])
# Adds an list of strings to the list of words to filter for
```

### Using a Custom Filter

To use a completely custom filter, you have to options. Your first option, use the `useCustomList()` function which accepts the list of words you would like to use as its argument. This can either be a single word as a string or multiple words as an list of strings. You can only define this in one place in your file (we recommend doing it somewhere near the top). You can use the `addWords()` and `addExceptions()` functions to add or remove words from your custom filter anywhere in the file still. Your second option is to create a JSON file to store the words in. To do this, use `useCustomListFile()` and then pass in a relative file path as a string and the `__file__` object so that the file can be located. It is important that you follow the specific structure for the JSON file that is listed below.

###### Option 1

```python
import content_filter

content_filter.useCustomList('singleword')
# Use a single string as the list of words to filter for

content_filter.useCustomList(['word1', 'word2', 'word3'])
# Use an list of strings as the list of words to filter for
```

###### Option 2

```python
import content_filter

content_filter.useCustomListFile('./fileName.json', __file__)
# Use a file to load the words to filter for
```

#### Custom JSON File Structure

To use a custom JSON file, you need to follow the specific structure that is stated here. To get started, the `"mainFilter"` is a list where you put all of the words to search the text for. Each word will need to be in a dictionary that contains the word to look for or the `"find"` (meaning it doesn't have to be the full word, just whatever you put in there is what it will look for anywhere in the text), the actual `"word"` (useful if you use a cutoff version of the word for the find), and a `"censored"` version of that word.

Next is the `"dontFilter"` which can either be null (None) or a list of strings to remove from the filter. If you set the value to null, this indicates to the filter that you want it to use the default list of words to not filter for. If you set the value to a list of strings, the filter will only not filter the strings in the list.

Finally, there is the `"conditionFilter"`, which is how you can make the filter only look for a specific word with no characters after it or before it as well as making spacing matter. This could be viewed as a strict filter where it will only find the word if the specific conditions are met exactly. The condition filter also follows the same standard as the main filter, being a list of dictionaries, each containing the find, word, and censored version.

If you ever want to make any of the filters blank, just put a empty list in the filter field, you want to contain nothing.

```json
{
  "mainFilter": [
    { "find": "find", "word": "word", "censored": "censored" },
    { "find": "helo", "word": "hello", "censored": "h3110" }
  ],
  "dontFilter": ["word"],
  "conditionFilter": [
    { "find": "find", "word": "word", "censored": "censored" }
  ]
}
```

Also, if you ever want to update the JSON file while python is running and have it start filtering for the words added, just call the `updateListFromFile()` function and it will re-pull the JSON file that was specified to be used.

## Examples

In the examples listed below, words have been bleeped out with \*'s which the filter natively checks for but the same concept would apply with the real words.

### Example #1

This is a basic example of how you could use content filter. In this example, we are just checking a message against the built in filter with no modification to the filter.

```python
import content_filter

content_filter.checkMessage('It is a beautiful day outside.')
# False

content_filter.checkMessage('Suck my d***!')
# True
```

### Example #2

This is a bit more advanced usage. In this example, a word is being removed from the filter and a new one is being added to the filter. Then, we check to see the results after modifying the filter.

```python
import content_filter

content_filter.addExceptions('s***')
content_filter.addWords('today')

content_filter.checkMessage('Hello there!')
# False

content_filter.checkMessage('MOTHERF***ER!')
# True

content_filter.checkMessage('Holy s***!')
# False

content_filter.checkMessage('Hi, how are you doing today?')
# True
```

### Example #3

This is more of an advanced use case for the module. In this example, the user is defining a custom list of words to check for which overrides the default filter. It will search for the words the same way but it will only search for the words that user defines in the custom filter.

```python
import content_filter

content_filter.useCustomList(['word1', 'word2'])

content_filter.checkMessage('Hello there!')
# False

content_filter.checkMessage('Welcome word1!')
# True

content_filter.checkMessage('What the f***!')
# False

content_filter.checkMessage('Hi, contains word2!')
# True
```

### Example #4

This is the most advanced use case for the module. In this example, the user is defining a custom file containing the words to check for which overrides the default filter. It will search for the words the same way but it will only search for the words that user defines in the custom filter. It will also return the information on what the filter found, not just a bool. For information on how to create a JSON file for the filter to be able to use, please visit the section above [Custom JSON File Structure](#custom-json-file-structure)

###### customFilter.json

```json
{
  "mainFilter": [
    { "find": "word1", "word": "word1", "censored": "w0rd1" },
    { "find": "word2", "word": "word2", "censored": "w0rd2" }
  ],
  "dontFilter": ["word"],
  "conditionFilter": [
    { "find": "find", "word": "word", "censored": "censored" }
  ]
}
```

###### main.py

```python
import content_filter

content_filter.useCustomListFile('./customFilter.json', __file__)

content_filter.checkMessageList('Hello there!')
# False

content_filter.checkMessageList('Welcome word1!')
# [{'word': 'word1', 'censored': 'w0rd1', 'count': 1}]

content_filter.checkMessageList('What the f***!')
# False

content_filter.checkMessageList('Hi, contains word2!')
# [{'word': 'word2', 'censored': 'w0rd2', 'count': 1}]
```

## Contributing

If you would like to help improve the Content Filter module, there are a few things that you can do to help. First, if you find any bugs/issues within the module, please report them in the [issues tab](https://github.com/MrDogeBro/content_filter/issues). Second, if you have any features that you would like added to the module or you have any other suggestions for the module, please submit a [pull request](https://github.com/MrDogeBro/content_filter/pulls). Third, if you found that a word was able to bypass the filter in your application, please submit a [bypass report](https://forms.gle/jaQkoPi54wayu9FA7). Finally, if you would like to help improve the filtering system, test the module on a ton of sentences and submit a [testing report](https://forms.gle/eXyUwdnqj9D8DgzB6) if you find any words that should be added or removed from the default filter. Testing is probably the most useful contribution you can make right now. We thank you for any contributions that you make to the module.

## Disclaimer

Please be aware that the code on GitHub may be newer than the version that is on [PyPI](https://pypi.org/project/content-filter/) since code may be uploaded to GitHub as a beta before it is uploaded officially to PyPI.

## License

The Content Filter module for Python is licensed under an [MIT license](https://github.com/MrDogeBro/content_filter/blob/master/LICENSE).
