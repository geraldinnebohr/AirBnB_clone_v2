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


@app.route('/hbnb_filters')
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
    # amenities
    list_amenities = []
    amenities = storage.all('Amenity')
    for key in amenities:
        amenity = amenities[key].name
        list_amenities.append(amenity)
    list_amenities.sort()
    print(amenities)
    return (render_template('10-hbnb_filters.html', city_list=city_list, list2=list2, list_amenities=list_amenities))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
