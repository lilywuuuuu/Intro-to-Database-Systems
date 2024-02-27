import csv
import psycopg2
from psycopg2.extras import RealDictCursor
import json
import twstock
from twstock import Stock
import numpy 

stock_id = '2330'

stock = twstock.Stock(stock_id)

data = stock.fetch(2022,12)
# print("2022/12/open")

for i in data:
    print(i.open)