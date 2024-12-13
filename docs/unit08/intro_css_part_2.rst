.. role:: red

Introduction to CSS: Part 2
===========================

In this section, we will explore more CSS concepts related to the layout of a page. 
We will look at how specificity and inheritance work in CSS, and how to use them to style your page.
We will look at the box model, and how it can be used to layout your page. 
We will also look at Flexbox, a layout model that is part of CSS3, and how it can be used to create flexible layouts. 
Finally, we will look at responsive design, and how to create a page that looks good on all devices.
After this module, students should be able to:

:red:`what students will learn`


Setup and Installation
----------------------

You should still have your old directory from the previous module that covered HTML with the associated **index.html** file.
Navigate to your directory. You can use the ``index.html`` you created last time for Exercise 2 of the HTML, or
copy an update version that is done `here <https://raw.githubusercontent.com/andrewsolis/cs401/refs/heads/main/docs/unit08/resources/index_css.html>`_.
 

Run the following command to setup your small webserver, and navigate to http://localhost:8000/ to verify it is up and running.

.. code-block:: console

    [terminal]$ cd newsite
    [terminal]$ python -m http.server


Specificity and Inheritance
---------------------------

At a certain time when you are styling a page, you will notice that some styles are not being applied as you expect.
This is because of the way CSS handles specificity and inheritance.

Specificity is the way CSS determines which style to apply to an element when there are multiple styles that could apply.
The more specific a style is, the more likely it is to be applied.
The specificity of a style is determined by the number of selectors in the style, and the type of selectors used.
For example, a style with an ID selector is more specific than a style with a class selector, which is more specific than a style with an element selector.
If two styles have the same specificity, the one that comes later in the CSS file will be applied.

.. code-block:: css
    :linenos:

    h1 {
        color: red;
    }

    h1 {
        color: blue;
    }

Say we have two separate selectors: one using an element selector and the other using a class selector.

.. code-block:: css
    :linenos:

    h1 {
        color: red;
    }

    .heading {
        color: blue;
    }

The style with the class selector will be applied, because it is more specific than the style with the element selector.
This is the case even if the ``h1`` selectora appears further down in the CSS file.

Inheritance is the way CSS determines which styles are applied to an element based on the styles of its parent elements.
Some CSS property values are inherited from a parent by it's childresn, and some aren't.
For example, the ``color`` property is inherited, so if you set the color of a parent element, the color of its children will be the same.

.. code-block:: css
    :linenos:

    body {
        color: red;
    }

    p {
        color: black;
    }

There are some properties that are not which include width, margin, padding, and border. 

CSS provides five special property values that can be used to control inheritance:

* ``inherit``: The property value is inherited from the parent element.
* ``initial``: The property value is set to the default value for the property.
* ``revert``: The property value is set to the default value for the property, unless the property is naturally inherited, in which case it acts like ``inherit``.
* ``revert-layer``: Resets the property value applied to a selected element to the value extablished in a previous cascade layer.
* ``unset``  : Resets the property to its natural value, which means that if the property is naturally inherited it acts like ``inherit`` and if it is not naturally inherited it acts like ``initial``.

You can learn more about these properties here: https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance.

The Box model
-------------

Flexbox
-------

Responsive Design
-----------------

Additional Resources
--------------------
* Some of this materials is based on Mozilla `Learn Web Development <https://developer.mozilla.org/en-US/docs/Learn>`_
* `Specificity <https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity>`_
* `W3 Schools CSS Units <https://www.w3schools.com/cssref/css_units.php>`_
* `CSS Flexbox Layout Guide <https://css-tricks.com/snippets/css/a-guide-to-flexbox/>`_
* `CSS Guidelines Blog <https://cssguidelin.es/>`_