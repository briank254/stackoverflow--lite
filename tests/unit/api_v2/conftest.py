"""
Fixtures for apiV2
"""
import os
import pytest
import psycopg2

from app_v2 import create_app


@pytest.fixture(scope='module')
def test_client(request):
    """
    Flask testclient setup
    """
    app = create_app('testing')
    app_client = app.test_client()

    ctx = app.app_context()
    ctx.push()
    database = app.config['DATABASE']
    print ("db", database)
    yield app_client

    def drop():
        '''
        Function to be run at end of test
        '''
        print('deleting data')

        conn = psycopg2.connect(database)

        cur = conn.cursor()

        queries = ('''DELETE FROM answers''', '''DELETE FROM questions''', '''DELETE FROM users''')

        for query in queries:
            cur.execute(query)

        cur.close()

        conn.commit()

        conn.close()

        ctx.pop()

    request.addfinalizer(drop)