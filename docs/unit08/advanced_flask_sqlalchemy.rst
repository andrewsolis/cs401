Advanced Flask-SQLAlchemy
=========================

We have been learning some basics of using flask-sqlalchemy and how we use it
for creating and connecting to our database. Now, we will look at more advanced
topics in Flask-SQLAlchemy and how to properly integrate it into a full flask app.

After this module, students should be able to:

#. Understand how to set up Flask-SQLAlchemy in a Flask application.
#. Perform CRUD (Create, Read, Update, Delete) operations using Flask-SQLAlchemy.
#. Use Flask-Migrate to handle database migrations in a Flask application.
#. Understand the relationship between Flask-SQLAlchemy and Flask-Migrate.

Initial Setup
-------------

Checkout the repository for this module from GitHub to see all the files needed `here <https://github.com/andrewsolis/cs401/tree/main/scripts/db>`_.

There are 4 total files that should look like this below:

.. code-block:: text

    ├── .gitignore
    ├── app.py
    ├── populate.py
    ├── requirements.txt

Open up a terminal and navigate to the directory where these files are located
and create a new virtual envrionment, load it, and install the required packages
from the `requirements.txt` file.

.. code-block:: bash

    $ python3 -m venv movies
    $ source movies/bin/activate  # On Windows use `movies\Scripts\activate`
    $ pip install -r requirements.txt

.. caution::

    Be sure to change the port in **app.py** if it is different.

Make sure that the docker container for PostgreSQL is running along with a docker volume.
If you have not set it up yet, you can do so by running the following commands to setup
a docker volume and run a PostgreSQL container:

.. code-block:: bash

    $ docker volume create pgdata
    $ docker run --name db -e POSTGRES_PASSWORD=secret -v pgdata:/var/lib/postgresql/data -p 5433:5432 -d postgres:17.4

Try running the ``populate.py`` and see if it populates the database correctly. After you
run the script, you should see a message indicating that the database has been created
and the movies it imports.

.. code-block:: bash

    $ python manage.py 
                              
    Database reset: all tables dropped and recreated.
    Movie 'Inception' added to the database.
    Movie 'The Godfather' added to the database.
    Movie 'The Dark Knight' added to the database.
    Movie 'Pulp Fiction' added to the database.
    Movie 'Schindler's List' added to the database.
    Movie 'The Shawshank Redemption' added to the database.
    Movie 'Forrest Gump' added to the database.
    Movie 'The Matrix' added to the database.
    Movie 'Fight Club' added to the database.
    Movie 'Interstellar' added to the database.
    Movie 'The Lord of the Rings: The Return of the King' added to the database.

If all is correct you should be good to go. 

Templates
---------

If you start your flask app and navigate to http://localhost:5000/, you will see a simple
"Hello, World!" message. Let's enhance this by creating a home page that displays
a list of all movies in the database. 

Crea a new directory ``templates`` and add two files inside : `index.html` and `base.html`. 
Paste the following inside the `base.html` page:

.. code-block:: html
    :linenos:
    :emphasize-lines: 5,34,20

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{% block title %} {% endblock %} - Flask App</title>
        <style>
        </style>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="{{ url_for('index') }}">Flask App</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="{{ url_for('index') }}">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Create</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">About</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <hr>
        <div class="content">
            {% block content %} {% endblock %}
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>

There are a few lines worth noting in our ``base.html`` file.

#. The `{% block title %}` is a placeholder for the title of the page that can be
   overridden in other templates.
#. The `url_for('index')` is a Flask function that generates the URL for the `index` route.
#. The `{% block content %}` is a placeholder for the main content of the page

Our **base.html** file is what we will use as our base template for other pages on our website.
By using the **block** tags, we can inject only the content we want to change in 
our other templates that extend this template. Let's see an example below.

Paste the following inside of the `index.html` file:

.. code-block:: html
    :linenos:
    :emphasize-lines: 1,3,7

    {% extends 'base.html' %}

    {% block content %}
        <h1 class="title text-center my-4">{% block title %} Movies {% endblock %}</h1>
        <div class="container">
            <div class="row">
                {% for movie in movies %}
                    <div class="col-md-4 mb-4">
                        <div class="card h-100">
                            <div class="card-body">
                                <h5 class="card-title">#{{ movie.id }} - {{ movie.title }}</h5>
                                <p class="card-text"><strong>Year:</strong> {{ movie.year }}</p>
                                <p class="card-text"><strong>Directors:</strong> {{ movie.directors }}</p>
                                <p class="card-text"><strong>MPA:</strong> {{ movie.MPA }}</p>
                                <p class="card-text"><strong>Rating:</strong> {{ movie.rating }}</p>
                                <p class="card-text"><strong>Genres:</strong> {{ movie.genres }}</p>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        </div>
    {% endblock %}

* Line 1 shows that we are extending the ``base.html`` template, so we are re-using the html structure we defined there.
* Line 3 is overriding the **content** block of our ``base.html`` file. 
  We have an  associated ``endblock`` at the end of the file to close the block of all the code we 
  want to inject inside our base template.
* Line 7 is a for loop that iterates over the `movies` variable passed from our Flask route.

For both the **base.html** and **index.html** files, we are using ``Bootstrap`` to style our
HTML.

.. note::

    Templates are powerful tools in Flask that allow us to separate our HTML structure
    from our application logic. By using templates, you can create templates quicker
    and easier, and maintain a consistent look and feel across your application.

    To learn more about templates, check out the Flask documentation: 
    `Flask Templates <https://flask.palletsprojects.com/en/stable/tutorial/templates/>`_.

Now that we have our templates, we need to modify our `app.py` file to render the 
`index.html` template and pass the list of movies to it.

Let's modify our ``app.py`` file and `/` route to render the `index.html` template.

.. code-block:: python
    :linenos:
    :emphasize-lines: 8,9

    from database.models import Movie
    from database.config import app, db
    from flask import jsonify, render_template


    @app.route('/', methods=['GET'])
    def index():
        movies = db.session.scalars(db.select(Movie)).all()
        return render_template('index.html', movies=movies )

    if __name__ == '__main__':
        app.run(debug=True) # Set debug=True for development, change to False in production

* Line 8 is performing a query to select all movies from the database, and store them in a variable called **movies**.
* Line 9 is rendering the `index.html` template and passing the **movies** variable to it.

Now, if you start your Flask app and navigate to http://localhost:5000/, you should see
a list of all movies displayed on the page.

Up until now we have been using the same query to retrieve all movies from the database.
However, we have not look at what this is actually doing, and how we can use it for more
complex queries.

Queries
--------

Flask-SQLAlchemy provides a powerful query interface that allows you to perform
complex queries on your database. Let's breakdown the query we used in our `app.py` file:

.. code-block:: python
    
    movies = db.session.scalars(db.select(Movie)).all()

* `db.session`: This is the current database session that allows you to interact with the database.
* `db.select(Movie)`: This creates a SQL SELECT statement for the `Movie` model.
* `db.session.scalars(...)`: This executes the query and returns the results as a list of scalars.
* `.all()`: This retrieves all results from the query.

Usually most queries use **db.session.execute()** to execute the query, but in this case
we are using **db.session.scalars()** to retrieve the results as a list of objects.

If you were to use **db.session.scalars.execute()** the results would be given as
a list of tuples instead of a list of objects, so scalars is a helper function
that simplifies the process of retrieving results as objects. 

Most queries follow this similar pattern where inside of the ``execute`` or ``scalars`` 
function is a select option. However, this can be further customized to 
perform more complex queries. 

For example, if we wanted to filter the movies by a specific year, say 1999, we can modify
our query like this:

.. code-block:: python
    :linenos:
    
    db.session.scalars(db.select(Movie).where(Movie.year == 1999)).all()

This query adds a **WHERE** clause, similar to SQL, where we are filtering
and only returning movies that have a year of 1999.

Say we wanted our results to be ordered by the movie title in ascending order, we can modify
our query like this:

.. code-block:: python
    
    db.session.scalars(db.select(Movie).where(Movie.year == 1999).order_by(Movie.title)).all()

Here we are adding a ``.order_by(Movie.title)`` clause to our query to order the results
by the movie title in ascending order.

.. note::

    A true understanding of all the available options for a query is beyond the scope of 
    this module. However, you can find more information about the available options, 
    including joins, in the SQLAlchemy documentation: `SQLAlchemy Query Guide <https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html>`_.

CRUD Operations
---------------

We've mostly covered basic operations through the flask shell and the `populate.py` script
to add data to our database. We have a simple route that returns the entire dataset
at the index route ``/``. 

Now, we want to add more routes into our app
so that we can perform **CRUD** (**C** reate, **R** ead, **U** pdate, **D** elete) operations through HTTP requests.

Each of these operations will be mapped to a specific route in our Flask application
to support a specific action to our data:

* **Create**: Add a new movie to the database.
* **Read**: Retrieve a list of all movies or a specific movie by its ID.
* **Update**: Update the details of an existing movie.
* **Delete**: Remove a movie from the database.

The same idea can be said for any other model you create in any application. You can
follow the same pattern to create methods that perform CRUD operations for any 
model you define, regardless of if it's created in flask, or any other software application.

Create
~~~~~~~

Template & Route
^^^^^^^^^^^^^^^^

UP to now we have only been able to view those records that we added to our database through a script or command line.
However, traditionally you  want to be able to add new models to our database through a web interface.

Let's create a template that will be a form that users fill out.
Create a new file in the `templates` directory called `create.html` and paste the following code inside:

.. code-block:: html

    {% extends 'base.html' %}

    {% block content %}

    <div class="container mt-5">
      <h1 class="text-center mb-4">Add a New Movie</h1>
      <form action="/create" method="post" class="needs-validation" novalidate>
        <div class="mb-3">
          <label for="title" class="form-label">Title:</label>
          <input type="text" id="title" name="title" class="form-control" required>
        </div>

        <div class="mb-3">
          <label for="year" class="form-label">Year:</label>
          <input type="number" id="year" name="year" class="form-control" required>
        </div>

        <div class="mb-3">
          <label for="directors" class="form-label">Directors:</label>
          <input type="text" id="directors" name="directors" class="form-control" required>
        </div>

        <div class="mb-3">
          <label for="released_in_theatre" class="form-label">Released in Theatre:</label>
          <select id="released_in_theatre" name="released_in_theatre" class="form-select" required>
            <option value="True">Yes</option>
            <option value="False">No</option>
          </select>
        </div>

        <div class="mb-3">
          <label for="mpa" class="form-label">MPA Rating:</label>
          <input type="text" id="mpa" name="mpa" class="form-control" required>
        </div>

        <div class="mb-3">
          <label for="genres" class="form-label">Genres:</label>
          <input type="text" id="genres" name="genres" class="form-control" required>
        </div>

        <div class="mb-3">
          <label for="duration" class="form-label">Duration (in minutes):</label>
          <input type="number" id="duration" name="duration" class="form-control" required>
        </div>

        <div class="mb-3">
          <label for="rating" class="form-label">Rating:</label>
          <input type="number" id="rating" name="rating" class="form-control" step="0.1" min="0" max="10" required>
        </div>

        <button type="submit" class="btn btn-primary w-100">Add Movie</button>
      </form>
    </div>

    {% endblock %}

We have a new create page and now we need to add a route to our `app.py` file
to handle the form submission and add a new movie to the database.

Create a new route in your `app.py` file that handles the create page:

.. code-block:: python

    @app.route('/create', methods=['POST', 'GET'])
    def create():
        return render_template('create.html')

Lastly, lets add our link to the navigation bar so that a user can click the 
create link and be taken to the create page. Modify the ``base.html`` file
links to look like below.

.. code-block:: html

    <ul class="navbar-nav">
        <li class="nav-item">
            <a class="nav-link" href="{{ url_for('index') }}">Home</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="{{ url_for('create') }}">Create</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">About</a>
        </li>
    </ul>

You should now be able to navigate to the create page and see the form.
Fill it out and click submit and see what happens.

POST Request
^^^^^^^^^^^^^^^^

Right now the route is only rendering the template and not doing anything with the data
that is submitted. We need to modify the route to handle the form submission and
add a new movie to the database.
We can do this by checking if the request method is POST and then
creating a new movie object and adding it to the database.

Modify the `create` route in your `app.py` file handle the form submission:

.. code-block:: python
    :linenos:

    from flask import request, redirect, url_for

    @app.route('/create', methods=['POST', 'GET'])
    def create():
        if request.method == 'POST':
            title = request.form.get('title')
            year = request.form.get('year')
            directors = request.form.get('directors').split(',')
            released_in_theatre = True if request.form.get('released_in_theatre') == "True" else False
            mpa = request.form.get('mpa')
            genres = request.form.get('genres').split(',')
            duration = request.form.get('duration')
            rating = request.form.get('rating')

            new_movie = Movie(title=title, year=year, directors=directors,
                              theatre=released_in_theatre,
                              MPA=mpa, genres=genres, duration=duration,
                              rating=rating)

            db.session.add(new_movie)
            db.session.commit()

            return redirect(url_for('index'))

        return render_template('create.html')

We are doing a few things to process the form submission.

* line *5* is checking if the request method is POST, which means the form has been submitted.
* line *6-13* is getting the data from the form and storing it in variables. Note that any 
  data we request is stored in the `request.form` dictionary as a string. For numbers and
  arrays we have to be sure to cast them to the correct type.
* line *15* is creating a new `Movie` object with the data from the form.
* line *20* is adding the new movie to the database session.
* line *21* is committing the changes to the database.
* line *23* is redirecting the user back to the index page after the movie has been added.
* line *25* is rendering the create template if the request method is GET.

Take a look at the create page and fill out the form with a new movie.
You should see the new movie added to the database and displayed on the index page.

Read
~~~~~

Exercise 1
^^^^^^^^^^^^^

Now that we have a way to add new movies to the database, we need a way to view
existing movies. We can do this by creating a new route that handles the view
request and a new template that displays the details of a movie.

* Create a new file in the `templates` directory called `view.html`.
* Create a new route in your `app.py` file that handles the view request.
* Modify the `index.html` file to add a link to the view page for each movie.
* Modify the `view` route to retrieve the movie from the database and pass it to the template.
* Modify the `view.html` file to display the details of the movie.
* Test the view functionality by clicking on a movie in the index page and checking if the details are displayed correctly.

Update
~~~~~~

While GET and POST can be used for forms, PUT and DELETE are not allowed to be used for forms.
Instead of creating pages for these, we instead will create simple routes that handle
the requests and return a JSON response.

**PUT** is the equivalent of an update request, and is used to update an existing resource.

Let's create a new route in your `app.py` file that handles the update request:

.. code-block:: python

    @app.route('/update/<int:id>', methods=['PUT'])
    def update(id):
        movie = db.session.get(Movie, id)
        if not movie:
            return jsonify({'error': 'Movie not found'}), 404

        data = request.get_json()
        for key, value in data.items():
            setattr(movie, key, value)

        db.session.commit()
        return jsonify({'message': 'Movie updated successfully'}), 200


Here we are first checking to see if the movie exists. If it does not exist, we return
a 404 error. If it does exist, we get the data from the request and update the movie
object with the new data. Finally, we commit the changes to the database and return
a success message.

Though we are only using the **id** variable to identify the movie, there is actually
JSON that is being sent along with the PUT request that contains the new data for the movie.

The `request.get_json()` method gets the JSON data from the request.
Try sending a PUT request in Postman to the `/update/<id>` route with the following JSON data:

.. code-block:: json

    {
        "title": "Chaminade : The Movie",
        "year": 2025,
        "directors": ["Rylan Chong"],
        "released_in_theatre": "yes",
        "mpa": "PG-13",
        "genres": ["Action", "Drama"],
        "duration": 120,
        "rating": 8.5
    }

See if it updates the movies on the website if it says it is successful.

Delete
~~~~~~~~

Exercise 2
^^^^^^^^^^^^^

Now that we have a way to update movies in the database, we need a way to delete
movies from the database. We can do this by creating a new route that handles the delete
request.

* Create a new route in your `app.py` file that handles the delete request.
* Check if the movie exists in the database and delete it if it does.
* Return a JSON response indicating whether the movie was deleted successfully or not.
* Test the delete functionality by sending a DELETE request to the delete route with a movie ID.

Additional Resources
---------------------

Materials in this module were based on the following resources

* `Digital Ocean Tutorial <https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application>`_
* `Flask-SQLAlchemy <https://flask-sqlalchemy.readthedocs.io/en/stable/>`_

----------

* `SQLAlchemy Query Guide <https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html#orm-queryguide-select-orm-entities>`_
* `Postman CRUD Operations <https://www.postman.com/ssr-swaraj25/api-fundamentals-using-postman/collection/9au8ldv/restful-api-basics-crud-test-variable>`_