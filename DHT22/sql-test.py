#!/usr/bin/python
# -*- coding: utf-8 -*-
# version.py – Fetch and display the MySQL database server version.
# import the MySQLdb and sys modules
import MySQLdb
import sys
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host="localhost", user = "pi", passwd = "dadopi", db = "weather_station")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()
# execute the SQL query using execute() method.
cursor.execute ('SELECT VERSION()')
# fetch a single row using fetchone() method.
row = cursor.fetchone ()
# print the row[0]
# (Python starts the first row in an array with the number zero – instead of one)
print 'Server version:', row[0]
# close the cursor object
cursor.close ()
# close the connection
connection.close ()
# exit the program
sys.exit()
