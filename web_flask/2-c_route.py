#!/usr/bin/python3
"""Flask Web app starter"""


from flask import Flask


app = Flask(__name__)

"""Base route"""


@app.route("/", strict_slashes=False)
def hello_world():
    """doc"""
    return "Hello HBNB!"


"""Route for /hbnb"""


@app.route("/hbnb", strict_slashes=False)
def hello():
    """doc"""
    return "HBNB"


"""
Route for /c and display function of /c/<text> to print the value of the
text variable
"""


@app.route("/c/<text>", strict_slashes=False)
def C(text=None):
    """def"""
    new = text.replace("_", " ")
    return "C {}".format(new)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
