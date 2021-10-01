import psycopg2
from psycopg2.extras import DictCursor, register_uuid
from dotenv import load_dotenv
from os import environ
load_dotenv()


class Postgres():
    def __init__(self):
        # instantiate a connection to database
        # cursor is a particular "pointer". Think of it as a buffer getting data from db
        # the default cursor is tuple, which means data comes back as tuple. For example ("caffe", "starbuck", etc.)
        # DictCursor is a type of cursor that allow accessing data by column name, like result["name"]; result["brand"]
        print("New db connection!")
        self.conn = psycopg2.connect(
            f"host={environ.get('POSTGRES_HOST')} dbname={environ.get('POSTGRES_DB')} user={environ.get('POSTGRES_USER')} password={environ.get('POSTGRES_PASSWORD')}", cursor_factory=DictCursor)

    def query(self, sql, values={}):  # may throw DbException
        register_uuid()

        # with is a pythonic feature called "context manager"
        # conn.cursor() opens a new connection
        with self.conn:
            with self.conn.cursor() as curs:
                # curs.execute takes 2 param, the SQL & the values to be interpolated.
                curs.execute(sql, values)
                # execute does not return data, therefore we need to "fetch" the data from cursor.
                rows = curs.fetchall()
                # there are 2 types of fetch: fetchone & fetchall. A typical query returns many rows, so we use fetchall.
                return rows
        # when done with a db operation, it's always necessary to close the connection, similar to closing a file
        # however, using context manager feature, it's automatically closed

    def update(self, sql, values={}):  # may throw DbException

        register_uuid()
        with self.conn:
            with self.conn.cursor() as curs:
                curs.execute(sql, values)
                # our insertion query only return 1 row, so we use fetchone.
                row = curs.fetchone()
                return row

    def close(self):
        print("Closing db connection")
        self.conn.close()
