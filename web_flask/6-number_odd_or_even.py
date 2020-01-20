#!/usr/bin/python3
"""Starting flask web application"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/number_odd_or_even/<int:n>')
def is_odd_or_even(n):
    """display or or even number in template"""
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/number_template/<int:n>')
def is_template(n):
    """display number in template"""
    return render_template('5-number.html', n=n)


@app.route('/number/<int:n>')
def is_number(n):
    """display C followed by text variable"""
    return '%d is a number' % n


@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    """display python followed by text variable"""
    url_friendly = text.replace('_', ' ')
    return 'Python %s' % url_friendly


@app.route('/c/<text>')
def c_text(text):
    """display C followed by text variable"""
    url_friendly = text.replace('_', ' ')
    return 'C %s' % url_friendly


@app.route('/hbnb')
def hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/')
def hello():
    """display Hello HBNB"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
