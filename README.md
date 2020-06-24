# Python Content Filter
[![Build Status](https://travis-ci.com/MrDogeBro/content_filter.svg?token=K4YBJnRBuxqyhssWYMJt&branch=master)](https://travis-ci.com/github/MrDogeBro/content_filter) [![PyPi version](https://img.shields.io/pypi/v/content-filter.svg)](https://pypi.python.org/pypi/content-filter/) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/content-filter.svg)](https://pypi.python.org/pypi/content-filter/) [![](https://img.shields.io/github/license/MrDogeBro/content_filter.svg)](https://github.com/MrDogeBro/content_filter/blob/master/LICENSE)

A basic but robust content filter for python. Content Filter allows you to easily detect if a piece of text 
contains any language it shouldn't. It also allows you to add your own words to filter for, remove words to filter for, 
or define a whole new list of words to filter for.

## Table of Contents
1. [Getting Started](#getting-started)
    * [Python Version](#python-version)
    * [Installation](#installation)
1. [Usage](#usage)
    * [Filtering Messages](#filter-messages)
    * [Adding Words to the Filter](#adding-words-to-the-filter)
    * [Removing Words from the Filter](#removing-words-from-the-filter)
    * [Using a Custom Filter](#using-a-custom-filter)
1. [Examples](#examples)
    * [Example #1](#example-1)
    * [Example #2](#example-2)
    * [Example #3](#example-3)
1. [Contributing](#contributing)
1. [Disclaimer](#disclaimer)
1. [License](#license)

## Getting Started
To get started, just make sure you have pip installed. If you use python, you probably already have pip installed as a lot of modules and libraries distribute via pip.

### Python Version
Please make sure that you have Python 3.4 or above installed or else the module will not work.

### Installation
To install Content Filter, enter the following command in any sort of terminal window or command prompt.
```
$ pip install content-filter
```

## Usage
Listed below are the different functions and their uses. If the function returns any value, the value it returns is also listed.

### Filtering Messages
To check a message with Content Filter, use the `.checkMessage()` function which accepts the message as a string to scan as its argument.
```python
import content_filter

content_filter.checkMessage('message')
# Returns bool of wether it found language from the filter in the message.
```

### Adding Words to the Filter
To add words to the built in filter, use the `.addWords()` function which accepts the words to add as its argument. This can either be a single word as a string or multiple words as an array of strings. You can add words in multiple places in your file with the same function.
```python
import content_filter

content_filter.addWords('singleword')
# Adds a single string to the list of words to filter for

content_filter.addWords(['word1', 'word2', 'word3'])
# Adds an array of strings to the list of words to filter for
```

### Removing Words from the Filter
To remove words from the built in filter, use the `.addExceptions()` function which accepts the words to remove as its argument. This can either be a single word as a string or multiple words as an array of strings. You can remove words in multiple places in your file with the same function.
```python
import content_filter

content_filter.addExceptions('singleword')
# Adds a single string to the list of words to filter for

content_filter.addExceptions(['word1', 'word2', 'word3'])
# Adds an array of strings to the list of words to filter for
```

### Using a Custom Filter
To use a completely custom filter, use the `.useCustomList()` function which accepts the list of words you would like to use as its argument. This can either be a single word as a string or multiple words as an array of strings. You can only define this in one place in your file (we recommend doing it somewhere near the top). You can use the `.addWords()` and `.addExceptions()` functions to add or remove words from your custom filter anywhere in the file still.
```python
import content_filter

content_filter.useCustomList('singleword')
# Use a single string as the list of words to filter for

content_filter.useCustomList(['word1', 'word2', 'word3'])
# Use an array of strings as the list of words to filter for
```

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
This is probably the most advanced use case for the module. In this example, the user is defining a custom list of words to check for which overrides the default filter. It will search for the words the same way but it will only search for the words that user defines in the custom filter.
```python
import content_filter

content_filter.useCustomFilter(['word1', 'word2'])

content_filter.checkMessage('Hello there!')
# False

content_filter.checkMessage('Welcome word1!')
# True

content_filter.checkMessage('What the f***!')
# False

content_filter.checkMessage('Hi, contains word2!')
# True
```

## Contributing
If you would like to help improve the Content Filter module, there are a few things that you can do to help. First, if you find any bugs/issues within the module, please report them in the [issues tab](https://github.com/MrDogeBro/content_filter/issues). Second, if you have any features that you would like added to the module or you have any other suggestions for the module, please submit a [pull request](https://github.com/MrDogeBro/content_filter/pulls). Third, if you found that a word was able to bypass the filter in your application, please submit a [bypass report](https://forms.gle/jaQkoPi54wayu9FA7). Finally, if you would like to help improve the filtering system, test the module on a ton of sentences and submit a [testing report](https://forms.gle/eXyUwdnqj9D8DgzB6) if you find any words that should be added or removed from the default filter. Testing is probably the most useful contribution you can make right now. We thank you for any contributions that you make to the module.

## Disclaimer
Please be aware that the code on GitHub may be newer than the version that is on [PyPI](https://pypi.org/project/content-filter/) since code may be uploaded to GitHub as a beta before it is uploaded officially to PyPI.

## License
The Content Filter module for Python is licensed under an [MIT license](https://github.com/MrDogeBro/content_filter/blob/master/LICENSE).