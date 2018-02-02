import psycopg2
from getpass import getpass

def init_db(user, passw):
    try:
        conn = psycopg2.connect(database="postgres", user=user, password=passw)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute("DROP DATABASE IF EXISTS FauxFlightDB")
        cur.execute("CREATE DATABASE FauxFlightDB")
        cur.close()
        conn.close()
    except psycopg2.OperationalError as err:
        print("{}".format(err))
    except psycopg2.InternalError as err:
        print("{}".format(err))

def setup_schema(user, passw):
    try:
        conn = psycopg2.connect(database="FauxFlightDB", user=user, password=passw)
        cur = conn.cursor()
        cur.close()
        conn.close()
    except psycopg2.OperationalError as err:
        print("{}".format(err))
    except psycopg2.InternalError as err:
        print("{}".format(err))

def read_schema():
    schemaname = "ffdbschema.sql"


if __name__ == "__main__":
    user = input("Postgres user: ")
    password = getpass()
    init_db(user, password)

