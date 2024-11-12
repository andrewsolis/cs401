Introduction to HTML
=====================

In this section, we will explore HTML and how it is used to create website.
We will better understand the structure of HTML, certain paradigms to follow, 
and explore ways to personalize and create a website. After going through
this module, students should be able to:

* Describe how HTML works for creating websites.
* Help define a layout of a website.
* understand different features of HTML such as bullets, styling, and using images.

Setup and Installation
----------------------

We will setup a local server so we can view the changes we make. A website is nothing more than
a set of files that are read by and sent to a client to render a website. With this in mind, it
is good to consider the structure of our website. In general a folder structure can be like the
one denoted below:

1. ``sitename`` **folder** - A folder containing all the source code for a web application.
2. ``index.html`` - Genreally contains the homepage content, including text and images. Contained within the ``sitename`` folder.
3. ``images`` **folder** - Folder containing any images that will be rendered on the website. Contained within the ``sitename`` folder.
4. ``styles`` **folder** - Folder containing *CSS* code to style our website. Contained within the ``sitename`` folder.
5. ``scripts`` **folder** - Contains *Javascript* code for our website. Contained within the ``sitename`` folder.

Create a folder named ``chaminadesite``. Then within that folder create the three previously mentioned folders. Also copy the ``index.html`` from 
the git repo `here <https://raw.githubusercontent.com/andrewsolis/cs401/refs/heads/main/docs/unit08/resources/indexl.html>`_ and place it into the folder.
Once completed your stucture should look similar to the one shown below:

.. code-block:: console

    [terminal]$ cd chaminadesite
    [terminal]$ ls
    images index.html scripts styles

It's okay to not understand what these folders do just yet. The following explanations will give you a better understanding of what goes into 
each of these folders/files.

What is HTML?
--------------

HTML, or **H**\yper **T**\ext **M**\arkup **L**\anguage, is exactly what is sounds like. It
is a *markup* language that defines the structure of the content, in this case the content for
a website. It consists of a series of **elements** which you use to wrap around different parameters
of the content to make them appear a certain way. Elements are created using **tag**\s that specify
the type of element. We will explore some of the common elements found in HTML.

Say we wanted to insert our sentence below into a tag.

.. code-block:: html
    :linenos:

    Chaminade University is where I go.

If we just had this simple sentence then we could insert it into a **paragraph** tag, which is denoted by
using the **p** tag.

.. code-block:: html
    :linenos:

    <p>Chaminade University is where I go.</p>

There are 4 main parts of our HTML element:

1. **Opening Tag** - The name of the tag we like to use in our case ``<p>``. This is where the content for this particular tag starts. 
2. **Closing tag** - The same as the opening tag except it includes an extra slash to denote it is the closing tag, in our case ``</p>``. This is where the content for this tag ends.
3. **Content** - This is what we place inside of our tag. In our case it is the sentence ``Chaminade University is where I go``, but it can get anything, including other tags.
4. **Element** - This is the combination of everything. This includes our opening and closing tag, and content. Our element would be ``<p>Chaminade University is where I go.</p>``




Additional Resources
--------------------

* SOme of this materials is based on this module my Mozille to `Learn Web Development <https://developer.mozilla.org/en-US/docs/Learn>`_