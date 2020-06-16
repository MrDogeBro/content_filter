# Python Content Filter
A basic but robust content filter for python. Content Filter allows you to easily detect if a piece of text 
contains any language it shouldn't. It also allows you to add your own words to filter for, remove words to filter for, 
or define a whole new list of words to filter for.

## Installation
To install Content Filter, enter the following command in a terminal window.
```
$ pip install content-filter
```

## Usage

```python
import content_filter

content_filter.exceptions('s***')
content_filter.additionalls('today')

content_filter.checkMessage('Hello there!')
# False

content_filter.checkMessage('_MOTHERF***ER_!')
# True

content_filter.checkMessage('Holy _s***_!')
# False

content_filter.checkMessage('Hi, how are you doing _today_?')
# True
```