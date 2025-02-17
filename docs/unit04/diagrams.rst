Diagrams for Software Design
=============================

In this module, we provide a brief introduction to diagrams for software design. By the end 
of this module, the student should be able to:

  * Explain the basic utility of diagrams for software design
  * Describe the differences between structural diagrams and behavioral diagrams. 
  * Create different types of structural and/or behavioral diagrams for their flask-based API system.

As a software system grows in its size and complexity, it becomes increasingly difficult to describe in 
written text. Diagrams help us visualize the components of a software system, allowing us to provide a
more concise and holistic description. There are many tools and approaches to creating diagrams for software 
systems. In this short module, we provide only a brief introduction to diagrams for software design, and
we include some references for further reading. 

Generally speaking, a diagram can convey two types of information:

  * Static relationships between components, sometimes called a structural diagram.
  * Dynamic information describing how the system changes or how different components react to 
    each other. These are called behavior diagrams.


Structural Diagrams
-------------------

With a structural diagram, the goal is to represent the components of the system with different shapes, 
and to indicate connections between the components, usually with an arrow. Different diagrams will
represent different types of components in the system at different granularity.
For example, we could use boxes to represent:

  * Classes in software utilizing object oriented programming
  * Modules and libraries in a large code base 
  * Containers or services in a distributed system utilizing a microservice architecture

.. figure:: ./images/class-diagram.png
    :width: 1000px
    :align: center
    :alt: An example of a class diagram
    
    An example of a class diagram

Similarly, arrows between components represent different types of connections. 

  * For classes in OOP, arrows represent different types of relationships between the classes, such as 
    inheritance (when one class is a child of another class) or dependency (when one class uses 
    methods from another class).
  * For a diagram containing microservices, arrows represent the communication between services. 


Behavioral Diagrams
-------------------

By contrast to structural diagrams, behavioral diagrams capture the how components within the system 
respond to changes. Some common behavioral diagrams include:

Flowcharts 
~~~~~~~~~~
Flowcharts depict the step-by-step process of an algorithm or component of a program. Each box
represents a different step in the process. Different shapes are used for different types of steps, 
such as a rhombus for collecting input, a diamond for an IF/THEN conditional, and a rectangle for a 
computation. 

.. figure:: ./images/Flowchart-of-the-Algorithm-for-Shortest-Path.png
    :width: 500px
    :align: center
    :alt: A flowchart of the all-pairs-shortest-path (APSP) algorithm. 
    
    A flowchart of the all-pairs-shortest-path (APSP) algorithm. 

Sequence Diagrams
~~~~~~~~~~~~~~~~~
Sequence diagrams describe the sequence of interactions (usually, communications) between components of
a system and even end users. The components represented in a sequence diagram could be web pages or URLs 
within a single web application, or they could be entirely different services in a microservice architecture.

.. figure:: ./images/oauth-sequence-diag.png
    :width: 500px
    :align: center
    :alt: A sequence diagram of the OAuth2 authorization code flow.
    
    A sequence diagram of the OAuth2 authorization code flow.


Unified Modeling Language (UML)
-------------------------------

The Unified Modeling Language (UML) is a modeling language for describing diagrams. It was created in 
1994 and became an ISO standard in 2005. There are two major versions of UML, v1 and v2. In v2, 
there are at least 14 different types of diagrams. 

Some UML diagrams, such as the class diagram, are precise enough to be able to generate code from them.
While this is a neat idea, in practice some software engineers find UML heavyweight and cumbersome.
If you are interested in UML, there are a number of tutorials on the web.

Here is an example description of a class digram created in `PlantUML <https://plantuml.com/>`_ diagram describing a hypothetical CS 401 final project:

.. code-block:: console

  @startuml
  class "Video Game"{
    + name: string
    + release date: string
    + genre : string []
    + platform : string []
    + game engine : string
  }

  class People {
    + name : string
    + dob  : string
    + current role : string
    + previous roles : string []
  }

  class Company {
    + name : string
    + founded: string
  }

  "Video Game" "0..*" -- "1..*" People
  "Video Game" "0..*" -- "0..*" Company
  People "1..*" -- "0..1" Company

  @enduml

This generates the following diagram:

.. figure:: ./images/plantuml.png
    :width: 300px
    :align: center
    :alt: A class diagram for video game database website
    
    A class diagram for video game database website


Options for Creating Diagrams
-----------------------------

There are a lot of options for creating diagrams:

  1. Google Slides/Google Draw - Both options allow you to create basic shapes and connectors, fill,
     arranges, etc. Free with a google account. 
  2. draw.io - Similar to google slides but some find it to be more ergonomic to use. Free.
  3. Microsoft Powerpoint - Similar to the other options above; requires access to Microsoft Office. 
  4. `PlantUML <https://plantuml.com/>`_ - create class and multiple different diagrams. Free.
  5. `dbdigram.io <https://dbdiagram.io/>`_ - create entity-relationship diagrams based on database.
  
And if you want to make diagrams from UML...
  4. Visual Paradigm - This is kind of like the others above where you click and drag boxes and arrows 
     (I think). I got the "Community Edition" installed on Ubuntu without much trouble. It is free. 
  5. kroki.io - This project is kind of fun. It provides an HTTP API for making diagrams (what could be better?) 
     You describe your diagrams in text (for example, in UML) and make an HTTP request to the diagram endpoint and it returns to 
     you HTML that renders your figure. You can use their community server, or you can run the whole API 
     as a docker container on your machine. It's all free. 
    
.. figure:: ./images/kroki-plant-uml-screenshot.png
    :width: 800px
    :align: center
    :alt: A screenshot of the kroki.io docs.
    
    From the kroki.io documentation.

Additional Resources
--------------------
* `UML Diagram Tutorial <https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/>`_