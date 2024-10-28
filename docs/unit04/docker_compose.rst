Docker Compose
==============

Up to this point, we have been looking at single-container applications - small
units of code that are containerized, executed *ad hoc* to generate or read a file, 
then exit on completion. But what if we want to do something more
complex? For example, what if our goal is to orchestrate a multi-container
application consisting of, e.g., a Flask app, a database, a front-end service, 
and more.

**Docker compose** is a tool for managing multi-container applications. A YAML
file is used to define all of the application service, and a few simple commands
can be used to spin up or tear down all of the services.

In this module, we will get a first look at Docker compose. After going
through this module, students should be able to:

* Translate Docker run commands into YAML files for Docker compose
* Run commands inside *ad hoc* containers using Docker compose
* Manage small software systems composed of more than one script, and more than
  one container
* Copy data into and out of containers as needed


Another Script, Another Container
---------------------------------

We have been working a lot with a script for reading in and analyzing a
simple text file. Let's quickly write a new script to
generate that data, then we will package it into its own container. Consider the
following script for **generating** sample number like we have
been working with:

.. code-block:: python3
   :linenos:

   import random
   import sys
   import names

   '''
   Collatz Generator Code for CS 401

   Author: Andrew Solis
   '''

   NUM = 20

   def main():


      for i in range(NUM):

         rand_num = random.randint(1, 1000)

         with open(sys.argv[1], 'a') as file:
               file.write( str(rand_num ) + '\n')
         

      print(f'Data written to {sys.argv[1]}')

      print(f'Codename { names.get_first_name() }')

   if __name__ == '__main__':
      main()


Copy that into a file called ``gen_collatz.py``, save it, make it executable, and
test it. You'll find that this script requires a **command line argument**. Meaning
we have to invoke it AND pass some information on the command line in order to get
it to work. In this case, it is expecting the name of the output file.

.. code-block:: console

   # copy contents into file called ``gen_collatz.py`` and save
   [user-vm]$ chmod +rx gen_collatz.py
   [user-vm]$ python3.12 gen_collatz.py
   Traceback (most recent call last):
     File "./gen_collatz.py", line 29, in <module>
       main()
     File "./gen_collatz.py", line 25, in main
       with open(sys.argv[1], 'w') as o:
   IndexError: list index out of range

   # need to provide output filename on command line
   [user-vm]$ python3.12 gen_collatz.py data.txt
   Data written to data.txt.
   Codename Sharon
   [user-vm]$ ls
   data.txt  Dockerfile  gen_collatz.py  input.txt  collatz.py
   [user-vm]$ head -n11 data.txt
   409
   1
   371
   622
   6
   229
   617
   236
   778
   165
   306

Containerizing this script should be easy enough - we already worked through
containerizing another very similar script. But, lets say we need a different dependency: the Python3
``names`` library.

To make things a little more clear, rename the existing Dockerfile as
``Dockerfile-program``, and make a copy of it called ``Dockerfile-gen``.

.. code-block:: console

   [user-vm]$ mv Dockerfile Dockerfile-program
   [user-vm]$ cp Dockerfile-program Dockerfile-gen
   [user-vm]$ ls
   Dockerfile-gen     Dockerfile-program collatz.py         
   data.txt           gen_collatz.py     input.txt

Edit ``Dockerfile-gen`` as follows:

.. code-block:: Dockerfile
   :linenos:
   :emphasize-lines: 8,10,12

   FROM ubuntu:20.04
   
   RUN apt-get update && \
       apt-get upgrade -y && \
       apt-get install -y python3 && \
       apt-get install -y python3-pip
   
   RUN pip3 install names==0.3.0
   
   COPY gen_ml_data.py /code/gen_ml_data.py
   
   RUN chmod +rx /code/gen_ml_data.py
   
   ENV PATH="/code:$PATH"



Now that we have a Dockerfile named something other than the default name, we
need to modify our command line a little bit to build it:

.. code-block:: console

   [user-vm]$ docker build -t username/gen_ml_data:1.0 -f Dockerfile-gen .

After the image is successfully built, change directories to a new folder just
to be sure you are not running the local scripts or looking at the local data.
Then, test the container as follows:

.. code-block:: console

   [user-vm]$ mkdir test
   [user-vm]$ cd test
   [user-vm]$ ls
   [user-vm]$ docker run --rm username/gen_ml_data:1.0 gen_ml_data.py ml.json
   Data written to ml.json!

If you list your local files, can you find ``ml.json``? No! This is because
whatever data generated inside the container is lost when the container
completes its task. What we need to do is use the ``-v`` flag to mount a directory
somewhere inside the container, write data into that directory, then the data will
be captured after the container exists. For example:

.. code-block:: console

   [user-vm]$ docker run --rm -v $PWD:/data username/gen_ml_data:1.0 gen_ml_data.py /data/ml.json
   Data written to ml.json!

.. note::

   To reiterate, because we mounted our current location as a folder called "/data"
   (``-v $PWD:/data``), and we made sure to write the output file to that location in
   the container (``gen_ml_data.py /data/ml.json``), then we get to keep the file
   after the container exits, and it shows up in our current location (``$PWD``).

Alas, there is one more issue to address. The new file is owned by root, simply
because it is root who created the file inside the container. This is one minor
Docker annoyance that we run in to from time to time. The simplest fix is to use
one more ``docker run`` flag (``-id``)to specify the user and group ID namespace
that should be used inside the container.

.. code-block:: console

   [user-vm]$ ls -l
   total 4
   -rw-r--r--. 1 root root 2098 Feb 21 22:39 ml.json
   [user-vm]$ rm ml.json
   rm: remove write-protected regular file ml.json’? y
   [user-vm]$ docker run --rm -v $PWD:/data -u $(id -u):$(id -g) username/gen_ml_data:1.0 gen_ml_data.py /data/ml.json
   Data written to /data/ml.json!
   [user-vm]$ ls -l
   total 4
   -rw-r--r--. 1 ubuntu G-815499 2098 Feb 21 22:41 ml.json



EXERCISE
~~~~~~~~

Spend a few minutes testing both containers. Be sure you can generate data with
one container, then read in and analyze the same data with the other. Data needs
to persist outside the containers in order to do this.



Write a Compose File
--------------------

Docker compose works by interpreting rules declared in a YAML file (typically
called ``docker-compose.yml``). The rules we will write will replace the
``docker run`` commands we have been using, and which have been growing quite
complex. For example, the commands we used to run our JSON parsing scripts in a
container looked like the following:

.. code-block:: console

   [user-vm]$ docker run --rm -v $PWD:/data -u $(id -u):$(id -g) username/gen_ml_data:1.0 gen_ml_data.py /data/ml.json
   [user-vm]$ docker run --rm -v $PWD/ml.json:/data/ml.json username/ml_data_analysis:1.0 ml_data_analysis.py /data/ml.json

The above ``docker run`` commands can be loosely translated into a YAML file.
Navigate to the folder that contains your Python scripts and Dockerfiles, then
create a new empty file called ``docker-compose.yml``:

.. code-block:: console

   [user-vm]$ pwd
   /home/ubuntu/coe-332/docker-exercise
   [user-vm]$ touch docker-compose.yml
   [user-vm]$ ls
   docker-compose.yml  Dockerfile-analysis  Dockerfile-gen  gen_ml_data.py  ml_data_analysis.py  test/


Next, open up ``docker-compose.yml`` with your favorite text editor and type /
paste in the following text:

.. code-block:: yaml
   :linenos:
   :emphasize-lines: 9,12,18

   ---
   version: "3"

   services:
       gen-data:
           build:
               context: ./
               dockerfile: ./Dockerfile-gen
           image: username/gen_ml_data:1.0
           volumes:
               - ./test:/data
           user: "1000:1000"
           command: gen_ml_data.py /data/ml.json
       analyze-data:
           build:
               context: ./
               dockerfile: ./Dockerfile-analysis
           depends_on:
               - gen-data
           image: username/ml_data_analysis:1.0
           volumes:
               - ./test:/data
           command: ml_data_analysis.py /data/ml.json
   ...

.. warning::

   The highlighted lines above may need to be edited with your username / userid /
   groupid in order for this to work. See instructions below.


The ``version`` key must be included and simply denotes that we are using
version 3 of Docker compose.

The ``services`` section defines the configuration of individual container
instances that we want to orchestrate. In our case, we define two called
``gen-data`` for the gen_ml_data functionality, and ``analyze-data`` for
the ml_data_analysis functionality.

Each of those services is configured with its own Docker image,
a mounted volume (equivalent to the ``-v`` option for ``docker run``), a user
namespace (equivalent to the ``-u`` option for ``docker run``), and a default
command to run.

Please note that the image name above should be changed to use your image. Also,
the user ID / group ID are specific to ``ubuntu`` - to find your user and group
ID, execute the Linux commands ``id -u`` and ``id -g``.

.. note::

   The top-level ``services`` keyword shown above is just one important part of
   Docker compose. Later in this course we will look at named volumes and
   networks which can be configured and created with Docker compose.


Running Docker Compose
----------------------

The Docker compose command line tool follows the same syntax as other Docker
commands:

.. code-block:: console

   docker-compose <verb> <parameters>

Just like Docker, you can pass the ``--help`` flag to ``docker-compose`` or to
any of the verbs to get additional usage information. To get started on the
command line tools, try issuing the following two commands:

.. code-block:: console

   [user-vm]$ docker-compose version
   [user-vm]$ docker-compose config

The first command prints the version of Docker compose installed, and the second
searches your current directory for ``docker-compose.yml`` and checks that it
contains only valid syntax.

To run one of these services, use the ``docker-compose run`` verb, and pass the
name of the service as defined in your YAML file:

.. code-block:: console

   [user-vm]$ ls test/     # currently empty
   [user-vm]$ docker-compose run gen-data
   Data written to /data/ml.json!
   [user-vm]$ ls test/
   ml.json               # new file!
   [user-vm]$ docker-compose run analyze-data
   6004.5
   Southern & Eastern
   ... etc.


Now we have an easy way to run our *ad hoc* services consistently and
reproducibly. Not only does ``docker-compose.yml`` make it easier to run our
services, it also represents a record of how we intend to interact with this
container.



Essential Docker Compose Command Summary
----------------------------------------

+------------------------+------------------------------------------------+
| Command                | Usage                                          |
+========================+================================================+
| docker-compose version | Print version information                      |
+------------------------+------------------------------------------------+
| docker-compose config  | Validate docker-compose.yml syntax             |
+------------------------+------------------------------------------------+
| docker-compose up      | Spin up all services                           |
+------------------------+------------------------------------------------+
| docker-compose down    | Tear down all services                         |
+------------------------+------------------------------------------------+
| docker-compose build   | Build the images listed in the YAML file       |
+------------------------+------------------------------------------------+
| docker-compose run     | Run a container as defined in the YAML file    |
+------------------------+------------------------------------------------+


Additional Resources
--------------------

* `Docker Compose Docs <https://docs.docker.com/compose/>`_
