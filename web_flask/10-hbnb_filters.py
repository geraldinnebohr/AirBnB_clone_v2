#!/usr/bin/python3
"""Starting flask web application"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def db(x=None):
    """remove the current session"""
    storage.close()


@app.route('/hbnb_filters')
def states():
    """display html page"""
    return (render_template('10-hbnb_filters.html', list2=list2))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
