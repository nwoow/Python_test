import requests
import pandas as pd
import time
import json
import datetime, pytz
import pymysql
def get_symbol_data(parameter_list):
    u = parameter_list   
    p = "https://api.iextrading.com/1.0/stock/"+ u +"/delayed-quote"
    response = requests.get(p)
    if response:
        response.content.decode("utf-8")
        js = response.json()
        return js
    else:
        return False

def get_nyc_time():
    now = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
    current_hour = now.hour
    current_minute = now.minute
    time = ""+str(current_hour)+":"+str(current_hour)
    return time

def symbol_list():
    data = [
    "AAPL",
    # "BAC",
    # "AMZN",
    # "T",
    # "GOOG",
    # "MO",
    # "DAL",
    # "AA",
    # # "AXP",
    # # "DD",
    # "BABA",
    # "ABT",
    # "UA",
    # "AMAT",
    # "AMGN",
    # "AAL",
    # "AIG",
    # "ALL",
    # "ADBE",
    # "GOOGL",
    # "ACN",
    # "ABBV",
    # "MT",
    # "LLY",
    # "AGN",
    # "APA",
    # "ADP",
    # "APC",
    # "AKAM",
    # "NLY",
    # "ABX",
    # "ATVI",
    # "ADSK",
    # "ADM",
    # # "BMH.AX",
    # "WBA",
    # "ARNA",
    # "LUV",
    # "ACAD",
    # "PANW",
    # "AMD",
    # "AET",
    # "AEP",
    # "ALXN",
    # # "CLMS",
    # "AVGO",
    # "EA",
    # "DB",
    # # "RAI",
    ]
    return data

def loop_single_symbol(p1):
    i = 0
    delayedPrice = []
    symbol = [] 
    while i<5 :
        print(p1)
        h = get_symbol_data(p1)
        delayedPrice.append(h['delayedPrice']) 
        symbol.append(h['symbol'])
        i+=1
    df = pd.DataFrame([], columns = []) 
    df["delayedPrice"] = delayedPrice
    df["symbol"] = symbol
    df["time"] = get_nyc_time()
    mysql_insert_new(delayedPrice,symbol,get_nyc_time())
    return df 
    time.sleep(4)

def mysql_insert(p1,p2,p3,p4,p5,p6,p7):
    # Open database connection
    db = pymysql.connect("localhost","root","DxyAY1JLS9c$q@WKoLG!8rs","pytest" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO Stock(symbol,delayedPrice, high, low, delayedSize,delayedPriceTime,processedTime)
    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    values = (p1,p2,p3,p4,p5,p6,p7)
    
    try:
    # Execute the SQL command
    #    cursor.execute(sql)
        cursor.execute(sql, values)
        # Commit your changes in the database
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    # cursor.execute(sql)
    db.close()

def mysql_insert_new(p1,p2,p3):
    # Open database connection
    db = pymysql.connect("localhost","root","DxyAY1JLS9c$q@WKoLG!8rs","pytest" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    print(p1)

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO Stock1(delayedPrice, symbol, time)
    VALUES (%s, %s, %s)"""
    values = (p1,p2,p3)
    
    try:
    # Execute the SQL command
    #    cursor.execute(sql)
        cursor.execute(sql, values)
        # Commit your changes in the database
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    # cursor.execute(sql)
    db.close()   
