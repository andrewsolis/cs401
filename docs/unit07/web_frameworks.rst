.. role:: red

Introduction to Web frameworks
==============================

We have recently been covering the basics of web development. Having a good foundation of HTML, CSS, and Javascript
is important for any modern software engineer for web applications. However, writing a web application
from scratch is a lot of work. This is where web frameworks come in.
Web frameworks are libraries that provide a set of tools and conventions for building web applications. They
help you to structure your code, handle requests and responses, and manage the database. In this unit, we will
explore some popular web frameworks in general, and how you can use them to build web applications.
After this module, students should have an understanding of:

* What a web framework is
* Why we use web frameworks
* What are some different web frameworks
* What are CSS frameworks
* What are some different CSS frameworks
* What are some different backend frameworks

Web Frameworks
--------------

Web frameworks are tools that provide a structured way to build and manage web applications. They offer reusable components, libraries, and best practices to streamline development and improve code quality. Popular web frameworks include:

- **React**: A JavaScript library for building user interfaces, developed by Facebook. It allows developers to create reusable UI components and manage the state of their applications efficiently.

- **Vue.js**: A progressive JavaScript framework for building user interfaces. Vue.js is designed to be incrementally adoptable, meaning you can use as much or as little of it as you need. It is known for its simplicity and flexibility.

- **Angular**: A platform and framework for building single-page client applications using HTML and TypeScript, developed by Google. Angular provides a comprehensive solution for building dynamic web applications, including tools for routing, forms, and HTTP client communication.

We have looked at creating simple website from vanilla HTML, CSS, and Javascript. However, as we have seen,
this can be a lot of work. This is where web frameworks come in. Web frameworks take a bit to learn at first,
but offer increased productivity and maintainability in the long run. 

In general there is no perfect framework. Each framework has its own strengths and weaknesses, 
and the best choice depends on the specific needs of your project. For example, if you are building 
a large, complex application, you might want to use a framework like Angular or React. If you are 
building a small, simple application, you might want to use a framework like Vue.js. 
Angular is a good choice also for building large complex apps, but it is more opinionated and has a steeper learning curve.

Let's take a look at a simple example of a web application using Vue.js.

Vue.js
~~~~~~

Let's create a simple example To start a `Vue.js <https://vuejs.org/>`_ app, you need to include the Vue.js library in your HTML file and create a Vue instance. Here is a basic example:

.. note::

    Here we are using the Vue.js CDN, script link, to include the library. 
    In a real-world application, you would most likely install Vue.js using a package manager 
    like npm, and use a build tool like Webpack to bundle your code.
    However, for simplicity, we are using the CDN in this example.

    To learn more on how to install Vue.js using npm, check out the official documentation:
    https://vuejs.org/v2/guide/installation.html.

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Vue.js App</title>
        <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #4CAF50;
                color: white;
                padding: 1em;
                text-align: center;
            }
            nav {
                background-color: #333;
                overflow: hidden;
            }
            nav a {
                float: left;
                display: block;
                color: white;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }
            nav a:hover {
                background-color: #ddd;
                color: black;
            }
            .hero {
                background-color: #f4f4f4;
                padding: 2em;
                text-align: center;
            }
            .grid {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                padding: 1em;
            }
            .grid-item {
                background-color: #e0e0e0;
                border: 1px solid #ccc;
                margin: 0.5em;
                padding: 1em;
                width: 200px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div id="app">
            <header>
                <h1>{{ header }}</h1>
            </header>
            <nav>
                <a href="#home">Home</a>
                <a href="#about">About Us</a>
                <a href="#services">Services</a>
            </nav>
            <div class="hero">
                <h2>{{ heroTitle }}</h2>
                <p>{{ heroText }}</p>
            </div>
            <div class="grid">
                <div class="grid-item" v-for="link in links" :key="link.text">
                    <a :href="link.url">{{ link.text }}</a>
                </div>
            </div>
        </div>

        <script>
            var app = new Vue({
                el: '#app',
                data: {
                    header: 'Welcome to My Vue.js App',
                    heroTitle: 'Hello, Vue.js!',
                    heroText: 'This is a simple hero element.',
                    links: [
                        { text: 'Google', url: 'https://www.google.com' },
                        { text: 'Facebook', url: 'https://www.facebook.com' },
                        { text: 'Twitter', url: 'https://www.twitter.com' },
                        { text: 'GitHub', url: 'https://www.github.com' }
                    ]
                }
            });
        </script>
    </body>
    </html>

.. note::

    Flexbox, or the Flexible Box Layout, is a CSS layout module designed to provide 
    a more efficient way to lay out, align, and distribute space among items in 
    a container, even when their size is unknown or dynamic. Flexbox is particularly 
    useful for creating responsive layouts.

    For more detailed information, you can refer to the MDN Web Docs on Flexbox:
    `MDN Flexbox <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox>`_.

Let's break down the code:

- The HTML file includes the Vue.js library using a CDN link.
- The `#app` element is the root element of the Vue instance.
- The `data` property of the Vue instance contains the data that will be displayed in the HTML.
- The `v-for` directive is used to loop through the `links` array and create a grid of links.
- The `:href` directive is used to bind the `url` property of each link to the `href` attribute of the anchor tag.
- the `:key` directive is used to give each link a unique key, which helps Vue.js to efficiently update the DOM when the data changes.

This is just a very simple example of using Vue.js for a homepage for an application.
The true power of web frameworks like these comes when you start building more complex applications with multiple components, routing, and state management.
Interactivity is also a key feature of web frameworks, as they allow you to create dynamic user interfaces that respond to user input and update in real-time.

We looked at Vue.js here because it is known for it's ease of use and simplicity.
It follows a similar structure of using HTML, CSS, and Javascript files, but with the added benefit of Vue.js components and reactivity.
That being said, if you find another framework that you like better, feel free to explore it further.

.. important::

    Web frameworks are complex and fairly detailed.
    A true understanding of these frameworks is beyond the scope of this one lesson.
    I recommend going through the tutorials, and find out which one you like.
    To learn more of each web framework we have discussed, check out the official documentation:

    * `Vue.js <https://vuejs.org/>`_
    * `React <https://reactjs.org/>`_
    * `Angular <https://angular.io/>`_

Exercise 1
~~~~~~~~~~

In this exercise, you will modify the existing Vue.js code to make some changes to the website. Follow the steps below:

1. Change the `header` text to "Welcome to My Modified Vue.js App".
2. Add a new link to the `links` array with the text "LinkedIn" and the URL "https://www.linkedin.com".
3. Change the background color of the `header` to `#FF5733`.

CSS Frameworks
--------------

We have covered CSS in the past and you now have a general understanding of how to style a webpage.
However, writing CSS from scratch can be time-consuming and repetitive. Adding interactivity and responsiveness to your website can be challenging
and quickly lead down a path of large CSS files you have to manage and keep track of. 

This is where CSS frameworks come in.

CSS frameworks provide a set of pre-designed styles and components that you can use to quickly build a website.
They help you to create a consistent and visually appealing design without having to write all the CSS from scratch.
There are also CSS frameworks that allow you to build your own custom design components, such as Tailwind CSS, 
while still using consistent classes to style your elements.

For now let's take a look an example of a popular CSS framework, `Bootstrap <https://getbootstrap.com/>`_.

Bootstrap
~~~~~~~~~

Bootstrap was developed by the team at twitter to provide an easier way to style and build responsive websites.
It has gone through a few different iterations, the most recent being bootstrap 5.
Some core features have remained the same though including: a grid system, typography, forms, buttons, navigation bars, and more. 

Let's take a look at a simple example of a website using Bootstrap using our previous Vue.js example.

We'll use a CDN again, but you could install it using a package manager and include it in your build process.

.. note::

    The term "responsive" can have different meanings. In general it usually means that you are developing
    a website that can adapt to different screen sizes. This is important so that users can have the same
    experience on a desktop, tablet, or mobile device.

.. code-block:: html
    :linenos:
    :emphasize-lines: 6-7

    <!DOCTYPE html>
    <html>
    <head>
        <title>Bootstrap App</title>
        <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
        </style>
    </head>
    <body>
        <div id="app">
            <header class="bg-primary text-white text-center py-3">
                <h1>Welcome to My Bootstrap App</h1>
            </header>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">Navbar</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <a class="nav-link active" aria-current="page" href="#home">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#about">About Us</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#services">Services</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <div class="container my-5">
                <div class="row">
                    <div class="col text-center">
                        <h2>Hello, Bootstrap!</h2>
                        <p>This is a simple hero element.</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-12 col-md-6 col-lg-3 mb-3" v-for="link in links" :key="link.text">
                        <div class="card">
                            <img v-bind:src="link.image_url" alt="">
                            <div class="card-body text-center">
                                <a :href="link.url" class="btn btn-primary">{{ link.text }}</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script>
            var app = new Vue({
                el: '#app',
                data: {
                    links: [
                        { text: 'Google', url: 'https://www.google.com', image_url : 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png' },
                        { text: 'Facebook', url: 'https://www.facebook.com', image_url : 'https://www.facebook.com/images/fb_icon_325x325.png' },
                        { text: 'Twitter', url: 'https://www.twitter.com', image_url : 'https://e7.pngegg.com/pngimages/708/311/png-clipart-icon-logo-twitter-logo-twitter-logo-blue-social-media-thumbnail.png' },
                        { text: 'GitHub', url: 'https://www.github.com', image_url : 'https://imgs.search.brave.com/np-NaC0N3gBsHZTYs6VaesbSU5ZQTfcZ-SAea-uqIb4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hc3Nl/dHMuc3RpY2twbmcu/Y29tL2ltYWdlcy81/ODQ3Zjk4ZmNlZjEw/MTRjMGI1ZTQ4YzAu/cG5n' }
                    ]
                }
            });
        </script>
    </body>
    </html>

This look fairly similar to the Vue.js example, but with some key differences.
Note that in the `head` section, we include the Bootstrap CSS and JavaScript files using CDN links.
We also got rid of the custom styles and used Bootstrap classes to style the elements.
We still set some minor styles.

As you explore more of the html you begin to see that classes are applied to elements to style them.
For example:

* the `bg-primary` class is used to set the background color of the header to the primary color defined by Bootstrap.
* The `navbar` class is used to create a navigation bar with a dark background color.
* The `container` class is used to center the content on the page and add some padding.
* The `row` and `col` classes are used to create a grid layout with responsive columns.
* The `card` class is used to create a card component with an image and a button.

All of these help with creating a responsive and visually appealing website without having to write a lot of custom CSS.

Exercise 2
~~~~~~~~~~

Try getting the example working locally. Once you do our little website could use a footer.
There are many examples throughout bootstrap's documentation on how to create a footer.

Take a look here and see if you can copy an entire element, and it's nested elements, to create a footer for our website:
https://getbootstrap.com/docs/5.3/examples/footers/

.. important::

    Bootstrap is a very large framework with many components and utilities.
    This example only scratches the surface of what you can do with Bootstrap.
    Like vue.js, you should explore which CSS framework you want to use and if it fits your purpose.

    You can learn more about different CSS Frameworks by checking out the official documentation:

    * `Bootstrap <https://getbootstrap.com/>`_
    * `Tailwind CSS <https://tailwindcss.com/>`_
    * `UIKit <https://getuikit.com/>`_
    * `Bulma <https://bulma.io/>`_
    * `Material UI <https://material-ui.com/>`_

Building a web application locally
----------------------------------

Up to now we have been using CDN links to include libraries in our HTML files.
This is a good way to get started, but it is not the best way to build a web application.
In a real-world application, you would want to install the libraries locally and use a build tool to manage your code.

Now we will take a look at how to build a web application locally using Vue.js.
Vue.js uses `nodejs <https://nodejs.org/en>`_ and `npm <https://www.npmjs.com/>`_ to manage packages. Node is a Javascript runtime
environment. Think similarly how you can run `python` to run python code, you can run `node` to run javascript code.
Npm is a package manager for node. It allows you to install and manage packages for your node projects, similar
to how `pip` works for python.

Try the following steps to install Vue locally on your computer. 
You can also follow along on this page: https://vuejs.org/guide/quick-start.html.

Exercise 3
~~~~~~~~~~

#. Install `Node.js <https://nodejs.org/en/download>`_ on your computer. You can verify it's install by doing `node -v`.
#. Navigate to a directory to create a new Vue project, and run the following command:

   .. code-block:: shell

      npm create vue@latest 

#. Follow the prompots to create a new Vue Project.
#. Once the project is created, navigate to the project directory and run the following commands to install the required packages and run the development server.

   .. code-block:: bash

      npm install
      npm run format
      npm run dev 

#. Open your browser and navigate to url provided by your terminal to see your Vue app running locally.

You should now have a local Vue.js application running on your computer. 
You can start modifying the code in the `src` directory to build your application.
But say you reach a good point and are now ready to create 

You might notice on your new webpage that it says it is using `Vite <https://vitejs.dev/>`_.

It is a build tool that is used to bundle and optimize your Vue.js application for production.
Similar to how python comes with a development server, 
Vite comes with a development server that allows you to run your Vue.js application locally.
It also allows you to build your application for production, which is what we will do next.

.. note::

    Vite is a build tool that is used to bundle and optimize your Vue.js application for production.
    It is also the default build tool for Vue.js applications. We have simply covered a simple example using it,
    but there are many more features and options available.

    You can learn more about Vite by checking out the official documentation:
    https://vitejs.dev/guide/

When you are ready to deploy your application, you can run the following command to build your application for production:

.. code-block:: bash

   npm run build

This will create a `dist` directory in your project folder with all the files needed to run your application.
You can then deploy this directory to a web server or a cloud service like AWS, Azure, or Google Cloud.


Now that we have our code ready to ship, we can look at containerizing our code to easily
deploy it for production.

Containerizing Web Applications
-------------------------------

We have been using python for local web servers as well as npm which has wrapper to 
running vite commands to start a local server. However, when we are ready to deploy our application
we need to think about how we are going to run our application in production through a container.

We can take our vue.js application and containerize it. Think about the commands we needed to run for installing
node, npm, and vite. Combine that with what you have learned about containers, we can see that we can create a container
that has all the dependencies we need to run our application.

Exercise 4
~~~~~~~~~~

#. Create a ``Dockerfile`` in the root of your Vue.js project directory.
#. Add the following code to your Dockerfile.

   .. code-block:: dockerfile
      :linenos:

      # Stage 1: Build the Vue.js application
      FROM node:lts-alpine AS builder
  
      WORKDIR /app
  
      COPY package*.json ./
      RUN npm install
      COPY . .
      RUN npm run build
  
      # Stage 2: Serve the application with Nginx
      FROM nginx:alpine
      COPY --from=builder /app/dist /usr/share/nginx/html
      EXPOSE 80
      CMD ["nginx", "-g", "daemon off;"]

#. Build the Dockerfile

   .. code-block:: shell
    
      docker build -t vue-app .

#. Run the Docker container

   .. code-block:: shell

      docker run -p -d 8080:80 vue-app

#. Open your browser and navigate to ``http://localhost:8080`` to see your Vue.js application running in a Docker container.

There's a bit more happening here than we have seen in the past in terms of the Dockerfile.
Let's break it down a bit.

- The first line specifies the base image to use for the build stage. In this case, we are using the `node:lts-alpine` image, which is a lightweight version of Node.js.
- The `WORKDIR` command sets the working directory inside the container to `/app`.
- The `COPY` command copies the `package.json` and `package-lock.json` files to the working directory.
  These contain all the dependencies necessary to run the application.
- The `RUN npm install` command installs the dependencies specified in the `package.json` file.
- The second `COPY` command copies the rest of the application code to the working directory.
- The `RUN npm run build` command builds the Vue.js application for production.

- The second stage of the Dockerfile uses the `nginx:alpine` image to serve the built application.
- The `COPY --from=builder` command copies the built application from the first stage to the Nginx server's default HTML directory.
- The `EXPOSE` command exposes port 80 for the Nginx server.
- The `CMD` command starts the Nginx server.

Something we haven't seen before is a webserver that can actually serve our application.
`Nginx <https://nginx.org/en/docs/>`_ is a popular web server that is used to serve static files and reverse proxy requests to other servers.
In this case, we are using it to serve the built Vue.js application.

.. note::

    Nginx is a powerful web server that can be used to serve static files, reverse proxy requests, and load balance requests.
    It is widely used in production environments and is a good choice for serving web applications.
    You can learn more about Nginx by checking out the official documentation:
    https://nginx.org/en/docs/

Exercise 5
~~~~~~~~~~

Now that we have our docker container running we can build a docker-compose file to make running our application even easier.
Since we are using the ``CMD`` command we do not need to specify our command in our compose file to run our application.
We can simply give it the image we runt to run and expose the correct ports.

#. Create a ``docker-compose.yml`` file in the root of your Vue.js project directory.
#. Modify the file to create one service that uses the image we built in the previous exercise.
   You only need to add the ``image`` and ``ports`` keys to the service, but there are many other ways to configure it.
   

Additional Resources
---------------------

Web Frameworks

- `Vue.js <https://vuejs.org/>`_
- `React <https://reactjs.org/>`_
- `Angular <https://angular.io/>`_
- `Django <https://www.djangoproject.com/>`_

CSS Frameworks

- `Bootstrap <https://getbootstrap.com/>`_
- `Tailwind CSS <https://tailwindcss.com/>`_
- `UIKit <https://getuikit.com/>`_
- `Bulma <https://bulma.io/>`_
- `Material UI <https://material-ui.com/>`_ 

Web servers

- `Nginx <https://nginx.org/en/docs/>`_
- `Apache <https://httpd.apache.org/>`_