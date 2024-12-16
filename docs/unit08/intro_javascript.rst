.. role:: red

Introduction to Javascript
===========================

* Events
* Asynchronous Programming
* Promises

Setup and Installation
----------------------

You should still have your old directory from the previous module that covered HTML with the associated **index.html** file.
Navigate to your directory. You can use the ``index.html`` you created last time for Exercise 2 of the HTML, or
copy an update version that is done `here <https://raw.githubusercontent.com/andrewsolis/cs401/refs/heads/main/docs/unit08/resources/index_js.html>`_.

You can also copy the up-to-date css code `here <https://raw.githubusercontent.com/andrewsolis/cs401/refs/heads/main/docs/unit08/resources/styles/style_js.css>`_.

Run the following command to setup your small webserver, and navigate to http://localhost:8000/ to verify it is up and running.

.. code-block:: console

    [terminal]$ cd newsite
    [terminal]$ python -m http.server

What is JavaScript?
-------------------
JavaScript is a scripting language, or programming language if you prefer :), that is used to create and control dynamic website content. 
Using it you can control the behavior of different elements on a webpage, create animations, and more.
You can also use it to interact with Public APIs to make available data on your website.

Like how we've seen the other modules on HTML and CSS, it is a fundamental skill that opens your ability to not only
create static website, but also dynamic website and use available frameworks to streamline your development process.

Let's take a look at a simple hello world example.

Hello World Example
~~~~~~~~~~~~~~~~~~~

| You will recall in the very beginning of this Unit you created a folder called **scripts**.
| Within that folder create a new file called **script.js**.
| Then add the following to your ``index.html`` file just before the closing ``</body>`` tag.

.. code-block:: html

    <script src="scripts/script.js"></script>

This is similar to the ``<link>`` tag we used to link our CSS file, but instead of linking to a CSS file, we are linking to a JavaScript file.

Add the following code to your **script.js** file.

.. code-block:: javascript

    const myHeading = document.querySelector('h1');
    myHeading.textContent = 'Hello, World!';

| Reload your page and see if your text has changed.
| Here we see a simple example of how we are able to manipulate the content of our webpage using JavaScript.
| Let's take a closer look at how to use the language.

Syntax and Structure
--------------------
JavaScript is an interesting language in that it is similar to scripting like Python, but also has a lot of similarities to C and Java.

For example, to declare a variable in JavaScript you can use the ``let`` keyword.

.. code-block:: javascript

    let myVariable = 'Hello, World!';


.. note::

    | Semicolons are required when you need to separate statements on a single line, but aren't fully required.
    | For more details on how to use semicolons see `this article <https://www.codecademy.com/resources/blog/your-guide-to-semicolons-in-javascript/>`_.

Similar to C++ style, ``let`` means we are declaring a variable that is mutable and able to be reassigned.
If we want to declare a variable that is immutable, we can use the ``const`` keyword.

.. code-block:: javascript

    const myConstant = 'Hello, World!';

You can also use the ``var`` keyword, but it is not recommended as it has some quirks that can lead to bugs in your code and is an older style of devleopment.

.. warning::

    JavaScript is a loosely typed language, meaning you don't have to declare the type of a variable when you declare it.
    This can lead to some unexpected behavior if you are not careful, and means you can also overwrite the type of a variable.
    Be mindful when you are working with different data types.

There are many different `data types <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures/>`_ available in Javascript:

    +----------+---------------------------------------------------+-------------------------------------------------------------------+
    | Variable | Details                                           | Example                                                           |
    +==========+===================================================+===================================================================+
    | String   | similar to string types                           | ``let name = 'Andrew';``                                          |
    +----------+---------------------------------------------------+-------------------------------------------------------------------+
    | Number   | double precision float                            | ``const value = 10;``                                             |
    +----------+---------------------------------------------------+-------------------------------------------------------------------+
    | Boolean  | True/False                                        | ``let value = true;``                                             |
    +----------+---------------------------------------------------+-------------------------------------------------------------------+
    | Array    | link                                              | ``let content = [23, "Stephen", {name : "Stu"}]``                 |
    +----------+---------------------------------------------------+-------------------------------------------------------------------+
    | Object   | All elements in JS are objects that can be stored | ``const myHeading = document.querySelector('h1');``               |
    +----------+---------------------------------------------------+-------------------------------------------------------------------+

.. note::
    Arrays do not have to be the same type for all elements. Be mindful of this when using arrays for data.

Comments can be added toa page using the ``//`` syntax for single line comments, or the ``/* */`` syntax for multi-line comments.

.. code-block:: javascript

    // This is a single line comment
    /* This is a multi-line comment
    that spans multiple lines */

However, javascript can become more complex once you explore the topics of functions, objects, and events.

Conditionals and Loops
----------------------

Like other programming languages, JavaScript has conditional statements and loops that allow you to control the flow of your program.

For example, you can use the ``if`` statement to check if a condition is true.

.. code-block:: javascript

    let value = 10;

    if (value > 5) {
        alert('Value is greater than 5');
    } else {
        alert('Value is less than or equal to 5');
    }

.. note::
    The ``alert`` function is a built-in function that allows you to display a message to the user.
    This appears as a pop-up on the screen and is available on most browsers.

You can also use the ``switch`` statement to check multiple conditions.

.. code-block:: javascript

    let value = 10;

    switch (value) {
        case 5:
            console.log('Value is 5');
            break;
        case 10:
            console.log('Value is 10');
            break;
        default:
            console.log('Value is not 5 or 10');
    }

Loops are also available in JavaScript, and you can use the ``for`` loop to iterate over a range of values.

.. code-block:: javascript

    for (let i = 0; i < 10; i++) {
        console.log(i);
    }

You can also use the ``while`` loop to iterate over a range of values.

.. code-block:: javascript

    let i = 0;

    while (i < 10) {
        console.log(i);
        i++;
    }

There are also other types of loops available in JavaScript, such as the ``do...while`` loop, and the ``for...in`` loop.

.. note::
    ``console.log`` is a built-in function that allows you to print to the console.
    You will most certainly be using this to debug your code.
    You can learn more about built-in objects and their methods available `here <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects>`_.

Functions & Events
------------------

Functions
~~~~~~~~~

Functions in JavaScript are similar to functions in other languages, but have some unique features that make them powerful.
Some of these are built-in by the browser, and some you can define yourself.
To define your own function you can use the ``function`` keyword.

For example, say we wanted to take to strings and create a "Full Name":

.. code-block:: javascript

    function fullName(firstName, lastName) {
        return firstName + ' ' + lastName;
    }

    console.log(fullName('Andrew', 'Solis'));

**Functions** that are a part of objects are called **methods**.

Though you can create functions this way, there are a few other ways to define functions in JavaScript.

.. code-block:: javascript

    ( function() {
        console.log('Hello, World!');
    });
    

Lecture Outline
----------------

4. Functions
    * Function Declaration and Expression
    * Arrow Functions
    * Scope and Closures
6. DOM Manipulation
    * Selecting Elements
    * Modifying Elements
    * Event Handling
7. Asynchronous JavaScript
    * Callbacks
    * Promises
    * Async/Await
8. Debugging and Best Practices
    * Common Errors
    * Debugging Tools
    * Writing Clean Code


Additional Resources
--------------------
* Some of this materials is based on Mozilla `Learn Web Development <https://developer.mozilla.org/en-US/docs/Learn>`_
* Try and avoid `callback hell<http://callbackhell.com/>`_