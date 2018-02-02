"""
Sér um gagnagrunnsaðgerðir
"""
import psycopg2
from getpass import getpass

def init_db(user, passw):
    """
    Eyðir gamla DB og býr til nýtt. 
    Kallar á fall sem setur upp schemað
    """
    try:
        conn = psycopg2.connect(database="postgres", user=user, password=passw)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute("DROP DATABASE IF EXISTS fauxflightdb")
        cur.execute("CREATE DATABASE fauxflightdb")
        cur.close()
        conn.close()

        setup_schema(user, passw)
    except psycopg2.OperationalError as err:
        print("{}".format(err))
        raise Exception()
    except psycopg2.InternalError as err:
        print("{}".format(err))
        raise Exception()

def setup_schema(user, passw):
    """
    Setur upp schemað í gagnagrunninum
    """
    try:
        conn = psycopg2.connect(database="fauxflightdb", user=user, password=passw)
        cur = conn.cursor()
        cur.execute(read_schema())
        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.OperationalError as err:
        print("{}".format(err))
        raise Exception()
    except psycopg2.InternalError as err:
        print("{}".format(err))
        raise Exception()

def read_schema():
    """
    Les inn skipanir úr ffdbschema.sql
    til þess að setja upp gagnagrunn
    """
    schema = None
    with open("./files/ffdbschema.sql") as f:
        schema = f.read()
    return schema
    

def connect(user, passw):
    """
    Skilar tengingu við fauxflightdb
    """
    return psycopg2.connect(database="fauxflightdb", user=user, password=passw)



if __name__ == "__main__":
    user = input("Postgres user: ")
    password = getpass()
    init_db(user, password)

