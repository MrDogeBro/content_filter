# Python Content Filter
A basic but robust content filter for python. Content Filter allows you to easily detect if a piece of text 
contains any language it shouldn't. It also allows you to add your own words to filter for, remove words to filter for, 
or define a whole new list of words to filter for.

## Installation
To install Content Filter, enter the following command in any sort of terminal window as long as you have Python 3 installed on your computer.
```
$ pip install content-filter
```

## Examples
In the examples listed below, words have been bleeped out with \*'s which the filter natively checks for but the same concept would appy with the real words.

#### Example #1
This is a basic example of how you could use content filter. In this example, we are just checking a message against the built in filter with no modification to the filter.
<pre lang=python><code>import content_filter
  content_filter.checkMessage('It is a beautiful day outside.')
  # False

  content_filter.checkMessage('Suck my <em>d***</em>!')
  # True
</code></pre>
#### Example #2
This is a bit more advanced usage. In this example, a word is being removed from the filter and a new one is being added to the filter. Then, we check to see the results after modifying the filter.
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
