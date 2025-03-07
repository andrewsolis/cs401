Flask Special Topics
====================


Writing Unit Tests for Flask
----------------------------

There are several different approaches for writing *unit tests* for Flask apps,
some of which are included in the Flask documentation. One approach 
which is most congruent with the topics we already covered in this class,
is to instead write *integration tests*. 

For these tests, the key thing is that you have to have an actual copy of your
Flask server running. Then, the tests will perform requests.get() to the various
routes and you can evaluate the output. Be careful to make sure that your tests
are independent of the data, which may change over time. The job of these unit
tests is not to check / validate that the right data is being returned; rather,
the goal is to make sure the routes work and return the right kind of response.

If your code also has standalone functions separate from the functions decorated
as Flask routes, (e.g., you may have written helper functions inside of your file
that are not routes but help process or retrieve data), then you would still want to import
those and test them as normal in your unit test file.

Consider the previous code we made for getting degrees with different HTTP requests.

.. code-block:: python3
   :linenos:

   from flask import Flask
   from flask import request

   data = [ {'id': 0, 'year': 1990, 'degrees': 5818},
            {'id': 1, 'year': 1991, 'degrees': 5725},
            {'id': 2, 'year': 1992, 'degrees': 6005},
            {'id': 3, 'year': 1993, 'degrees': 6123},
            {'id': 4, 'year': 1994, 'degrees': 6096} ]


   app = Flask(__name__)

   @app.route('/degrees', methods=['GET', 'DELETE'])
   def degrees():

      global data

      if request.method == 'GET':
         return(data)
      elif request.method == 'DELETE':
         content = request.get_json()
         new_data = []
         for item in data:
               if item['id'] != content['id']:
                  new_data.append(item)
         data = new_data
         return(data)

   @app.route('/degrees/<int:id>', methods=['GET'])
   def degrees_for_id(id):

      for x in data:
         if x['id'] == id:
               return x
      
      return f"Error: ID {id} not found."

   @app.route('/degrees/<int:id>/degrees', methods=['GET'])
   def only_degrees_for_id(id):

      for x in data:
         if x['id'] == id:
               return {'id' : id, 'degrees': x['degrees'] }
         
      return f"Error: ID {id} not found."

   if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0')

Look at the following pytest snippet that tests the /degrees and /degrees/<int:id>
routes:


.. code-block:: python3
   :linenos:

    import requests
    import logging


    def test_degrees_route():

        response1 = requests.get('http://127.0.0.1:5000/degrees')

        logging.debug(f"Response from /degrees: {response1.json()}")  

        assert response1.status_code == 200
        assert isinstance(response1.json(), list) == True
        assert len(response1.json()) == 5

        assert response1.json()[0]['id'] == 0
        assert response1.json()[0]['year'] == 1990
        assert response1.json()[0]['degrees'] == 5818
        assert response1.json()[1]['id'] == 1
        assert response1.json()[1]['year'] == 1991
        assert response1.json()[1]['degrees'] == 5725

    def test_specific_degree_route():

        response2 = requests.get('http://127.0.0.1:5000/degrees/' + str(1))

        assert response2.status_code == 200
        assert isinstance(response2.json(), dict) == True
        assert len(response2.json()) == 3

        assert response2.json()['id'] == 1
        assert response2.json()['year'] == 1991
        assert response2.json()['degrees'] == 5725



These lines may need to be modified depending on the format of data returned by
your API. And, as mentioned above, it assumes these tests are performed when your
API is already running.


Reverse Proxy with ``ngrok``
----------------------------

Up to now, our Flask apps have been isolated to their host hardware. What if 
we want to access our Flask apps from outside our host hardware? A utility
called ``ngrok`` can be used to provide a reverse proxy on the fly.

.. note::
 
   To do this, you need an ngrok account and access token, which can be
   obtained `here <https://dashboard.ngrok.com/signup>`_

First, install ``ngrok`` by following this `tutorial <https://dashboard.ngrok.com/get-started/setup/windows>`_ 
once your account is created and setup.

Confirm ``ngrok`` is working and add your
`access token <https://dashboard.ngrok.com/get-started/your-authtoken>`_:

.. code-block:: console

   [terminal]$ ngrok --help
   NAME:
     ngrok - tunnel local ports to public URLs and inspect traffic
   ...
   [terminal]$ ngrok config add-authtoken <TOKEN>
   Authtoken saved to configuration file: /home/ubuntu/.config/ngrok/ngrok.yml


Assuming you have a Flask app running on ``localhost`` and port ``5000``, then
do the following: 

.. code-block:: console

   [terminal]$ ngrok http http://localhost:5000


This will lock your terminal into an interface that looks like the following:

.. code-block:: console

   ngrok
   
   Policy Management Examples http://ngrok.com/apigwexamples        

   Session Status                online
   Account                       andrew solis (Plan: Free)   
   Update                        update available (version 3.18.2, Ctrl-U to update)
   Version                       3.17.0
   Region                        United States (us)
   Latency                       34ms
   Web Interface                 http://127.0.0.1:4040
   Forwarding                    https://022d-136-62-4-166.ngrok-free.app -> http://localhost:5000

   Connections                   ttl     opn     rt1     rt5     p50     p90
                                 0       0       0.00    0.00    0.00    0.00

Navigate to or curl the link provided to access your Flask app from outside
your system. Press ``Ctrl+C`` to quit forwarding.


Flask and HTML
--------------

Flask has the ability to render HTML templates that contain a mix of static data
and variables (for run-time dynamic data). The route you write will take the 
template from a predefined location, inject any variables, and render it into
a final HTML document to return to the client.

In your Flask project directory, create a folder called ``templates`` and add
the following HTML document as ``example.html``. It uses Jinja syntax for
injecting dynamic data (``{{name}}``):

.. code-block:: html

   <!DOCTYPE html>
   <html>
   <head>
       <title>Flask Templating Example</title>
   </head>
   <body>
       <h1>Hello, {{name}}!</h1>
       <p>This file should be stored in the "templates" folder as "example.html"</p>
   </body>
   </html>

Then, adapt the ``/<name>`` Flask route to return that HTML document using Flask's 
``render_template()`` method. The old version of the route which returns a plain
string is also provided as reference. 

.. code-block:: python3
   :linenos:

   from flask import Flask, render_template
   
   app = Flask(__name__)
   
   @app.route('/<name>', methods=['GET'])
   def hello_name(name):
       return render_template('example.html', name=name)

   ### For reference, this is the /<name> route without render_template
   # @app.route('/<name>', methods=['GET'])
   # def hello_name(name):
   #     return f'Hello, {name}!\n'
   
   if __name__ == '__main__':
       app.run(debug=True, host='0.0.0.0')

   



Additional Resources
--------------------

* `Ngrok <https://dashboard.ngrok.com/signup>`_
* `Flask Templates <https://flask.palletsprojects.com/en/2.3.x/tutorial/templates/>`_
