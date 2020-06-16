"""
Python Content Filter
~~~~~~~~~~~~~~~~~~~~

A module that allows you to easily detect if a piece of text
contains any language it shouldn't. It also allows you to add
your own words to filter for, remove words to filter for, or
define a whole new list of words to filter for.

copyright: (c) 2020-2020 MrDogeBro |
license: MIT, see LICENSE for more details.

"""

__title__ = 'Content Filter'
__author__ = 'MrDogeBro'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020-2020 MrDogeBro'
__version__ = '1.0.0'

from .filter import checkMessage, addExceptions, addWords, useCustomList