import csv
import psycopg2
from psycopg2.extras import RealDictCursor
import json
import twstock
from twstock import Stock

# Assume that you have a dictionary that looks like this:
# my_dict = {'1101': StockCodeInfo(type='股票', code='1101', name='台泥', ISIN='TW0001101004', start='1962/02/09', market='上市', group='水泥工業', CFI='ESVUFR')}

my_dict = twstock.twse

# Open a file for writing
with open('list.csv', 'w', newline='') as f:
  # Create a CSV writer object
  writer = csv.writer(f)
  
  # Write the headers
  writer.writerow(['type', 'code', 'name', 'ISIN', 'start', 'market', 'group', 'CFI'])
  
  # Write the rows of data
  for code, stock_info in my_dict.items():
    writer.writerow([ stock_info.type, code, stock_info.name, stock_info.ISIN, stock_info.start, stock_info.market, stock_info.group, stock_info.CFI])
