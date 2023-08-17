#!/usr/bin/python3
"""Run a flask app that returns Hello HBNB"""
from flask import Flask

app = Flask(__name__)

@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_airbnb():
    """Return hello NMBB for /airbnb-onepage/"""
    return "Hello HBNB!"

@app.route("/airbnb-dynamic/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Return a message based on whether n is odd or even"""
    if n % 2 == 0:
        return f"{n} is
