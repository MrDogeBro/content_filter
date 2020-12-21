Quickstart
==========

This will walk you through the basic usage of content filter.

Filtering a Message
-------------------

Filtering a message using the default list of words is super simple.

First, your going to need to import the :ref:`filter-object`.

.. code-block:: python

    from content_filter import Filter

Next, were going to need to create a filter instance and assign it to a variable.

.. code-block:: python

    filter = Filter()

Now that we have created a filter instance and assigned it to a variable, we can check any message we like against the default filter.
All you need to do if you want to check a message is call the check function. In the parameters for this function, you will need to pass in the message you want to filter in the form of a string.

.. code-block:: python

    filter.check('this is the message that will get checked against the default filter')

When we use the check function to check a message, it will return a check object. This allows us to request the results in two different ways.
For this example, we will request a bool of wether it found anything in the message or not. If you would like to find out more about the check object and the results it can give, check out the :ref:`check-object`.

.. code-block:: python

    filter.check('message to filter').as_bool

Thats it! Now you have filtered a message and got a bool back of wether the filter found anything in the message. Now you can do whatever you would like with the result of the filter.
For more info on using the filter and more advanced uses, check out :doc:`Using the Filter <./usage>` or the :doc:`examples <./examples>`.