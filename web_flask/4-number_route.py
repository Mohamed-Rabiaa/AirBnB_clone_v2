#!/usr/bin/python3
""" This script starts a Flask web application """


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Displays Hello HBNB! on the home page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB on the hbnb page"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """Displays 'C' followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route("/python/")
@app.route("/python/<text>")
def python(text="is cool"):
    """ Displays 'Python', followed by the value of the text variable """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route("/number/<int:n>")
def number(n):
    """ Displays {n} is a number” only if n is an integer """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
