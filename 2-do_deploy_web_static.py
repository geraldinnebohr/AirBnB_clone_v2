#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import put, env, run
import os.path
import re

env.hosts = ['34.73.35.58', '34.74.63.9']


def do_deploy(archive_path):
    """Compress files in .tgz"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        filename = re.search('versions/(.*).tgz', archive_path)
        run('mkdir -p /data/web_static/releases/{}'.format(filename.group(1)))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'
            .format(filename.group(1), filename.group(1)))
        run('rm /tmp/{}.tgz'.format(filename.group(1)))
        run('mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/'
            .format(filename.group(1), filename.group(1)))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(filename.group(1)))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(filename.group(1)))
        return True
    except:
        return False
