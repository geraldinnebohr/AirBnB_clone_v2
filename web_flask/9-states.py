#!/usr/bin/python3
"""Starting flask web application"""
from flask import Flask
from flask import render_template
from models import storage
import shlex
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def db(x=None):
    """remove the current session"""
    storage.close()


@app.route('/states')
def states():
    """display html page"""
    my_list = []
    objects = storage.all('State')
    for key in objects:
        values = objects[key].name + '.' + objects[key].id
        my_list.append(values)
    my_list.sort()
    list2 = []
    for key in my_list:
        key = key.replace('.', ' ')
        key = shlex.split(key)
        list2.append((key[0], key[1]))
    return (render_template('9-states.html', id=None, list2=list2))


@app.route('/states/<id>')
def state_id(id):
    my_list = []
    objects = storage.all('State')
    for key in objects:
        values = objects[key].name + '.' + objects[key].id
        my_list.append(values)
    my_list.sort()
    list2 = []
    for key in my_list:
        key = key.replace('.', ' ')
        key = shlex.split(key)
        list2.append((key[0], key[1]))
    # cities by state in id
    list_c = []
    objs = storage.all('City')
    for k in objs:
        val = objs[k].name + '.' + objs[k].id + '.' + objs[k].state_id
        list_c.append(val)
    list_c.sort()
    city_list = []
    for key in list_c:
        key = key.replace('.', ' ')
        key = shlex.split(key)
        city_list.append((key[0], key[1], key[2]))
    s_name = None
    for k in list2:
        if k[1] == id:
            s_name = k[0]
    return (render_template('9-states.html', id=id,
                            city_list=city_list, s_name=s_name))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
