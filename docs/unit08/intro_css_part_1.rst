.. role:: red

Introduction to CSS: Part 1
===========================

In this section, we will explore CSS and how it helps with designing a website.
this includes problems such as coloring (text/background), making the content display at a certain location,
and "decorating" with images and color schemes. After this module, students should be able to:

* Understand the basics of CSS
* Understand how to apply CSS to a webpage
* Understand the different types of CSS selectors
* Understand how to use CSS units


Setup and Installation
----------------------

You should still have your old directory from the previous module that covered HTML with the associated **index.html** file.
Navigate to your directory. You can use the ``index.html`` you created last time for Exercise 2 of the HTML, or
copy an update version that is done `here <https://raw.githubusercontent.com/andrewsolis/cs401/refs/heads/main/docs/unit08/resources/index_css.html>`_.


Run the following command to setup your small webserver, and navigate to http://localhost:8000/ to verify it is up and running.

.. code-block:: console

    [terminal]$ cd newsite
    [terminal]$ python -m http.server


What is CSS?
------------

CSS, or Cascading Style Sheets, are similar to HTML, in that it is not a programming language.
However, it is also not a markup language. It is rather a **style sheet language**. It is used
to style HTML elements. For example, say we wanted to make all ``p`` tags red.

.. code-block:: css
    :linenos:

    p {
        color: red;
    }

But where exactly do we put this? Notice how you created a folder in the previous material on HTML called ``styles``. 
Open it up and place a new file called **style.css**. Then, paste the following line inside your **index.html** file within
the ``<head>`` tag.

.. code-block:: HTML
    :linenos:

    <link href="styles/style.css" rel="stylesheet" />

All of your paragraph tags should now be red. Be sure to reload the page if needed.

Let's take a closer look at how CSS is used.

Anatomy of CSS
~~~~~~~~~~~~~~

.. figure:: ./images/css.jpg
    :width: 600px
    :align: center

    CSS Anatomy

From the image above we can see a breakdown of a CSS **ruleset**. Let's analyze the individual parts.

- **selector** - The html element type to be styled. 
- **Declaration** - Our single rule is to change the color of the text to red. We have a single declaration here, but there can be multiple for a CSS ruleset.
- **Property** - Which property we like to change or apply to our selector.
- **Property Value** - the value of the property we wish to set.

Instead of just setting the color, let's try setting a few more properties.

.. code-block:: css
    :linenos:

    p {
        color: red;
        background-color:rgb(55, 43, 226);
        height: 100px;
    }

.. note::

    color attributes can be set by many basic colors by name, rgb, hsl, and hex. To learn more about colors click here:  `CSS Colors <https://www.w3schools.com/css/css_colors.asp>`_.

Say instead of just selecting all the ``p`` elements we wanted to select other elements on our page and change their color.

.. code-block:: css
    :linenos:

    p,
    li,
    h3 {
        color: red;
    }


.. warning::

    Try to make sure that certain rules are set for a particular element and not set also in other places. This can create conflicts where you deal with heirarchy of which rules to apply, which
    is normal but can be a pain when starting to learn about CSS.

Types of Selectors
~~~~~~~~~~~~~~~~~~

Up to this point we have only been applying our rulset to HTML elements. However, they are other selectors that are available through CSS that can help make our selections more specific.

Element
^^^^^^^

**Element** selectors select all elements of a given type. We have seen these before when we specified we wanted to apply something to all ``p`` elements.

Example

.. code-block:: css
    :linenos:
    :emphasize-lines: 1,5

    p{
        color: red;
    }

    h1, h2, h3 {
        font-size: 200%
    }

Class
^^^^^

**Class** selector is one of the most common selectors used in CSS. Elements on the page are given a name for the ``class`` attribute of an html element.
Multiple classes can be applied to a single html element, by simply spacing out the class names.
Say we wanted all our titles to have a class, and use a class to change the text color.

.. code-block:: html
    :linenos:
    :emphasize-lines: 2, 7, 10

    <header>
        <h1 class="title gr">Planet Express!</h1>
        ...
    </header>
    ...
    <main>
        <h2 class="title or">Main Content</h2>
        ...
        <aside>
            <h3 class="title bl">Related content</h3>
            ...
        </aside>
    </main>
    <footer>
        <p>Copyright Planet Express 2024</p>
    </footer>

We then specify a class in our ``style.css`` file using a period (**.**) in the selector place.

.. code-block:: css
    :linenos:

    .title {
        font-style: italic;
    }

    .gr {
        color: green;
    }

    .or {
        color: orange;
    }

    .bl {
        color: blue;
    }

Try changing the color of all of your headlines to different colors using ``classes``.

ID
^^

The ``ID`` selector is used similar to class where it can be applied to an HTML tag using the ``id`` attribute.
However, the similarities stop there, as there are some key differences.

1. The attribute is specified in a css file using the number or hash sign (**#**).
2. An ID is expected to only be placed on a **SINGLE** html element. This is different from classes which can be placed across multiple elements.
3. ID takes a precedence over class, meaning if you define a property in both an ID and Class specification, the ID will be used.

.. code-block:: html
    :linenos:
    :caption: index.html

    <header>
            <h1 id="main_title" class="title gr">Planet Express!</h1>
            <img src="./images/planet_express.png" alt="">
    </header>

.. code-block:: css
    :linenos:
    :caption: style.css

    
    #main_title {
        color: rgb(121, 0, 0);
    }


.. warning::

   Most code editors usually do not detect if an ID is only placed on a single element. 
   This is more of a design pattern that is expected to be followed. 
   With that in mind please be mindful of not accidentally using ID's in multiple places.


Class and id selectors can be combined with element selectors to give even more specificity.

.. code-block:: css
    :linenos:
    :caption: style.css

    h1#main_title {
        font-style: italic;
    }
    
    h2.title {
        color: rgb(121, 0, 0);
    }

Attribute Selectors
^^^^^^^^^^^^^^^^^^^

These selectors are used with element selectors to specify an element based on an attribute that it has. 
This can be used to apply for elements that just have an attribute, or the attribute is set to a specific example.

.. code-block:: css
    :linenos:
    
    /* change all links with href attribute to black */
    a[href] {
        color: black;
    }


Pseudo-class Selector
^^^^^^^^^^^^^^^^^^^^^

These **pseudo-class** selectors are named so because they are styles given to signify a state of an element. 
You can think of different styles that change as you explore a website such hovering over an element, the first line of an element, and more.

.. code-block:: css
    :linenos:
    
    /* link color when hovered over */
    a:hover {
        color: black;
    }

For a full list of all selectors, click here: `CSS Selectors <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors>`_.

CSS Units
~~~~~~~~~~

You might have noticed that for some styling to size things we used a unit such as ``px``. There are many CSS units that are 
we are unable to cover in this course. If you are interested you can learn more about them here: `CSS Units <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units>`_

In general there are a few that are worth mentioning that you will most commonly see and use.

.. table:: 
    :widths: 30 70

    +----------------+-----------------------------------------------------------+
    | Unit           | Details                                                   |
    +================+===========================================================+
    | ``px``         | Used to represents the size  in terms of "pixels"         |
    +----------------+-----------------------------------------------------------+
    | ``mm``         | milimeters                                                |
    +----------------+-----------------------------------------------------------+
    | ``vh``         | 1% of viewports height. i.e. 1% of iphone screen height   | 
    +----------------+-----------------------------------------------------------+
    | ``vw``         | 1% of viewports width. i.e. 1% of iphone screen width     | 
    +----------------+-----------------------------------------------------------+
    | ``%``          | percentage                                                | 
    +----------------+-----------------------------------------------------------+


Exercise 1
~~~~~~~~~~

Remove all CSS in your current ``style.css`` file.

Apply the follwing styles in your stylesheet file. Be sure to set your attributes as needed in your ``index.html`` file.

- Give each header element (h1 - h6) a different `color <https://www.w3schools.com/cssref/pr_text_color.php>`_ using a **class** selector
- Give each header the **same** `font-family <https://developer.mozilla.org/en-US/docs/Web/CSS/font-family>`_ using a **class** selector
- Set the **font-family** for the footer paragraph with the copyright using an **id** selector
- set the color of all links in the ``nav`` HTML element using **any** selector
- set the color of all links in the ``aside`` only on **hover** using the `hover <https://www.w3schools.com/cssref/sel_hover.php>`_ psuedo selector

Remember that google and even AI are your friend (just not skynet).

Using CSS
---------

Up to now we have only been adding our styles to a stylesheet that we then load in our html file. 
While this is a traditional way of adding styles to a webpage, there are two other ways.
Let's see and compare all three.


External Stylesheet
~~~~~~~~~~~~~~~~~~~

This is the way we have been using, where we reference a stylesheet and load it.

.. code-block:: html
    :linenos:
    :emphasize-lines: 7

    <!doctype html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width" />
            <title>Planet Express</title>
            <link href="styles/style.css" rel="stylesheet" />
        </head>
        ...
        </body>
    </html>

This has some useful advantages. We only need to referenced those stylesheets applied on a webpage, and if we wanted to we could
re-use a stylesheet on multiple webpages.

However, this still has some disadvantages. If we are using a css style that is fairly general, (i.e. change all ``p`` tags) we run
the risk of altering other styles in different pages that use the same stylesheet. 

Later on we will explore how to setup some frameworks to minimize this issue.

Internal Stylesheet
~~~~~~~~~~~~~~~~~~~

An **Internal Stylesheet** resides inside the HTML document. A special element, ``<style>`` is used within the ``<head>`` tag
that is used to store the CSS rulesets for that page.

.. code-block:: html
    :linenos:
    :emphasize-lines: 7-19

    <!doctype html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width" />
            <title>Planet Express</title>
            <style>
                .main_title {
                    color: brown;
                }

                .second_title {
                    color: chartreuse;
                }

                .lower_title {
                    color:deeppink;
                }
            </style>
        </head>
        <body>
        ...
        </body>
    </html>

Internal stylesheets are useful where you may not have acces to the external CSS files and only need to make changes on a single page.

However, for sites with multiple web pages it can start to be cumbersome. If you need the same styles for multiple pages, then they
will have to placed inside each respective HTML file.

Inline styles
~~~~~~~~~~~~~

**Inline** styles affect a single HTML element. The ``style`` attribute is modified using semicolon-separated values.

.. code-block:: html
    :linenos:
    :emphasize-lines: 10

    <!doctype html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width" />
            <title>Planet Express</title>
        </head>
        <body>
            <header>
                <h1 style="font-size: 15px; font-family:'Courier New';">Planet Express!</h1>
                <img src="./images/planet_express.png" alt="">
            </header>
        ...
        </body>
    </html>

.. warning::

    This type of CSS should used as a last resort. This can quickly make HTML hard to read. It also does not allow a separation
    between code and content. This can also require multiple edits within a single page which can start to increase from a single change.
    I won't say not to use it cause even I still see it used, but definitely try and limit it as much as possible if all other attempts fail.

Combinators
-----------

While considered a selector, combinators are used to select elements based on their relationship to other elements. 
Here we detail some of the most useful combinators.

A full list of combinators can be found here: `CSS Combinators <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors>`_.

Descendant Combinator
~~~~~~~~~~~~~~~~~~~~~

| The **descendant combinator** is used to select elements that are descendants of a specified element.  
| This is done by placing a space between the two selectors.  
| Selectors that utilize this combinator are called **descendant selectors**.

.. code-block:: css
    :linenos:

    main p {
        color: red;
    }

This will select all ``p`` elements that are descendants of a ``main`` element.

You can also use this to select elements that are descendants of a class or id.

.. code-block:: css
    :linenos:

    .main p {
        color: red;
    }

This will select all ``p`` elements that are descendants of an element with the class ``title``.

Child Combinator
~~~~~~~~~~~~~~~~

| The **child combinator** is used to select elements that are direct children of a specified element.
| This is done by placing a greater than sign (``>``) between the two selectors.

.. code-block:: css
    :linenos:

    ul > li {
        color: red;
    }

This will select all ``li`` elements that are direct children of a ``ul`` element.

Next-Sibling Combinator
~~~~~~~~~~~~~~~~~~~~~~~

| The **next-sibling combinator** is used to select elements that are the next sibling of a specified element.
| This is done by placing a tilde (``+``) between the two selectors.
| For example, to select all ``p`` elements that are next siblings of a ``div`` element:

.. code-block:: css
    :linenos:

    div + p {
        color: red;
    }

| This will select all ``p`` elements that are next siblings of a ``div`` element.
| A common usecase is to do something with a paragraph that is directly after a header.

.. code-block:: css
    :linenos:

    h2 + p {
        color: red;
    }

| This will select all ``p`` elements that are next siblings of a ``h2`` element.

Subsequent-Sibling Combinator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The **subsequent-sibling combinator** is used to select elements that are siblings of a specified element.
| This is done by placing a tilde (``~``) between the two selectors.
| This will select all siblings even if they are not directly adjacent to the element.
| For example, to select all ``img`` that come *anywhere* after a ``h1`` element:

.. code-block:: css
    :linenos:

    h1 ~ img {
        border: 1px solid red;
    }

| This will select all ``img`` elements that are siblings of a ``h1`` element.

Complex Selectors
~~~~~~~~~~~~~~~~~

You can use nesting to create rules that use combinaors to create more complex rules.

.. code-block:: css
    :linenos:

    p {
    ~ img {
      }
    }
    /* This is parsed by the browser as */
    p ~ img {
    }

The ``&`` can also be used to create complex selectors.

.. code-block:: css
    :linenos:

    p {
    & img {
      }
    }
    /* This is parsed by the browser as */
    p img {
    }

Combining Selectors
~~~~~~~~~~~~~~~~~~~

You can also combine selectors to create more complex rules.
For example, say you want to select al ``li`` elements with the class ``point`` that are descendants of a ``ul`` element.

.. code-block:: css
    :linenos:

    ul > li[class="point"] {
        color: red;
    }

.. note::

   Be mindful when creating a big list of selectors to select very specific parts. 
   This can make it hard to reuse styles and can make it hard to maintain.
   It is often better to create a simple class or id to apply to the elements you want to style.

Exercise 2
~~~~~~~~~~

Make the following changes to your ``style.css`` file using combinators.

- Select all ``li`` elements that are descendants of a ``ul`` element and ``nav`` element and change their color.
- Select all ``li`` elements that are descendants of a ``ul`` element and ``main`` element and change their color.
- Select all ``p`` elements that are siblings of headers and change their font size.
- Select all ``img`` elements that are siblings of headers and change their border to 7px solid black.

Feel free to add classes and ids to your HTML elements to make it easier to select them with certain combinators. 

Additional Resources
--------------------
* Some of this materials is based on Mozilla `Learn Web Development <https://developer.mozilla.org/en-US/docs/Learn>`_
* `W3 Schools CSS <https://www.w3schools.com/css/css_intro.asp>`_
* `W3 Schools CSS Units <https://www.w3schools.com/cssref/css_units.php>`_
* `CSS Flexbox Layout Guide <https://css-tricks.com/snippets/css/a-guide-to-flexbox/>`_
* `CSS Guidelines Blog <https://cssguidelin.es/>`_