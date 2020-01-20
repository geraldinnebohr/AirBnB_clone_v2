#!/usr/bin/python3
"""Starting flask web application"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


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
