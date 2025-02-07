Documentation
=============

As we have probably all heard before, good documentation is almost as important
(if not equally as important) as good code itself. You may have written some
elegant and powerful code to solve your problems today, but weeks or months
from now, that code may become functionally useless if you forget what it does or
how to call it. Python3 users have a special built-in tool at their disposal
called *docstrings* that make documenting functions easy. After going through
this module, students should be able to:

* Write well-crafted docstrings for all functions
* Add type hints to function definitions
* Write effective READMEs for a project

Docstrings
----------

Docstrings are special strings that appear immediately following function
definitions in our code. They should be surrounded by three double-quotation
marks on each side, and they may span multiple lines. For example:

.. code-block:: python3

   def a_function():
       """
       This is a docstring.
       """
       # code goes here
       return


The above is a valid docstring, but it is not a very helpful docstring. When you
write docstrings, at a minimum try to include the following sections:

1. A short description of the purpose of the function
2. A list of arguments, including type
3. A list of returned values, including type

A better template for a docstring (based on the
`Google Style Guide <https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>`_)
might look like:

.. code-block:: python3

   def a_function(arg1, arg2):
       """
       This function does XYZ.

       Args:
           arg1 (type): Define what is expected for arg1.
           arg2 (type): Define what is expected for arg2.

       Returns:
           result (type): Define what is expected for result.
       """
       # code goes here
       return(result)

The description should be succinct, yet complete. Arguments should be listed by
name and the expected type (e.g., bool, float, str, etc) should be stated. And
the return result(s) should be listed along with the expected type(s).

Let's look at one more example using a real function:

.. code-block:: python3

   def add_and_square(num1, num2):
       """
       Given two numbers, this function will first add them together, then square the sum
       and return the result.

       Args:
           num1 (float): The first number.
           num2 (float): The second number.

       Returns:
           result (float): The square of the sum of input arguments.
       """
       result = (num1+num2)**2
       return(result)


.. note::

   Notice above we are using more-or-less complete sentences with proper grammar.


Next, let's add docstrings to our ``groceries.py`` code we have been
working on:

.. code-block:: python3
    :linenos:
    :emphasize-lines: 5-17,26-36,42-44

    #!/usr/bin/env python3
    import json

    def compute_average_quantity(a_list_of_dicts, a_key_string):
        """
        Iterate through a list of dictionaries, pulling out values associated with
        a given key. Returns the average of those values.

        Args:
            a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                    same set of keys.
            a_key_string (string): A key that appears in each dictionary associated
                                with the desired value( will enforce float type).

        Returns:
            result (float): Average value.
        """

        total_quantity = 0
        for item in a_list_of_dicts:
            total_quantity += item[ a_key_string ]

        return float( total_quantity / len( a_list_of_dicts ) )

    def calc_total_price( price, quantity ):
        """
        Given a price and quantity, calculate to total price of items in stock and return
        the calculated amount.

        Args:
            price (float): price of an item
            quantity (float): amount of an item the grocery store has in stock

        Returns:
            total_price (float): total calculated price of item.
        """
        
        total_price = price * quantity
        return total_price

    def count_categories(a_list_of_dicts, a_key_string):
        """
        ???
        """
        categories_observed = {}
        for item in a_list_of_dicts:
            if item[a_key_string] in categories_observed:
                categories_observed[item[a_key_string]] += 1
            else:
                categories_observed[item[a_key_string]] = 1
        return(categories_observed)

    def main():
        with open('groceries.json', 'r') as f:
            grocery_data = json.load( f )

        print( compute_average_quantity( grocery_data['items'], 'quantity' ) )

        for row in grocery_data['items']:
            total_price = calc_total_price( float( row['price']), float( row['quantity'] ) ) 
            print(f'Total Price: {total_price:.2f}')

        print( count_categories( grocery_data['items'], 'category' ) )

    if __name__ == '__main__':
        main()


In general, your ``main()`` function usually does not need a docstring. It is
good habit to write the ``main()`` function simply and clearly enough that it is
self explanatory, with perhaps a few comments to help. If you do add a docstring
to  the ``main()`` function, you may write a few short summary sentences but omit
the Args and Returns sections.

EXERCISE
~~~~~~~~

Write the missing docstring for the ``count_categories()`` function above.


EXERCISE
~~~~~~~~

Open up the Python3 interactive interpreter. Import your ``groceries.py``
methods. Use the commands ``dir()`` and ``help()`` to find and read the docstrings
that you wrote.



Type Hints
----------

Type hints in function definitions indicate what types are expected as input and
output of a function. No checking actually happens at runtime, so if you send the
wrong type of data as an argument, the type hint itself won't cause it to return
an error. Think of type hints simply as documentation or annotations to help the
reader understand how to use a function.

.. warning::

   In the code blocks below, we omit docstrings for brevity only. Please keep
   including docstrings in your code.

Type hints should take form:

.. code-block:: python3

   def a_function(arg_name: arg_type) -> return_type:
       # code goes here
       return(result)

In the above example, we are providing a single argument called ``arg_name`` that
should be of type ``arg_type``. The expected return value should be ``return_type``.
Let's look at an example using a real function:

.. code-block:: python3

   def add_and_square(num1: float, num2: float) -> float:
       result = (num1+num2)**2
       return(result)


Next, add type hints to the function definitions of the ``groceries.py``
script (only showing snippets below):

.. code-block:: python3

   def compute_average_quantity(a_list_of_dicts: list[dict], a_key_string: str) -> float:

.. code-block:: python3

   def calc_total_price(price: float, quantity: float) -> float:

.. code-block:: python3

   def count_categories(a_list_of_dicts, a_key_string):  # what about this one?

Although Python3 does not check or enforce types at run time, there are other
tools that make use of type hints to check types at the time of development. For
example, some IDEs (including PyCharm) will evaluate type hints as you write code
and provide an alert if you call a function in a way other than what the type
hint suggests. In addition, there are Python3 libraries like *mypy* that can wrap
your Python3 programs and check / evaluate type hints as you go, provided errors
where types don't match.

.. warning::

   Be aware that there is some redundancy in the information contained in type hints
   and in the docstrings. Be careful not to let them get out of sync as your code
   evolves.



README
------

A README file should be included at the top level of every coding project you
work on. Websites like GitHub will automatically look for README files and render
them directly in the web interface. Markdown is probably the most common syntax
people use to write READMEs. It is very easy to create headers, code blocks,
tables, text emphases, and other fancy renderings to make the README pleasant and
easy to read.

.. note::

   In this class we ask you to include READMEs in each of your homework folders
   on GitHub. Each homework is essentially a standalone project, so a dedicated
   README for each is warranted.

At a minimum, plan to include the following sections in all of your READMEs:

* Title: a descriptive, self-explanatory title for the project.
* Description: a high-level description of the project that informs the reader
  what the code does, why it exists, what problem it solves, etc.
* Installation: As we advance into the semester our code bases will become more
  complex with more moving parts. Eventually we will need to start providing
  detailed instructions about getting the project working plus any requirements.
* Usage: The key here is **examples**! Show code blocks of what it looks like
  to execute the code from start to finish. Describe what output is expected and
  how it should be interpreted.

Other general advice includes:

* Use proper grammar and more-or-less complete sentences.
* Use headers, code blocks, and text emphases (e.g. bold, italics) to make the
  document readable. There are plenty of tools to preview Markdown before committing
  to GitHub, so plan to go through several cycles of editing -> previewing to
  make your README look nice.
* Be prepared to include other information about authors, acknowledgements, and
  licenses in the READMEs as appropriate
* Spend some time browsing GitHub and look for READMEs of other popular projects.
  There are many correct ways to write a README.

Remember, the README is your chance to document for yourself and explain to others
why the project is important, what the code is, and how to use it / interpret the
outputs. The advice above is general advice, but it is not one-size-fits-all.
Every project is different and ultimately your README may include other sections
or organization schemes that are unique to your project.




Additional Resources
--------------------

* `Google Style Guide for docstrings <https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>`_
* `Type hints spec <https://www.python.org/dev/peps/pep-0484/>`_
* `Mypy project <http://mypy-lang.org/index.html>`_
* `Markdown syntax <https://www.markdownguide.org/basic-syntax/>`_
* `Tips on writing a good README <https://www.makeareadme.com/>`_
