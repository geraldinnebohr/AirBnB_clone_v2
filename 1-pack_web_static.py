#!/usr/bin/python3
#Fabric script that generates a .tgz archive from the contents of the web_static folder
from fabric.api import local
from datetime import datetime


def do_pack():
    """Compress files in .tgz"""
    try:
        local("mkdir -p versions")
        time = datetime.now()
        date = time.strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_" + date
        local("tar -cvzf {}.tgz web_static".format(path))
        return path
    except:
        return None
