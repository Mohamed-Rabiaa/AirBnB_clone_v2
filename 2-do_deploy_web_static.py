#!/usr/bin/python3
"""
This script distributes an archive to your web servers,
using the function do_deploy
"""


import os
from fabric.api import put, run, env


env.hosts = ['52.90.0.3', '54.210.51.202']
env.user = 'ubuntu'


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
