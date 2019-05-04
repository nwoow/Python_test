#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","DxyAY1JLS9c$q@WKoLG!8rs","pytest" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
# sql = "INSERT INTO STOCK(symbol, \
#    delayedPrice, high, low, delayedSize,delayedPriceTime,processedTime) \
#    VALUES ('%s', '%s', '%s', '%s', '%s','%s','%s' )" % \
#    ('Mac', 'Mohan', 20, 'M', 2000)
add_stock = ("INSERT INTO STOCK "
               "(symbol,delayedPrice, high, low, delayedSize,delayedPriceTime,processedTime) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
 data_employee = ('Geert', 123, 123,3232, 23232,3434,34343)              
try:
   # Execute the SQL command
    cursor.execute(add_stock, data_employee)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

