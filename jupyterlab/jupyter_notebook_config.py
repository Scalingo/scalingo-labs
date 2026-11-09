#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import getpass

from jupyter_server.auth import passwd
from pgcontents import PostgresContentsManager, PostgresCheckpoints


c = get_config()  # noqa

c.ServerApp.ip = '*'
c.ServerApp.port = int(os.getenv("PORT"))
c.ServerApp.open_browser = False

jupyter_token = os.environ.get("JUPYTER_TOKEN")
if jupyter_token:
    c.IdentityProvider.token = jupyter_token

# jupyter_passwd = os.environ.get("JUPYTER_PASSWORD")
# if jupyter_passwd:
#    c.ServerApp.password = passwd(jupyter_passwd)
c.PasswordIdentityProvider.allow_password_change = False

# Tell IPython to use PostgresContentsManager for all storage.
c.ServerApp.contents_manager_class = PostgresContentsManager

# Set the url for the database used to store files.  See
# http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#postgresql
# for more info on db url formatting.
# pgcontents is supposed to support PGCONTENTS_DB_URL to store the database
# URL.
# The code shows that the variable is called DB_URL_ENVVAR.
# Unfortunately none of them seems to work.
# We still use PGCONTENTS_DB_URL, but set it explicitely:
c.PostgresContentsManager.db_url = os.getenv("PGCONTENTS_DB_URL")

# Use /bin/bash as shell inside JupyterLab
c.ServerApp.terminado_settings = {'shell_command': ['/bin/bash']}

# Set a maximum file size, if desired.
c.PostgresContentsManager.max_file_size_bytes = 1000000  # 1MB File cap
