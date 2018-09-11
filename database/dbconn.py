"""Database Config"""

import psycopg2
from flask import current_app

def dbconn():
    conn = psycopg2.connect(current_app.config['DATABASE'])
    return conn
    