#!/usr/bin/python3
'''Importing Flask form flask'''
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C {}'.format((text).replace("_", " "))

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python(text ='is cool'):
    return 'Python {}'.format((text).replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
        return '{} is a number'.format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
     if (n % 2) == 0:
        return render_template('6-number_odd_or_even.html', number=n, even_odd= 'even')
     else:
        return render_template('6-number_odd_or_even.html', number=n, even_odd= 'odd')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
