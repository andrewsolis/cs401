Code Organization
=================

Following standard Python3 code organization practices will make our code easier
to read by other developers, and by our future selves who are looking back to see
what we did. After going through this module, students should be able to:

* Organize code into ``main()`` functions
* Import functions into other scripts without executing the ``main()`` block
* Write functions in a generalizable way so they are reusable
* Use a shebang in their Python3 scripts to make them executable



Main Function
-------------

In many Python programs, you will find the developer has organized their code
into a ``main()`` function. Then, they will only call the ``main()`` function
if the variable ``__name__`` is equal to the string ``'__main__'``. For example:

.. code-block:: python3

    def main():
        # the meat of the main function goes here

    if __name__ == '__main__':
        main()


If this script is executed on the command line directly, then the internal
variable ``__name__`` will be set to the string ``'__main__'``. The conditional
evaluates as ``True`` and the ``main()`` function is called.

If this script is instead **imported into another script**, say, to reuse some of
the functions defined within, then the internal variable ``__name__`` will instead
be set to the name of the script. Thus, the ``main()`` function is not called,
but other functions defined in this script would be available.

Consider the script used for reading grocery items stored in a JSON file (called ``groceries.py``)
that also does a few computations:

.. code-block:: python3
    :linenos:

    import json

    def compute_average_quantity(a_list_of_dicts, a_key_string):
        total_quantity = 0
        for item in a_list_of_dicts:
            total_quantity += item[ a_key_string ]

        return float( total_quantity / len( a_list_of_dicts ) )

    def calc_total_price( price, quantity ):
        total_price = price * quantity
        return total_price

    with open('groceries.json', 'r') as f:
        grocery_data = json.load( f )


    print( compute_average_quantity( grocery_data['items'], 'quantity' ) )

    for row in grocery_data['items']:
        item_name = row['product_name']
        item_count = row['quantity']
        total_price = calc_total_price( float( row['price']), float( row['quantity'] ) )
        print(f'Total Price for {item_count} items of {item_name}: ${total_price:,.2f}')


To reorganize this code, we would put the file read operation and the two function
calls into a main function:

.. code-block:: python3
    :linenos:
    :emphasize-lines: 15,29-30

    import json

    def compute_average_quantity(a_list_of_dicts, a_key_string):
        total_quantity = 0
        for item in a_list_of_dicts:
            total_quantity += item[ a_key_string ]

        return float( total_quantity / len( a_list_of_dicts ) )

    def calc_total_price( price, quantity ):
        total_price = price * quantity
        return total_price


    def main():

        with open('groceries.json', 'r') as f:
            grocery_data = json.load( f )


        print( compute_average_quantity( grocery_data['items'], 'quantity' ) )

        for row in grocery_data['items']:
            item_name = row['product_name']
            item_count = row['quantity']
            total_price = calc_total_price( float( row['price']), float( row['quantity'] ) )
            print(f'Total Price for {item_count} items of {item_name}: ${total_price:,.2f}')

    if __name__ == "__main__":
        main()


If this code is imported into another Python3 script, that other script will have
access to the ``check_total_price()`` and ``compute_average_quantity()`` functions,
but it will not execute the code in the ``main()`` function.

EXERCISE
~~~~~~~~

Write a new script to import the above code, assuming that above code is saved
in a file called ``groceries.py``:

.. code-block:: python3
    :linenos:

    import groceries    # assumes it is in this directory, or installed in known location

    print( groceries.calc_total_price(3.50, 7.0) )
    print( groceries.calc_total_price(20.5, 3) )

.. tip::

   The main function does not have to be called literally ``main()``. But, if
   someone else is reading your code, calling it ``main()`` will certainly help
   orient the reader.




Generalizing Functions
----------------------

A good habit to get into while writing functions is to write them in a
*generalizable* way. This means writing them in such a way that they can be used
for multiple purposes or in multiple applications. The trick is to try to think
ahead about how else you might use the function, think about what form the input
data takes, and try not to hardcode indices or variable names.

``compute_average_quantity``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In our ``compute_average_quantity`` function, we knew we needed to send it *something*,
and we knew it needed to return an average amount. The main question was what form
should the input take?

.. code-block:: python3

   def compute_average_quantity( xyz ):
       # do some computation
       return(average_quantity)

We could have just sent the function the entire dictionary data structure, then
have it parse the data to get quantities out. But if we did that, we would also need
to hardcode the name of the main key ``'items'`` as well as the name
of the key referring to the quantities ``'quantity'``.


.. code-block:: python3

   # BAD
   def compute_average_quantity( a_dictionary ):
       total_quantity = 0.
       for item in a_dictionary['items']:
           total_quantity += float(item['quantity'])
       return(total_quantity / len(a_dictionary['items']) )

   print(compute_average_quantity(grocery_data))

It would be better practices to try and generalize this function
by sending it a list of dictionaries data structure and the
name of the key to extract. This way it can be used by others without needed
to adhere to the restrictions in the previous code.


.. code-block:: python3

   # GOOD
   def compute_average_quantity(a_list_of_dicts, a_key_string):
       total_quantity = 0.
       for item in a_list_of_dicts:
           total_quantity += float(item[a_key_string])
       return(total_quantity / len(a_list_of_dicts) )

   print(compute_average_quantity(grocery_data['items'] ,'quantity' ))




``calc_total_price``
~~~~~~~~~~~~~~~~~~~~

The ``calc_total_price`` function is very similar - we send it *something* and
it returns (or prints) a string.

.. code-block:: python3

   def calc_total_price( xyz )
       # run through some conditionals
       return(calculated_price)

Here we could have also sent a list of dictionaries along with the names of two
keys representing the quantities and price for a single item and print it here. That would have been ok.

.. code-block:: python3

   # NOT TERRIBLE
   def calc_total_price(a_list_of_dicts, price_key, quantity_key):
       for item in a_list_of_dicts:
            total_price = float(item[price_key]) * float(item[quantity_key]
            print(total_price)
       return

   calc_total_price(grocery_data['items'], 'price', 'quantity')


However, to make it even more generalizable, we could abstract one layer further
and just send it two floats: price and quantity. That would make the function
useful for our list of dictionaries data structure, and for one-off checks given
just a pair of floats:

.. code-block:: python3

    # BETTER
    def calc_total_price(price, quantity):
        total_price = price * quantity
        return(total_price)

   for row in grocery_data['items']:
       print(calc_total_price(float(row['price']), float(row['quantity'])))


EXERCISE
~~~~~~~~

Write a new function to count how many of each 'category' of items there is
in the list. The output should look something like:

.. code-block:: console

    type, number
    Frozen Foods : 3
    Bakery : 2 
    Meat : 1   
    Dairy : 2  
    Produce : 2

Consider carefully what inputs you are sending to the function. How can you write
it in a generalizable way?


Shebang
-------

A "shebang" is a line at the top of your script that defines what interpreter should
be used to run the script when treated as a standalone executable. You will often
see these used in Python, Perl, Bash, C shell, and a number of other scripting
languages. In our case, we want to use the following shebang, which should appear
on the first line of our Python3 scripts:

.. code-block:: python3

   #!/usr/bin/env python3

The ``env`` command simply figures out which version of ``python3`` appears first
in your path, and uses that to execute the script. We usually use that form instead
of, e.g., ``#!/usr/bin/python3.8`` because the location of the Python3 executable
may differ from machine to machine, whereas the location of ``env`` will not.

Next, you also need to make the script executable using the Linux/Mac command
``chmod``:

.. code-block:: console

   [terminal]$ chmod u+x groceries.py

.. note::

   Windows machines may not support this functionality.

That enables you to call the Python3 code within as a standalone executable without
invoking the interpreter on the command line:

.. code-block:: console

   [terminal]$ ./groceries.py

This is helpful to lock in a Python version (e.g. Python3) for a script that may
be executed on multiple different machines or in various environments.


Other Tips
----------

As our Python3 scripts become longer and more complex, we should put more thought
into how the different contents of the script are ordered. As a rule of thumb, try
to organize the different sections of your Python3 code into this order:

.. code-block:: python3

   # Shebang

   # Imports

   # Global variables / constants

   # Class definitions

   # Function definitions

   # Main function definition

   # Call to main function

Other general tips for writing code that is easy to read can be found in the
`PEP 8 Style Guide <https://www.python.org/dev/peps/pep-0008/>`_, including:

* Use four spaces per indentation level (no tabs)
* Limit lines to 80 characters, wrap and indent where needed
* Avoid extraneous whitespace unless it improves readability
* Be consistent with naming variables and functions

  * Classes are usually ``CapitalWords``
  * Constants are usually ``ALL_CAPS``
  * Functions and variables are usually ``lowercase_with_underscores``
  * Consistency is the key

* Use functions to improve organization and reduce redundancy
* Document and comment your code

.. note::

   Beyond individual Python3 scripts, there is a lot more to learn about organizing
   *projects* which may consist of many files. We will get into this later in the
   semester.



Additional Resources
--------------------

* `PEP 8 Style Guide <https://www.python.org/dev/peps/pep-0008/>`_
