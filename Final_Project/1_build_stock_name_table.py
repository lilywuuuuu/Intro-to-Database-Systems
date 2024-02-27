"""
This file fetch the list of listed companies in taiwan from the twstock, and upload them into the table on RDS.
"""

import psycopg2
from psycopg2.extras import RealDictCursor
import json
import twstock
from twstock import Stock

host = "database-1.c4alhaecwxce.us-east-1.rds.amazonaws.com"
username = "postgres"
password = "postgres"
database = "dbhw1"

conn = psycopg2.connect(
    host = host,
    database = database,
    user = username,
    password = password
)

cur = conn.cursor(cursor_factory = RealDictCursor)
stock_list = twstock.twse

for i, (key, value) in enumerate(stock_list.items()):

    if (stock_list[key].market == '上市'):
            command = ' insert into list values(\'' + stock_list[key].type + '\', \'' + stock_list[key].code + '\', \'' + stock_list[key].name + '\', \'' + stock_list[key].ISIN + '\', \'' + stock_list[key].start + '\', \'' + stock_list[key].market + '\', \'' + stock_list[key].group + '\', \'' + stock_list[key].CFI + '\');' 
            cur.execute(command)

conn.commit()
