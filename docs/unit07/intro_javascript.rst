.. role:: red

Introduction to Javascript
===========================

We've learned how to create basic static website using HTML, and learned some basic ways to style these websites using CSS.
But one of the powerful things of the web is adding interactivity to a website. Think dropdowns, buttons, charts, animations, and more.
While we could program these with some modern CSS and HTML, most modern browsers use Javascript to add interactivity to a page.
This can be simple actions for buttons, to more complex actions such as whole page animations, and even video games.
In the following module we will explore some basic usecases of Javascript, along with best practices.

After this module, students should be able to:

* Understand the basics of Javascript
* Know the general syntax and structure
* Understand how to use functions, events, and Callbacks
* Understand the DOM and how to manipulate it
* Know and how to use promises
* How to debug code and best practices

Setup and Installation
----------------------

You should still have your old directory from the previous module that covered HTML with the associated **index.html** file.
Navigate to your directory. You can use the ``index.html`` you created last time for Exercise 2 of the HTML, or
copy an update version that is done `here <https://raw.githubusercontent.com/andrewsolis/cs401/refs/heads/main/web/index_js.html>`_.

You can also copy the up-to-date css code `here <https://raw.githubusercontent.com/andrewsolis/cs401/refs/heads/main/web/styles/style.css>`_.

Run the following command to setup your small webserver, and navigate to http://localhost:8000/ to verify it is up and running.

.. code-block:: console

    [terminal]$ cd newsite
    [terminal]$ python -m http.server

What is JavaScript?
-------------------
JavaScript is a scripting language, or programming language if you prefer, that is used to create and control dynamic website content. 
Using it you can control the behavior of different elements on a webpage, create animations, and more.
You can also use it to interact with Public APIs to make available data on your website.

Like how we've seen the other modules on HTML and CSS, it is a fundamental skill that opens your ability to not only
create static website, but also dynamic website and use available frameworks to streamline your development process.

Let's take a look at a simple hello world example.

Hello World Example
~~~~~~~~~~~~~~~~~~~

| You will recall in the very beginning of this Unit you created a folder called **scripts**.
| Within that folder create a new file called **script.js**.
| Then add the following to your ``index.html`` file just before the closing ``</head>`` tag.

.. code-block:: html

    <script src="scripts/script.js" defer></script>

This is similar to the ``<link>`` tag we used to link our CSS file, but instead of linking to a CSS file, we are linking to a JavaScript file.

.. note::
    You can learn more about what *defer* and *async* do at this great stackoverflow explantion - `stackoverflow <https://stackoverflow.com/questions/436411/where-should-i-put-script-tags-in-html-markup>`_.

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
    | Array    | list of any type of elements                      | ``let content = [23, "Stephen", {name : "Stu"}]``                 |
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

Functions, Events, & Callbacks
------------------------------

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

Anonymous and Arrow Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Though you can create functions this way, there are a few other ways to define functions in JavaScript.

.. code-block:: javascript

    ( function() {
        console.log('Hello, World!');
    });
    
| This type of function is called an **anonymous function** because it has no name.
| These functions are common for functions that are passed as arguments to other functions.

| For example, say we want to print the type of key that a user presses on a keyboard when typing into a text box.
| In order to detect this we add an **event listener** to the textbox object.

Add the following code your html file.

.. code-block:: html

        ...
        <input type="text" id="myInput">
    </main>

Then add the following code to your **script.js** file.

.. code-block:: javascript

    const input = document.getElementById('myInput');

    input.addEventListener('keypress', function(event) {
        console.log(event.key);
    });

Here we are passing an anonymous function to the ``addEventListener``.

There is also an alternative form you can use, called an **arrow function**.

.. code-block:: javascript

    input.addEventListener('keypress', (event) => {
        console.log(event.key);
    });

Arrow functions are a more concise way to define functions, and are often used in modern JavaScript code.

If your function only takes one parameter, you can omit the parentheses.

.. code-block:: javascript

    input.addEventListener('keypress', event => {
        console.log(event.key);
    });

If your function only has one line of code, you can omit the curly braces, as well as the return statement.

.. code-block:: javascript

    input.addEventListener('keypress', event => console.log(event.key));


.. important::
    It's important to note that in Javascript functions like these are not called sequentially, 
    but rather are called when the event is triggered, in this case when a key is pressed.

    These functions are known as **callback functions**.


Exercise 1
~~~~~~~~~~~

Now we will test your understanding of events and callbacks.

1. Create a new `button <https://www.w3schools.com/tags/tag_button.asp>`_ element in your HTML file. Give it an id.
2. In your *script.js* file, select the element using the same way we selected the input in the previous example.
3. Add an event listener to the button that listens for a ``click`` event.
4. When the button is clicked, display a console message saying "Button clicked!".

.. note::
    Instead of attaching an event listener completely from javascript, you can also add an event listener directly in the HTML file.
    For example, you can add an ``onclick`` attribute to the button element in your HTML file.

        <button id="myButton" onclick="clickHandler()">Click me</button>
    
    Then, in your *script.js* file, you can define the ``clickHandler`` function to handle the click event.
    
        function clickHandler() {
            console.log('Button clicked!');
        }
    This is a more traditional way of handling events in HTML, but it is generally recommended to use event listeners in JavaScript for better separation of concerns.
    Also in javascript you can add more events to a single element, whereas in HTML you can only have specify one click event per element.

Scope and Closures
~~~~~~~~~~~~~~~~~~

| Scope in JavaScript refers to the visibility of variables within a program.
| When you create a function, you create a new scope, and variables declared within that function are only accessible within that scope.
| The top-level outside all functions is called the **global scope**.

For example, place the following code in your **script.js** file.

.. code-block:: javascript

    // Global scope
    let globalVar = 'I am a global variable';

    input.addEventListener('keypress', (event) => 
    {
        console.log(event.key)
        // Local scope within EventListener function
        let outerVar = 'I am an outer variable';
        
        const innerFunction = () => {
            // Local scope within innerFunction
            let innerVar = 'I am an inner variable';
    
            console.log(globalVar); // Accessible
            console.log(outerVar);  // Accessible
            console.log(innerVar);  // Accessible
        };
    
        innerFunction();
        console.log(globalVar); // Accessible
        console.log(outerVar);  // Accessible
        // console.log(innerVar); // Not accessible, would cause an error

    });

    console.log(globalVar); // Accessible
    // console.log(outerVar); // Not accessible, would cause an error
    // console.log(innerVar); // Not accessible, would cause an error


In this example, we have three different scopes

* global scope
* scope of the event listener function
* scope of the inner function.

Variables declared in the global scope are accessible from all scopes, but variables declared in the inner function are only accessible within that function. 
Give it a try and see what happens when you try to access variables outside of their scope.

DOM Manipulation and Events
---------------------------

| The **Document Object Model (DOM)** a data representation of the objects that makeup a webpage.
| It is a tree-like structure that represents the different elements on a webpage, and allows you to interact with those elements using JavaScript.
| We actually saw this previously when we used the ``document`` object to select our input element on the page.

Here we will go into further detail of selecting DOM elements, modifying them, and handling events.

Selecting Elements
~~~~~~~~~~~~~~~~~~

There are two methods that are generally recommended for selecting DOM elements

1. `querySelector() <https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector>`_ - This returns the first matching ``Element`` in a nodes tree.  
2. `querySelectorAll() <https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll>`_ - This returns a ``NodeList`` (array) of all matching elements in a nodes tree.

.. note::
    There are other methods available for selecting elements, but these are the most commonly and best recommended methods.
    To see more options available looke here - https://www.w3schools.com/js/js_htmldom_elements.asp.


For example, say we wanted to select those `li` elements with a class of `nav-link` in our html file.

.. code-block:: javascript

    // Select the first paragraph element
    const firstLink = document.querySelector('.nav-link');
    console.log(firstLink.textContent); // Output: Home

    // Select all paragraph elements
    const allLinks = document.querySelectorAll('.nav-link');
    allLinks.forEach(paragraph => {
        console.log(paragraph.textContent);
    });
    // Output: 
    // Home
    // Our Team
    // About

Modifying Elements
~~~~~~~~~~~~~~~~~~

Once you have selected elements using `querySelector` or `querySelectorAll`, you can modify them in various ways. 

Exercise 2
~~~~~~~~~~~

Now that you have a basic understanding of how to select elements, let's try modifying them.
Go through each example and try selecting an element in your HTML page and modifying it.

1. Changing the text content of an element:

.. code-block:: javascript

    const firstParagraph = document.querySelector('.text');
    firstParagraph.textContent = 'New text content';

2. Changing the HTML content of an element:

.. code-block:: javascript

    const firstParagraph = document.querySelector('.text');
    firstParagraph.innerHTML = '<strong>New HTML content</strong>';

3. Changing the style of an element:

.. code-block:: javascript

    const firstParagraph = document.querySelector('.text');
    firstParagraph.style.color = 'blue';
    firstParagraph.style.fontSize = '20px';

4. Adding a class to an element:

.. code-block:: javascript

    const firstParagraph = document.querySelector('.text');
    firstParagraph.classList.add('new-class');

5. Removing a class from an element:

.. code-block:: javascript

    const firstParagraph = document.querySelector('.text');
    firstParagraph.classList.remove('text');

6. Modifying multiple elements using `querySelectorAll`:

.. code-block:: javascript

    const allParagraphs = document.querySelectorAll('.text');
    allParagraphs.forEach(paragraph => {
        paragraph.style.color = 'green';
    });

Event Handling
~~~~~~~~~~~~~~

Event handling in JavaScript allows you to execute code in response to user interactions or other events that occur in the browser. Here are some examples:

1. Handling a button click event:

.. code-block:: html

    <button id="myButton">Click me</button>

.. code-block:: javascript

    const button = document.getElementById('myButton');
    button.addEventListener('click', () => {
        alert('Button was clicked!');
    });

2. Handling a form submission event:

.. code-block:: html

    <form id="myForm">
        <input type="text" id="myInput" />
        <button type="submit">Submit</button>
    </form>

.. code-block:: javascript

    const form = document.getElementById('myForm');
    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent the form from submitting
        const input = document.getElementById('myInput');
        alert(`Form submitted with input: ${input.value}`);
    });

3. Handling a mouseover event:

.. code-block:: html

    <div id="myDiv">Hover over me</div>

.. code-block:: javascript

    const div = document.getElementById('myDiv');
    div.addEventListener('mouseover', () => {
        div.style.backgroundColor = 'yellow';
    });

Promises
--------

A **Promise** in JavaScript is an object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value. Promises provide a cleaner, more flexible way to handle asynchronous operations compared to traditional callback functions.

Creating a Promise
~~~~~~~~~~~~~~~~~~

You can create a promise using the `Promise` constructor, which takes a function with two parameters: `resolve` and `reject`.

.. code-block:: javascript

    const myPromise = new Promise((resolve, reject) => {
        const success = true; // Simulate an asynchronous operation

        if (success) {
            resolve('Operation was successful!');
        } else {
            reject('Operation failed.');
        }
    });

Consuming a Promise
~~~~~~~~~~~~~~~~~~~

To consume a promise, you use the `then` and `catch` methods. The `then` method is called when the promise is resolved, and the `catch` method is called when the promise is rejected.

.. code-block:: javascript

    myPromise
        .then((message) => {
            console.log(message); // Output: Operation was successful!
        })
        .catch((error) => {
            console.error(error); // Output: Operation failed.
        });

Chaining Promises
~~~~~~~~~~~~~~~~~

You can chain multiple `then` methods to handle a sequence of asynchronous operations.

.. code-block:: javascript

    const promise1 = new Promise((resolve) => {
        setTimeout(() => resolve('First operation complete'), 1000);
    });

    const promise2 = new Promise((resolve) => {
        setTimeout(() => resolve('Second operation complete'), 2000);
    });

    promise1
        .then((message) => {
            console.log(message); // Output: First operation complete
            return promise2;
        })
        .then((message) => {
            console.log(message); // Output: Second operation complete
        });

Error Handling
~~~~~~~~~~~~~~

You can handle errors in a promise chain using the `catch` method.

.. code-block:: javascript

    const faultyPromise = new Promise((resolve, reject) => {
        setTimeout(() => reject('Something went wrong'), 1000);
    });

    faultyPromise
        .then((message) => {
            console.log(message);
        })
        .catch((error) => {
            console.error(error); // Output: Something went wrong
        });

Promise.all
~~~~~~~~~~~

The `Promise.all` method takes an array of promises and returns a single promise that resolves when all of the promises in the array have resolved, or rejects if any of the promises in the array reject.

.. code-block:: javascript

    const promiseA = Promise.resolve('A');
    const promiseB = Promise.resolve('B');
    const promiseC = Promise.resolve('C');

    Promise.all([promiseA, promiseB, promiseC])
        .then((values) => {
            console.log(values); // Output: ['A', 'B', 'C']
        });

.. note::
    
    Though Promises have their uses most front-end changes usually are fine with using callbacks and anonymous functions.
    However, if you start to use more complex APIs, and use a Javascript based framework such as `node.js <https://nodejs.org/en>`_ you will find promises to be very useful.

Debugging and Best Practices
-----------------------------

Common Errors
~~~~~~~~~~~~~

When writing JavaScript, you may encounter common errors such as:

1. **Syntax Errors**: These occur when there is a mistake in the code syntax.
   
   .. code-block:: javascript

       console.log('Hello, World!') // Missing semicolon

2. **Reference Errors**: These occur when you try to use a variable that has not been declared.
   
   .. code-block:: javascript

       console.log(nonExistentVariable); // nonExistentVariable is not defined

3. **Type Errors**: These occur when a value is not of the expected type.
   
   .. code-block:: javascript

       const num = 5;
       num.toUpperCase(); // num.toUpperCase is not a function

Debugging Tools
~~~~~~~~~~~~~~~

To debug JavaScript code, you can use the following tools:

1. **Console**: The `console.log` method is commonly used to print messages to the console for debugging purposes.
   
   .. code-block:: javascript

       console.log('Debug message');

2. **Browser Developer Tools**: Most modern browsers come with built-in developer tools that allow you to inspect the DOM, debug JavaScript, and analyze network activity.
   
   - In Chrome, you can open the developer tools by pressing `Ctrl+Shift+I` or `Cmd+Opt+I` on Mac.
   - In Firefox, you can open the developer tools by pressing `Ctrl+Shift+I` or `Cmd+Opt+I` on Mac.

3. **Breakpoints**: You can set breakpoints in your code to pause execution and inspect the current state of variables.
   
   .. code-block:: javascript

       debugger; // This will pause execution at this line

Writing Clean Code
~~~~~~~~~~~~~~~~~~

To write clean and maintainable JavaScript code, follow these best practices:

1. **Use meaningful variable names**: Choose descriptive names for your variables to make your code more readable.
   
   .. code-block:: javascript

       let userName = 'Andrew';

2. **Keep functions small**: Write small, single-purpose functions to make your code easier to understand and test.
   
   .. code-block:: javascript

       function calculateSum(a, b) {
           return a + b;
       }

3. **Use comments**: Add comments to explain complex logic or important sections of your code.
   
   .. code-block:: javascript

       // Calculate the sum of two numbers
       function calculateSum(a, b) {
           return a + b;
       }

4. **Consistent formatting**: Use consistent indentation and formatting throughout your code.
   
   .. code-block:: javascript

       if (condition) {
           // Do something
       } else {
           // Do something else
       }

5. **Avoid global variables**: Minimize the use of global variables to reduce the risk of conflicts and bugs.
   
   .. code-block:: javascript

       (function() {
           let localVariable = 'I am local';
           console.log(localVariable);
       })();


Additional Resources
--------------------
* Some of this materials is based on Mozilla `Learn Web Development <https://developer.mozilla.org/en-US/docs/Learn>`_
* Try and avoid `callback hell <http://callbackhell.com/>`_