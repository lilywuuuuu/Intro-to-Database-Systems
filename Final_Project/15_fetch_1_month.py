import csv
import psycopg2
from psycopg2.extras import RealDictCursor
import json
import twstock
from twstock import Stock
import time 
import random

# Assume that you have a dictionary that looks like this:
# my_dict = {'1101': StockCodeInfo(type='股票', code='1101', name='台泥', ISIN='TW0001101004', start='1962/02/09', market='上市', group='水泥工業', CFI='ESVUFR')}

# my_dict = twstock.twse

delay_choices = [1.93, 1.8, 1.9, 2.1, 1.7, 1.73]  #延遲的秒數


with open('/Users/chinlinwu/Documents/6_Introductions_to_Database_Systems/Final_Project/10_stock_price.csv', 'w', newline='') as f:
  # Create a CSV writer object
  writer = csv.writer(f)


  for i in ['2330']:
    stock = twstock.Stock(i)
    for j in range(1,13):
      fetch = stock.fetch(2022,j)
      for row in fetch:
        print(row)
        writer.writerow([row.date, row.capacity, row.turnover, row.open, row.high, row.low, row.close, row.change, row.transaction])
        
      delay = random.choice(delay_choices)  #隨機選取秒數
      time.sleep(2*delay)  #延遲

# # Open a file for writing
# with open('list.csv', 'w', newline='') as f:
#   # Create a CSV writer object
#   writer = csv.writer(f)
  
#   # Write the headers
#   writer.writerow(['type', 'code', 'name', 'ISIN', 'start', 'market', 'group', 'CFI'])
  
#   # Write the rows of data
#   for code, stock_info in my_dict.items():
#     writer.writerow([ stock_info.type, code, stock_info.name, stock_info.ISIN, stock_info.start, stock_info.market, stock_info.group, stock_info.CFI])
