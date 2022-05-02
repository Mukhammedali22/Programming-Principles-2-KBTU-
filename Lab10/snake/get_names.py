#!/usr/bin/python

import psycopg2
from config import config


def getNames():
    """ get a user names from the users table """
    sql = "SELECT user_name FROM users"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the get names statement
        cur.execute(sql)
        colnames = cur.fetchall()
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    #print(user_id)
    return colnames
