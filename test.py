import requests
import pandas as pd
import time
import json
import threading
import numpy as np
from func import get_symbol_data
from func import symbol_list
from func import get_nyc_time
from func import loop_single_symbol
from func import loop_single_symbol
from matplotlib import pyplot as plt
from func import mysql_insert_new

length = len(symbol_list())
data = symbol_list()
data_frame_array = []
df = pd.DataFrame() 
for j in range(length): 
    u = data[j]
    h = get_symbol_data(u)
    if h:
        df_of_single_symbol = loop_single_symbol(u)
        du = df_of_single_symbol
        df = pd.concat([df, du], axis=0).reset_index(drop=True)
        # mysql_insert_new(delayedPrice,symbol,get_nyc_time())
    
df.to_excel("output.xlsx")


       





