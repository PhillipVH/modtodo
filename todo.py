#!/bin/python

import sqlite3
import datetime
import sys
import subprocess

DB_PREFIX = '/home/phillip/Projects/Personal/modtodo/'

def connect_to_database(database_name='todo.db'):
    conn = sqlite3.connect(DB_PREFIX + database_name)
    return conn

def commit_and_disconnect():
    conn.commit()
    conn.close()

def add_todo(text: str):
    # Connect to the database and fetch a cursor
    conn = connect_to_database()
    c = conn.cursor()

    # Execute the insertion operation and commit
    c.execute('''INSERT INTO todos VALUES (?, ?)''', (datetime.datetime.now(), text))

    conn.commit()

if __name__ == '__main__':
    # Ensure that the user entered the todo in the correct format
    if len(sys.argv) != 2:
        print("Usage: todo.py \"Your todo here\"")
        raise SystemExit()

    # Grab a connection
    conn = connect_to_database()
    
    # Add the todo
    add_todo(sys.argv[1])

    # Commit and close the database
    commit_and_disconnect()
