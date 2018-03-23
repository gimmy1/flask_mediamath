import os

base_dir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'myprecious'

DATABASE_PATH = os.path.join(base_dir, DATABASE)
