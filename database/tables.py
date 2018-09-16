"""
Create db table
"""

import psycopg2

QUERIES = (
    """
    CREATE TABLE IF NOT EXISTS users(
        user_id SERIAL PRIMARY KEY NOT NULL,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(100) NOT NULL
        )
    """,

    """
    CREATE TABLE IF NOT EXISTS questions(
        question_id SERIAL PRIMARY KEY NOT NULL,
        user_id int null references users(user_id)on delete cascade,
        title VARCHAR(80) NOT NULL UNIQUE,
        question VARCHAR(500) NOT NULL,
        answers int default 0
        )
    """,

    """
    CREATE TABLE IF NOT EXISTS answers(
        answer_id SERIAL PRIMARY KEY NOT NULL,
        user_id int null references users(user_id) on delete cascade,
        question_id int references questions(question_id) on delete cascade,
        answer VARCHAR(500) NOT NULL,
        status varchar(80) default 'pending'
        )
    """
)

def create_tables(db_url):
    """
    Create tables for the database
    """
    
    conn = psycopg2.connect(db_url)

    cur = conn.cursor()
    #create tables
    for query in QUERIES:
        cur.execute(query)

    cur.close()

    conn.commit()

    conn.close()


if __name__ == '__main__':
    create_tables("postgresql://gray:graycadeau@localhost/stackoverflow_lite")