import requests
import pandas as pd
import time
import json
import datetime, pytz
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
    "BAC",
    "AMZN",
    "T",
    "GOOG",
    "MO",
    "DAL",
    "AA",
    # "AXP",
    # "DD",
    "BABA",
    "ABT",
    "UA",
    "AMAT",
    "AMGN",
    "AAL",
    "AIG",
    "ALL",
    "ADBE",
    "GOOGL",
    "ACN",
    "ABBV",
    "MT",
    "LLY",
    "AGN",
    "APA",
    "ADP",
    "APC",
    "AKAM",
    "NLY",
    "ABX",
    "ATVI",
    "ADSK",
    "ADM",
    # "BMH.AX",
    "WBA",
    "ARNA",
    "LUV",
    "ACAD",
    "PANW",
    "AMD",
    "AET",
    "AEP",
    "ALXN",
    # "CLMS",
    "AVGO",
    "EA",
    "DB",
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
    return df 
    time.sleep(4) 
