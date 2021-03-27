Using the Filter
================

Creating a Filter Object
------------------------

Creating a :ref:`filter-object` is really simple. Just import the filter class from the module and your ready to go. You can now create a filter object and use that to filter messages.
You can also have multiple filter objects which allows you to have multiple different configured filters in one file.

.. code-block:: python

    from content_filter import Filter

    Filter()
    # creates a filter object

Filtering Messages
------------------

Once you have created a filter object, all you need to do is call the check function. The only parameter you need to pass into the check function is the string you want it to filter for. 
After you pass in a string, it will filter the message based on the current configuration. This will return a :ref:`check-object` where you can then get the results in different forms.
For example, if you wanted to get a bool of wether the filter found anything, you can just use the as_bool property of the check object.

.. code-block:: python

    from content_filter import Filter

    filter = Filter()

    filter.check('message here')
    # returns a Check object

    filter.check('message here').as_bool
    # returns a bool of True if it found anything, False if not

Adding or Removing words from the Filter
----------------------------------------

To add or remove words from the filter, just call the add_words function or the add_exceptions function on the filter object you created. The only parameter you need to pass in for both
of these functions is a list of strings. The add_words function adds the specified words on top of the default list and the add_exceptions function ignores the specified words in the default list.
These functions can be called multiple times for a single filter object.

.. code-block:: python

    from content_filter import Filter

    filter = Filter()

    filter.add_words(['word1', 'word2', 'word2'])
    # adds words to default filter

    filter.add_exceptions(['word1', 'word2', 'word2'])
    # ignores words in default filter

Using a Custom List
-------------------

To use a custom list of words to filter for, you pass in your list when you initialize the filter object. This needs to be a list of strings to filter for. Then, whenever you check a message, 
it will use the list you provided to the filter object instead of the default list. Note that these will all be filtered like they are in the mainFilter, not the conditionalFilter (:ref:`main-vs-conditional` for more details).


.. code-block:: python

    from content_filter import Filter

    filter = Filter(word_list=['word1', 'word2', 'word3'])
    # tells filter to use this list of words to filter for

.. _using-a-custom-list-file:

Using a Custom List File
------------------------

To use a custom list file for filtering, you pass in the path to the custom list file when you initialize the filter object. This is in the form of a string and can be a relative or absolute path.
This file must be a JSON file however, otherwise the filter can't use the file. The structure of this file however, is important. To learn how to structure your custom list file, check out :ref:`custom-list-file-structure`.

.. code-block:: python

    from content_filter import Filter

    filter = Filter(list_file='./filter_list.json')
    # gives the filter the relative path to the custom list file

    filter = Filter(list_file='~/Documents/Python/tests/filter_list2.json')
    # gives the filter the absolute path to the custom list file

.. _custom-list-file-structure:

Custom List File Structure
--------------------------

If you are using a custom list file, it needs to follow a specific structure for the JSON, otherwise the filter can't use the file. Below is the JSON structure you must follow when using a custom list file.
For each item in the main and conditional filter, there is a `"find"`, a `"word"`, and a `"censored"` as you can see below. The `"find"` is the word the filter actually is looking for. The `"word"` is the actual word it represents,
since the find is not always the complete word. And the `"censored"` is just a censored version of the word that is returned in checks. 

There also is a `"require_space"` in the conditional filter. This is just a bool that tells the filter wether the word needs to have a space before it or not for it to be picked up in the conditional filter. 
For more information on the main and conditional filter, check out :ref:`main-vs-conditional`.

There also is a don't filter. This is just a list of words that will be ignored in messages when filtering. This is useful is a word is picking up in one of the other two filters when you don't want it to.

To not put any words in a filter, just leave it blank. If would would like an example of the JSON structure, feel free to check out the default filter file on our `GitHub <https://github.com/MrDogeBro/content_filter>`_.

.. code-block:: json

    {
        "mainFilter": [
            { "find": "find", "word": "word", "censored": "censored" },
            { "find": "helo", "word": "hello", "censored": "h3110" }
        ],
        "dontFilter": ["word"],
        "conditionFilter": [
            {
            "find": "find",
            "word": "word",
            "censored": "censored",
            "require_space": true
            }
        ]
    }

.. _main-vs-conditional:

Main vs. Conditional Filter
---------------------------

The main difference between the main and conditional filters is how strictly the filtration is performed. The main filter performs more checks, such as use of repeated characters, 
whereas the conditional filter only checks exactly what it is given.

.. code-block::

    Word to Filter: 'testing'

    Main Filter: 'testing' - True

    Main Filter: 'tesssssstinnnnng' - True

    Conditional Filter: 'testing' - True

    Conditional Filter: 'tesssssstinnnnng' - False
