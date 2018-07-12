#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('todo.db')

c = conn.cursor()

c.execute('''CREATE TABLE todos
             (date text, todo text)''')

conn.commit()

conn.close()
