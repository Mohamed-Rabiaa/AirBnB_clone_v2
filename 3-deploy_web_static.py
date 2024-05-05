#!/usr/bin/python3
"""
This script creates and distributes an archive to your web servers,
using the function deploy
"""

import os
from datetime import datetime
from fabric.api import local, put, run, env


env.hosts = ['52.90.0.3', '54.210.51.202']
env.user = 'ubuntu'


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo
    """
    if not os.path.isdir('versions'):
        local('mkdir -p versions')

    time = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    result = local('tar -cvzf versions/web_static_{}.tgz web_static'
                   .format(time), capture=True)
    if result.succeeded:
        return result
    else:
        return None


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if not os.path.exists(archive_path):
        return False

    result = put(archive_path, '/tmp/')
    if result.succeeded:
        file_name = archive_path.replace("versions/", "")
        arc_dir = file_name.replace(".tgz", "")
        path = "/data/web_static/releases/{}".format(arc_dir)
        run('mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path))
        return True
