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

# cur = conn.cursor(cursor_factory = RealDictCursor)
# cur.execute("select * from ")
# results = cur.fetchall()
# json_result = json.dumps(results)
# print(json_result)


