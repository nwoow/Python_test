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
from func import mysql_insert
from matplotlib import pyplot as plt
import datetime
# i = 0
# ind= 0
# df2= pd.DataFrame()
# while i<50 :
#     df1= pd.DataFrame()
#     d = {}
#     length = len(symbol_list())
#     data = symbol_list()
#     symbol = [] 
#     for j in range(length):
#         d[j] = data[j]
#         u = data[j]
#         js = get_symbol_data(u)
#         df = pd.DataFrame(js,index=[ind])
#         df1 = df1.append(df)
#         ind+=1
#     df2 = df2.append(df1)   
#     i+=1
#     print(i)
#     time.sleep(300)
# df2['processedTime']= df2['processedTime'].apply(lambda x:datetime.datetime.fromtimestamp(x/1000.0))
# df2 = df2.set_index(df2.processedTime)
# df2['percTick']= df2['delayedPrice'].pct_change()>=0.02  
# df2['percTick'].replace('False',np.NaN,inplace=True)
# df2.loc[df2['percTick'] == False,'percTick'] = np.nan
# df2.to_excel('dataStock.xlsx')
p1 = "ww"
p2 = 33
p3 = 44
p4 = 44
p5 = 00
p6 = 66
p7 = 99
mysql_insert(p1,p2,p3,p4,p5,p6,p7)
