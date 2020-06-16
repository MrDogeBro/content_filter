# Python Content Filter
A basic but robust content filter for python. Content Filter allows you to easily detect if a piece of text 
contains any language it shouldn't. It also allows you to add your own words to filter for, remove words to filter for, 
or define a whole new list of words to filter for.

## Table of Contents
1. Installation
1. Usage
    1. Filtering Messages
    1. Adding Words to the Filter
    1. Removing Words from the Filter
    1. Using a Custom Filter
1. Examples

## Installation
To install Content Filter, enter the following command in any sort of terminal window as long as you have Python 3 installed on your computer.
```
$ pip install content-filter
```

## Usage
Listed below are the different functions and their uses. If the function returns any value, that is also listed.
#### Filtering Messages
To check a message with Content Filter, use the `.checkMessage()` function which accepts the message as a string to scan as its argument.
```python
import content_filter

content_filter.checkMessage('message')
# Returns bool of wether it found language from the filter in the message.
```
#### Adding Words to the Filter
To add words to the built in filter, use the `.addWords()` function which accepts the words to add as its argument. This can either be a single word as a string or multiple words as an array of strings. You can add words in multiple places in your file with the same function.
```python
import content_filter

content_filter.addWords('singleword')
# Adds a single string to the list of words to filter for

content_filter.addWords(['word1', 'word2', 'word3'])
# Adds an array of strings to the list of words to filter for
```
#### Removing Words from the Filter
To remove words from the built in filter, use the `.addExceptions()` function which accepts the words to remove as its argument. This can either be a single word as a string or multiple words as an array of strings. You can remove words in multiple places in your file with the same function.
```python
import content_filter

content_filter.addExceptions('singleword')
# Adds a single string to the list of words to filter for

content_filter.addExceptions(['word1', 'word2', 'word3'])
# Adds an array of strings to the list of words to filter for
```
#### Using a Custom Filter
To use a completely custom filter, use the `.useCustomList()` function which accepts the list of words you would like to use as its argument. This can either be a single word as a string or multiple words as an array of strings. You can only define this in one place in your file. You can use the `.addWords()` and `.addExceptions()` functions to add or remove words from your custom filter anywhere in the file still.
```python
import content_filter

content_filter.useCustomList('singleword')
# Use a single string as the list of words to filter for

content_filter.useCustomList(['word1', 'word2', 'word3'])
# Use an array of strings as the list of words to filter for
```

## Examples
In the examples listed below, words have been bleeped out with \*'s which the filter natively checks for but the same concept would appy with the real words.

#### Example #1
This is a basic example of how you could use content filter. In this example, we are just checking a message against the built in filter with no modification to the filter.
```python
import content_filter

content_filter.checkMessage('It is a beautiful day outside.')
# False

content_filter.checkMessage('Suck my d***!')
# True
```
#### Example #2
This is a bit more advanced usage. In this example, a word is being removed from the filter and a new one is being added to the filter. Then, we check to see the results after modifying the filter.
```python
import content_filter

content_filter.exceptions('s***')
content_filter.additionalls('today')

content_filter.checkMessage('Hello there!')
# False

content_filter.checkMessage('MOTHERF***ER!')
# True

content_filter.checkMessage('Holy s***!')
# False

content_filter.checkMessage('Hi, how are you doing today?')
# True
```
