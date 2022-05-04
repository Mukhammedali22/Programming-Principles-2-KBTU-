#!/usr/bin/python

import psycopg2
from config import config


def change_username(first_name, last_name, phone):
    """ update user name based on the user phone """
    sql = f""" UPDATE phonebook
                SET first_name = '{first_name}',
                last_name = '{last_name}'
                WHERE phone = '{phone}'
                """
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
        cur.execute(sql, (first_name, last_name, phone))
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

def change_phone(first_name, last_name, phone):
    """ update phone based on the username """
    sql = f""" UPDATE phonebook
                SET phone = '{phone}'
                WHERE first_name = '{first_name}'
                and last_name = '{last_name}'
            """
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
        cur.execute(sql, (first_name, last_name, phone))
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

def delete_user(first_name, last_name):
    """ delete data based on the username"""
    sql = f""" DELETE FROM phonebook
                WHERE first_name = '{first_name}' and last_name = '{last_name}'
            """
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
        cur.execute(sql, (first_name, last_name))
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

mode = input("What do you want to change?:\nusername or phone or delete data: ")

if mode == "delete data":
    first_name, last_name = input("Write your full name to delete data: ").split()
    delete_user(first_name, last_name)
    print(f"The user {first_name} {last_name} is succesfully deleted!")
elif mode == "phone":
    first_name, last_name = input("Write your full name to change phone: ").split()
    phone = input("Enter your new phone: ") 
    change_phone(first_name, last_name, phone)
    print("You are succesfully changed your phone!")
elif mode == "username":
    phone = input("Enter your phone to change name: ")
    first_name, last_name = input("Write your new full name: ").split() 
    change_username(first_name, last_name, phone)
    print("You are succesfully changed your username!")