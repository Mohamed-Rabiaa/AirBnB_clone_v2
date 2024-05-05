#!/usr/bin/python3
"""
This script generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack
"""

import os
from datetime import datetime
from fabric.api import local


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
