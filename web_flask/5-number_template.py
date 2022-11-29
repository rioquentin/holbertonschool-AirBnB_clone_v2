#!/usr/bin/python3
"""Flask Web app starter"""


from flask import Flask
from flask import render_template


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


"""
Route for /python and display function of /python/<text>
to print the value of the
text variable
"""


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python(text="is cool"):
    """def"""
    new = text.replace("_", " ")
    return "Python {}".format(new)


@app.route("/number/<int:number>", strict_slashes=False)
def Num(number):
    """def"""
    return "{} is a number".format(number)


@app.route("/number_template/<int:n>", strict_slashes=False)
def Num_Html(n):
    """def"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
