.. role:: red

Introduction to CSS
=====================

In this section, we will explore CSS and how it helps with designing a website.
this includes problems such as coloring (text/background), making the content display at a certain location,
and "decorating" with images and color schemes. After this module, you should understand:

:red:`list of what they will learn.`

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
