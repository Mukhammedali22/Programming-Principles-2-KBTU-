#!/usr/bin/python

import psycopg2
from config import config


def delete_data(table):
    """ deleting data in table """
    sql_delete = f"""DELETE FROM {table}"""
    sql_restart  = f"""TRUNCATE TABLE {table} RESTART IDENTITY"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the DELETE and RESTART statement
        cur.execute(sql_delete)
        cur.execute(sql_restart)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    table_name = input("Enter table what you want to delete: ")
    delete_data(table_name)
    print(f"DATA in the {table_name} deleted succesfully!")