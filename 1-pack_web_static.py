#!/usr/bin/python3
"""
This script generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack
"""


import tarfile
import os
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo
    """
    time = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    if not os.path.isdir('versions'):
        os.mkdir('versions')
    tar_file = "versions/web_static_{}.tgz".format(time)
    create_tgz(tar_file, "web_static")
    if os.path.exists(tar_file):
        return tar_file
    else:
        return None


def create_tgz(tar_file, dir):
    """ Creates a tgz file """
    with tarfile.open(tar_file, "w:gz") as tar:
        tar.add(dir, arcname=os.path.basename(dir))
