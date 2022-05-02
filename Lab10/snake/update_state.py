#!/usr/bin/python

import psycopg2
from config import config


def update_game_state(game_state):
    """ update user score based on the user name """
    sql = """ UPDATE users
                SET game_pause = %s
                SET game_end = %s
                SET game_win = %s
                SET level = %s
                WHERE user_name = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, game_state)
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows
