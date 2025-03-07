import json
import logging

from flask import Flask, request


app = Flask(__name__)

# Helper function to retrieve data from the movies.json file
def get_data() -> list[dict]:
    """
    Retrieve the movies dataset and return it as a list of dictionaries.

    Returns:
        data (list[dict]): A list of dictionaries containing the movies dataset.
    """
    with open('movies.json', 'r') as file:
    
        data = json.load(file)

    return data


# TODO: Add a route to return the entire dataset

# TODO: Add a route, or modify an existing route, to return the movies that are between a certain release year range

# TODO: Add a route to return a movie if it matches the id

# TODO: Add a route to return the genres for a specific movie

# TODO: Add a route to return a movie if it matches the title

# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')