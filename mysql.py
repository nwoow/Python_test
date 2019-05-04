#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","DxyAY1JLS9c$q@WKoLG!8rs","pytest" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE Stock (
   symbol  CHAR(20) NOT NULL,
   delayedPrice  FLOAT,
   high FLOAT,  
   low FLOAT,
   delayedSize INT,
   delayedPriceTime INT,
   processedTime INT )"""

cursor.execute(sql)

# disconnect from server
db.close()
