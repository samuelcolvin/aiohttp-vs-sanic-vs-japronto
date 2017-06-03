import random
import string

import asyncpg


PG_DSN_NO_DB = 'postgres://postgres:waffle@localhost:5432'
DB_NAME = 'foobar'
PG_DSN = PG_DSN_NO_DB + '/' + DB_NAME

DB_EXISTS = 'SELECT EXISTS (SELECT datname FROM pg_catalog.pg_database WHERE datname=$1)'

CREATE_TABLES = """\
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(63) NOT NULL
);
"""


async def setup_db(loop):
    conn = await asyncpg.connect(dsn=PG_DSN_NO_DB)
    try:
        db_exists = await conn.fetchval(DB_EXISTS, DB_NAME)
        if not db_exists:
            await conn.execute('CREATE DATABASE {}'.format(DB_NAME))
    finally:
        await conn.close()

    conn = await asyncpg.connect(dsn=PG_DSN)
    try:
        await conn.execute(CREATE_TABLES)
        names = [
            [''.join(random.choices(string.ascii_letters, k=random.randrange(10, 50)))]
            for _ in range(1000)
        ]

        await conn.executemany('INSERT INTO users (name) VALUES ($1);', names)
    finally:
        await conn.close()
    return await asyncpg.create_pool(PG_DSN, loop=loop, max_size=100)
