#!/usr/bin/python3
"""Run a flask app that returns Hello HBNB"""
from flask import Flask

app = Flask(__name__)

@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_airbnb():
    """Return hello NMBB for /airbnb-onepage/"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
