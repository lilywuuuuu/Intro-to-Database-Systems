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

def lambda_handler(event, context):

    twstock.__update_codes()
    stock = Stock('2330')                             # 擷取台積電股價
    ma_p = stock.moving_average(stock.price, 5)       # 計算五日均價
    ma_c = stock.moving_average(stock.capacity, 5)    # 計算五日均量
    ma_p_cont = stock.continuous(ma_p)                # 計算五日均價持續天數
    ma_br = stock.ma_bias_ratio(5, 10)                # 計算五日、十日乖離值

    # print(ma_p)
    # print(ma_c)
    # print(ma_p_cont)
    # print(ma_br)

    cur = conn.cursor(cursor_factory = RealDictCursor)
    cur.execute("insert into list values('股票', 1110, '台泥', 'TW0001101004', '1962/02/09', '上市', '水泥工業', 'ESVUFR');")
    results = cur.fetchall()
    print(results)
    # json_result = json.dumps(results)
    # print(json_result)
    # return json_result
    # return {
    #     'statusCode' : 200,
    #     'body' : json.dumps('Hello world')
    # }



lambda_handler('a','a')
