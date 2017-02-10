import sqlite3
import sys

#initialize database

db_conn = sqlite3.connect("dojo.db")
print ("Database Successfully Created")

db_conn.close()
print ("Database closed")