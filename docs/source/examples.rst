Examples
========

Below are a few examples to hopefully help you out.

Basic Filtering
---------------

In this basic example, all we are doing is checking a message that is a variable against the default filter. If anything is found, something happens.
If nothing is found, something else happens.

.. code-block:: python

    from content_filter import Filter

    message = 'hello there this is a test message'
    filter = Filter()

    if filter.check(message).as_bool:
        # handle filter finding something
    else:
        # handle filter not finding anything

Filtering with a Custom List
----------------------------

In this example, we tell the filter to use a custom list of words provided to filter with. Then, we check a message using this filter.

.. code-block:: python

    from content_filter import Filter

    filter_list = ['hello', 'anyword', 'wordhere', 'putyourwordshere']

    filter = Filter(word_list=filter_list)
    # pass in the custom list of words

    filter.check('anyword').as_bool
    # returns True because word is in the custom list

    filter.check('f***').as_bool
    # returns False because word isn't in the custom list
    # even though its in the default list

Filtering Using a Custom List File
----------------------------------

In this example, we will use a custom list file to filter with. The custom list file needs to be a JSON file and follow the :ref:`custom-list-file-structure`.
For more information on using custom list files, check out :ref:`using-a-custom-list-file`.

*custom_list.json*

.. code-block:: json

    {
        "mainFilter": [
            { "find": "helo", "word": "hello", "censored": "h3110" },
            { "find": "hi", "word": "hi", "censored": "h1" },
            { "find": "wordhere", "word": "wordhere", "censored": "w0rdh3r3" }
        ],
        "dontFilter": [],
        "conditionFilter": []
    }

*filter.py*

.. code-block:: python

    from content_filter import Filter

    filter = Filter(list_file='./custom_list.json')
    # pass in the custom file

    filter.check('wordhere').as_bool
    # returns True because word is in the custom file

    filter.check('s***').as_bool
    # returns False because word isn't in the custom list
    # even though its in the default list