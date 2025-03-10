Advanced Containers
===================

In the first part, we pulled and ran existing container images from Docker Hub.
In this section, we will build an image from scratch for running some of our own
Python3 code. Then, we will push that image back up to Docker Hub so others may
find and use it. After going through this module, students should be able to:

* Install and test code in a container interactively
* Write a Dockerfile from scratch
* Build a Docker image from a Dockerfile
* Push a Docker image to Docker Hub
* Volume mount external data inside a Docker container


Getting Set Up
--------------

*Scenario:* You are a developer who has written code in python. 
You now want to distribute that code for others 
to use in what you know to be a stable production environment
(including OS and dependency versions). End users may want to use this application
on their local workstations, in the cloud, etc. 


The first step in a typical container development workflow entails installing
and testing an application interactively within a running Docker container.


To begin, make a new folder for this work and prepare to gather some important
files.


.. code-block:: console

   [terminal]$ mkdir -p cs401/docker-exercise/
   [terminal]$ cd cs401/docker-exercise/
   [terminal]$ pwd
   /home/asolis/cs401/docker-exercise

Specifically, you need a copy of ``collatz.py`` script and the input data
file called ``input.txt``. You can find this in the class repository on GitHub. 
You also need a ``Dockerfile``, and we can just make an empty one with no contents for now.

.. math::
   f(n)=\begin{cases}
   n/2  & \text{if $n \equiv$ 0 (mod 2)},\\
   3n+1 & \text{if $n \equiv$ 1 (mod 2)}.
   \end{cases}

.. code-block:: console

   [terminal]$ ls
   Dockerfile collatz.py input.txt

.. warning::

   It is important to carefully consider what files and folders are in the same
   ``PATH`` as a Dockerfile (known as the 'build context'). The ``docker build``
   process will index and send all files and folders in the same directory as
   the Dockerfile to the Docker daemon, so take care not to ``docker build`` at
   a root level.


Containerize Code Interactively
-------------------------------

There are several questions you must ask yourself when preparing to containerize
code for the first time:

1. What is an appropriate base image?
2. What dependencies are required for my program?
3. What is the installation process for my program?
4. What environment variables may be important?

We can work through these questions by performing an **interactive installation**
of our Python script. My development environment is running python 3.12
but yours may be different. Verify the code works and then you can proceed with 
how we will containerize it. Use ``docker run`` to interactively attach to a fresh
`Ubuntu 20.04 container <https://hub.docker.com/_/ubuntu/tags?page=1&name=20.04>`_.

.. code-block:: console

   [terminal]$ docker run --rm -it -v $PWD:/code ubuntu:20.04 /bin/bash
   [root@7ad568453e0b /]#


.. note::
   
   For Windows users, **${PWD}** should be the only thing that needs to be modified, everything else should still work.


Here is an explanation of the options:

.. code-block:: text

   docker run       # run a container
   --rm             # remove the container on exit
   -it              # interactively attach terminal to inside of container
   -v $PWD:/code    # mount the current directory to /code
   ubuntu:20.04     # image and tag from Docker Hub
   /bin/bash        # shell to start inside container


The command prompt will change, signaling you are now 'inside' the container.
And, new to this example, we are using the ``-v`` flag which mounts the contents
of our current directory (``$PWD``) inside the container in a folder in the root
directory called (``/code``).


Update and Upgrade
~~~~~~~~~~~~~~~~~~

The first thing we will typically do is use the Ubuntu package manager ``apt``
to update the list of available packages and install newer versions of the
packages we have installed. We can do this with:

.. code-block:: console

  [root@7ad568453e0b /]# apt-get update
  [root@7ad568453e0b /]# apt-get upgrade
  [root@7ad568453e0b /]# apt-get install curl git vim software-properties-common
  [root@7ad568453e0b /]# add-apt-repository ppa:deadsnakes/ppa
  ...

.. note::

  You may need to press 'y' followed by 'Enter' to download and install updates


Install Required Packages
~~~~~~~~~~~~~~~~~~~~~~~~~

For our Python scripts to work, we need to install a few dependencies: Python3,
pip, and the 'pytest' package (more on the 'pytest' package later, let's just
assume for now we need it).

.. code-block:: console

   [root@7ad568453e0b /]# apt-get install python3.12
   ...
   [root@7ad568453e0b /]# python3.12 --version
   Python 3.12.7
   [root@7ad568453e0b /]# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   [root@7ad568453e0b /]# python3.12 get-pip.py
     ...

.. warning::

   An important question to ask is: Does the versions of Python and other
   dependencies match the versions you are developing with in your local
   environment? If not, make sure to install the correct version of Python.



Install and Test Your Code
~~~~~~~~~~~~~~~~~~~~~~~~~~

At this time, we should make a small edit to the code that will make it a little
more flexible and more amenable to running in a container. (Note: You may need to
``apt-get install ...`` your favorite text editor). Instead of hard coding
the filename 'input.txt' in the script, let's make a slight
modification so we can pass the filename on the command line. In the script, add
this line near the top:

.. tip::

   If you've already done this with something like ``argparse``, that works too.

   

.. code-block:: python3

   import sys

And change the ``with open...`` statements to these, as appropriate:

.. code-block:: python3

   with open(sys.argv[1], 'r') as file:
      ...



Since we are using a simple Python script, there is not a difficult install
process. However, we can make it executable and add it to the user's `PATH`.

.. code-block:: console

   [root@7ad568453e0b /]# cd /code
   [root@7ad568453e0b /]# chmod +rx collatz.py
   [root@7ad568453e0b /]# export PATH=/code:$PATH

Now test with the following:

.. code-block:: console

   [root@7ad568453e0b /]# cd /home
   [root@7ad568453e0b /]# cp /code/input.txt .
   [root@7ad568453e0b /]# collatz.py input.txt
   Collatz
   =======

   12
   ...

We now have functional versions of our script 'installed' in this container.
Now would be a good time to execute the `history` command to see a record of the
build process. When you are ready, type `exit` to exit the container and we can
start writing these build steps into a Dockerfile.

.. warning::

   If you are using a Windows machine you will need to make sure that the end of line sequennce
   is set to LF. If you are using visual studio code, you can do this by clicking on the CRLF 
   button in the bottom right corner of the screen and selecting LF. 
   This will ensure that the Dockerfile is properly formatted.

Assemble a Dockerfile
---------------------

After going through the build process interactively, we can translate our build
steps into a Dockerfile using the directives described below. Open up your copy
of ``Dockerfile`` with a text editor and enter the following:


The FROM Instruction
~~~~~~~~~~~~~~~~~~~~

We can use the FROM instruction to start our new image from a known base image.
This should be the first line of our Dockerfile. In our scenario, we want to
match our development environment with Ubuntu 20.04. We know our code works in
that environment, so that is how we will containerize it for others to use:

.. code-block:: dockerfile

   FROM ubuntu:20.04 

Base images typically take the form `os:version`. Avoid using the '`latest`'
version; it is hard to track where it came from and the identity of '`latest`'
can change.

.. tip::

   Browse `Docker Hub <https://hub.docker.com/>`_ to discover other potentially
   useful base images. Keep an eye out for the 'Official Image' badge.


The RUN Instruction
~~~~~~~~~~~~~~~~~~~

We can install updates, install new software, or download code to our image by
running commands with the RUN instruction. In our case, our dependencies
were curl, git, vim, software-properties-common, and Python3. 
So, we will use a few RUN instructions to install them. 
Keep in mind that the the ``docker build`` process cannot handle
interactive prompts, so we use the ``-y`` flag with ``yum`` and ``pip3``.

.. code-block:: dockerfile

   RUN apt-get update
   RUN apt-get upgrade -y
   RUN apt-get install -y curl git vim 
   
   RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common
   RUN add-apt-repository -y ppa:deadsnakes/ppa
   RUN apt-get install -y python3.12
   RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   RUN python3.12 get-pip.py

Each RUN instruction creates an intermediate image (called a 'layer'). Too many
layers makes the Docker image less performant, and makes building less
efficient. We can minimize the number of layers by combining RUN instructions.
Dependencies that are more likely to change over time (e.g. Python3 libraries)
still might be better off in in their own RUN instruction in order to save time
building later on:


.. code-block:: dockerfile

   RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y curl git vim 
    
   RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common 

   RUN add-apt-repository -y ppa:deadsnakes/ppa

   RUN apt-get install -y python3.12

   RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
       python3.12 get-pip.py

.. tip::

   In the above code block, the \ character at the end of the lines causes the
   newline character to be ignored. This can make very long run-on lines with
   many commands separated by && easier to read.




The COPY Instruction
~~~~~~~~~~~~~~~~~~~~

There are a couple different ways to get your source code inside the image. One
way is to use a RUN instruction with ``wget`` to pull your code from the web.
When you are developing, however, it is usually more practical to copy code in
from the Docker build context using the COPY instruction. For example, we can
copy our script to the root-level ``/code`` directory with the following
instructions:

.. code-block:: dockerfile

   COPY collatz.py /code/collatz.py


And, don't forget to perform another RUN instruction to make the script
executable:

.. code-block:: dockerfile

   RUN chmod +rx /code/collatz.py




The ENV Instruction
~~~~~~~~~~~~~~~~~~~

Another useful instruction is the ENV instruction. This allows the image
developer to set environment variables inside the container runtime. In our
interactive build, we added the ``/code`` folder to the ``PATH``. We can do this
with ENV instructions as follows:

.. code-block:: dockerfile

   ENV PATH="/code:$PATH"



Putting It All Together
~~~~~~~~~~~~~~~~~~~~~~~

The contents of the final Dockerfile should look like:

.. code-block:: dockerfile
   :linenos:

   FROM ubuntu:20.04

   RUN apt-get update && \
      apt-get upgrade -y && \
      apt-get install -y curl git vim 
      
   RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common 

   RUN add-apt-repository -y ppa:deadsnakes/ppa

   RUN apt-get install -y python3.12

   RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
      python3.12 get-pip.py

   COPY collatz.py /code/collatz.py

   RUN chmod +rx /code/collatz.py

   ENV PATH="/code:$PATH"


Build the Image
---------------

Once the Dockerfile is written and we are satisfied that we have minimized the
number of layers, the next step is to build an image. Building a Docker image
generally takes the form:

.. code-block:: console

   [terminal]$ docker build -t <dockerhubusername>/<code>:<version> .

The ``-t`` flag is used to name or 'tag' the image with a descriptive name and
version. Optionally, you can preface the tag with your **Docker Hub username**.
Adding that namespace allows you to push your image to a public registry and
share it with others. The trailing dot '``.``' in the line above simply
indicates the location of the Dockerfile (a single '``.``' means 'the current
directory').

To build the image, use:

.. code-block:: console

   [terminal]$ docker build -t username/collatz:1.0 .

.. note::

   Don't forget to replace 'username' with your Docker Hub username.


Use ``docker images`` to ensure you see a copy of your image has been built. You can
also use `docker inspect` to find out more information about the image.

.. code-block:: console

   [terminal]$ docker images
   REPOSITORY                 TAG        IMAGE ID       CREATED              SIZE
   username/collatz  1.0        2883079fad18   About a minute ago   446MB
   ...

.. code-block:: console

   [terminal]$ docker inspect username/collatz:1.0


If you need to rename your image, you can either re-tag it with ``docker tag``, or
you can remove it with ``docker rmi`` and build it again. Issue each of the
commands on an empty command line to find out usage information.



Test the Image
--------------

We can test a newly-built image two ways: interactively and non-interactively.
In interactive testing, we will use ``docker run`` to start a shell inside the
image, just like we did when we were building it interactively. The difference
this time is that we are NOT mounting the code inside with the ``-v`` flag,
because the code is already in the container:

.. code-block:: console

   [terminal]$ docker run --rm -it username/collatz:1.0 /bin/bash
   ...
   [root@c5cf05edddcd /]# ls /code
   collatz.py
   [root@c5cf05edddcd /]# cd /home
   [root@c5cf05edddcd home]# pwd
   /home
   [root@c5cf05edddcd home]# collatz.py input.txt
   Traceback (most recent call last):
     File "/code/collatz.py", line 96, in <module>
       main()
     File "/code/collatz.py", line 82, in main
       with open(sys.argv[1], 'r') as f:
   FileNotFoundError: [Errno 2] No such file or directory: 'input.txt'

Here is an explanation of the options:

.. code-block:: text

   docker run      # run a container
   --rm            # remove the container when we exit
   -it             # interactively attach terminal to inside of container
   username/...    # image and tag on local machine
   /bin/bash       # shell to start inside container


Uh oh! We forgot about ``input.txt``! We get a FileNotFoundError
in Python3. This is because we did not (1) copy the file into the container
at build time, nor did we (2) copy the file into the container at run
time.

We should pause at this moment to think about how we want to distribute this
application. Should the data be encapsulated within? Or should we expect potential
users to be bring their own data for analysis?

Let's try again, but this time mount the data inside the container so we can
access it. If we mount the current folder as, e.g., ``/data``, then everything
in the current folder will be available. In addition, if we write any new files
inside the container to ``/data``, those will be preserved and persist outside
the container once it stops.

.. code-block:: console

   [terminal]$ docker run --rm -it -v $PWD/input.txt:/data/input.txt username/collatz:1.0 /bin/bash
   ...
   ### Same command as above, but easier to read:
   [terminal]$ docker run --rm \
                         -it \
                         -v $PWD/input.txt:/data/input.txt \
                         username/collatz:1.0 \
                         /bin/bash
   
   [root@dc0d6bf1875c /]# pwd
   /
   [root@dc0d6bf1875c /]# ls /data
   input.txt
   [root@dc0d6bf1875c /]# ls /code
   collatz.py
   [root@dc0d6bf1875c /]# collatz.py /data/input.txt
   Collatz
   =======

   12
   ...



Everything looks like it works now! Next, exit the container and test the code
non-interactively. Notice we are calling the container again with ``docker run``,
but instead of specifying an interactive (``-it``) run, we just issue the command
as we want to call it on the command line. Also, notice the return of the ``-v``
flag, because we need to create a volume mount so that our data
(``input.txt``) is available inside the container.

.. code-block:: console

   [terminal]$ docker run --rm \
                         -v $PWD/input.txt:/data/input.txt \
                         username/collatz:1.0 \
                         collatz.py /data/input.txt
   Collatz
   =======

   12
   ...

Much simpler and cleaner! Our only local dependencies are the Docker runtime and
some input data that we provide. Then we pull and run the image, mounting our
data inside the container and executing the embedded Python3 script. Anyone with
their own data could follow our same steps to replicate our work in their own
environments.



Share Your Docker Image
-----------------------

Now that you have containerized, tested, and tagged your code in a Docker image,
the next step is to disseminate it so others can use it.

Docker Hub is the *de facto* place to share an image you built. Remember, the
image must be name-spaced with either your Docker Hub username or a Docker Hub
organization where you have write privileges in order to push it:

.. code-block:: console

   [terminal]$ docker login
   ...
   [terminal]$ docker push username/collatz:1.0


You and others will now be able to pull a copy of your container with:

.. code-block:: console

   [terminal]$ docker pull username/collatz:1.0


As a matter of best practice, it is highly recommended that you store your
Dockerfiles somewhere safe. A great place to do this is alongside the code
in, e.g., GitHub. GitHub also has integrations to automatically update your
image in the public container registry every time you commit new code.

For example, see: `Publishing Docker Images <https://docs.github.com/en/actions/publishing-packages/publishing-docker-images/>`_




Additional Resources
--------------------

* `Docker for Beginners <https://training.play-with-docker.com/beginner-linux/>`_
* `Play with Docker <https://labs.play-with-docker.com/>`_
