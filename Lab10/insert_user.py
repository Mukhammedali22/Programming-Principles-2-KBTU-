#!/usr/bin/python

import psycopg2
from config import config


def insert_user(user_info_list):
    """ insert a new user into the phonebook table """
    sql = """INSERT INTO phonebook(first_name, last_name, phone) VALUES(%s, %s, %s) RETURNING user_id;"""
    conn = None
    user_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, user_info_list)
        # get the generated id back
        user_id = cur.fetchone()[0]
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
    return user_id


if __name__ == '__main__':
    user_info = input("Enter your full name and your phone:\n").split()
    insert_user(user_info)