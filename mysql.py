#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","DxyAY1JLS9c$q@WKoLG!8rs","pytest" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO STOCK(symbol,delayedPrice, high, low, delayedSize,delayedPriceTime,processedTime)
   VALUES ('Mac', 34, 20, 3434, 2000,34343,4343)"""
# try:
#    # Execute the SQL command
#    cursor.execute(sql)
#    # Commit your changes in the database
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()

# disconnect from server
cursor.execute(sql)
db.close()

