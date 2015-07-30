WTF_CSRF_ENABLED = True
SECRET_KEY = 'i-am-an-octopus-under-the-sea'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://nickt:profound@mysql.nickt.suzyogi.com/nickt_blog'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')