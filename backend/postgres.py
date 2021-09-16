import psycopg2
from psycopg2.extras import DictCursor

class Postgres():
    def __init__(self):
        # instantiate a connection to database
        # cursor is a particular "pointer". Think of it as a buffer getting data from db
        # the default cursor is tuple, which means data comes back as tuple. For example ("caffe", "starbuck", etc.)
        # DictCursor is a type of cursor that allow accessing data by column name, like result["name"]; result["brand"]
        self.conn = psycopg2.connect("host=localhost dbname=testing_db user=postgres password=postgres", cursor_factory=DictCursor)
    
    def query(self, sql, values = {}): # may throw DbException
        # with is a pythonic feature called "context manager"
        # conn.cursor() opens a new connection
        with self.conn.cursor() as curs:
            curs.execute(sql, values) # curs.execute takes 2 param, the SQL & the values to be interpolated.
            rows = curs.fetchall() # execute does not return data, therefore we need to "fetch" the data from cursor.
            # there are 2 types of fetch: fetchone & fetchall. A typical query returns many rows, so we use fetchall.
            return rows
        # when done with a db operation, it's always necessary to close the connection, similar to closing a file
        # however, using context manager feature, it's automatically closed
        
    def update(self, sql, values = {}): # may throw DbException
        with self.conn.cursor() as curs:
            curs.execute(sql, values)
            row = curs.fetchone() # our insertion query only return 1 row, so we use fetchone.
            return row