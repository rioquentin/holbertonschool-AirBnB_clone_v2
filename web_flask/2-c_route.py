#!/usr/bin/python3

"""Flask Web app starter"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)

"""Base route"""

@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"

"""Route for /hbnb"""

@app.route("/hbnb", strict_slashes=False)
def hello():
    return "HBNB"

"""
Route for /c and display function of /c/<text> to print the value of the
text variable
"""

@app.route("/c/<text>", strict_slashes=False)
def C(text=None):
    new = text.replace("_", " ")
    return f"C {escape(new)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
