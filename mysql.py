#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","DxyAY1JLS9c$q@WKoLG!8rs","pytest" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()
