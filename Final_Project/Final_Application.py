import matplotlib.pyplot as plt
import numpy as np
import time
import psycopg2
from psycopg2.extras import RealDictCursor
import json
import twstock
from twstock import Stock
from datetime import datetime

def stock(day, company_code):
    if day == 7:
        plus = 0
        thickness = 3
        name = "Stock of 7 Days"
    elif day == 30:
        plus = 20
        thickness = 2
        name = "Stock of 30 Days"
    elif day == 230:
        plus = 220
        thickness = 1
        name = "Stock of an Year"
    elif day == 1205:
        plus = 1195
        thickness = 1
        name = "Stcok of 5 Years"
    
    stock = twstock.Stock(company_code)
    len = 31+plus
    Close = [0]*(len)
    Open = [0]*(len)
    High = [0]*(len)
    Low = [0]*(len)
    Date = [0]*(len)

    for i in range(31): 
        Close[len-31+i] = stock.close[i]
        Open[len-31+i] = stock.open[i]
        High[len-31+i] = stock.high[i]
        Low[len-31+i] = stock.low[i]
        Date[len-31+i] = stock.date[i].strftime("%Y-%m-%d")
    oldest_day = Date[len-31]

    cur.execute("select _date, _close, _open, _high, _low \
                from stock_prices where _code = '" + company_code + "' \
                and _date < '" + oldest_day + "' \
                order by _date desc limit " + str(plus))
    results = cur.fetchall()
    count = plus
    for row in results:
        count -= 1
        Date[count] = row["_date"]
        Close[count] = row["_close"]
        Open[count] = row["_open"]
        High[count] = row["_high"]
        Low[count] = row["_low"]

    vol = [0] * (len-1)
    pos = 0
    neg = 0
    for i in range(len-1):
        if Close[i] == 0:
            continue
        vol[i] = (Close[i+1]-Close[i])/Close[i]
        if vol[i] >= 0:
            pos = pos + vol[i]
        else:
            neg = neg - vol[i]

    rsi = pos/(pos + neg)*100
    print("RSI = " + str(rsi) + "\n")

    fig = plt.figure()
    if(day!=1205):
        for i in range(len-day, len):
            x = [str(Date[i]), str(Date[i])]
            y1 = [High[i], Low[i]]
            y2 = [Open[i], Close[i]]
            if Open[i] > Close[i]:
                plt.plot(x, y1, linestyle='-', linewidth=thickness, color='g', alpha=0.5)
                plt.plot(x, y2, linestyle='-', linewidth=thickness+2, color='g', alpha=0.5)
            else: 
                plt.plot(x, y1, linestyle='-', linewidth=thickness, color='r', alpha=0.5)
                plt.plot(x, y2, linestyle='-', linewidth=thickness+2, color='r', alpha=0.5)

    day1 = 5
    day2 = 20

    len1 = len-day1+1 
    len2 = len-day2+1 
    SMA1 = [0] * len1
    SMA2 = [0] * len2
    SMA_day = [0] * day
    SMA_date1 = [0] * len1
    SMA_date2 = [0] * len2
    SMA_date_day = [0] * day

    for i in range(len1):
        sum = 0
        for j in range(day1):
            sum += Close[i+j]
        SMA1[i] = sum/day1
    for i in range(len1):
        SMA_date1[i] = Date[i+day1-1]
    for i in range(day):
        SMA_day[i] = SMA1[len1-day+i]
        SMA_date_day[i] = str(SMA_date1[len1-day+i])
    plt.plot(SMA_date_day, SMA_day, linestyle='-', linewidth=thickness+1, color='deepskyblue', label="5 Day Moving Average")

    for i in range(len2):
        sum = 0
        for j in range(day2):
            sum += Close[i+j]
        SMA2[i] = sum/day2
    for i in range(len2):
        SMA_date2[i] = Date[i+day2-1]
    for i in range(day):
        SMA_day[i] = SMA2[len2-day+i]
        SMA_date_day[i] = str(SMA_date2[len2-day+i])
    plt.plot(SMA_date_day, SMA_day, linestyle='-', linewidth=thickness+1, color='orange', label="20 Day Moving Average")

    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False) # labels along the bottom edge are off

    fig.canvas.set_window_title(name)
    plt.legend()
    plt.show()
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

done = False

print("\nWelcome to Dinu Stock Analyzer!\n")
#time.sleep(1)

while(not done):
    print("If you want to check out the listed companies in Taiwan, press '1'. \nYou can find the company codes there.\n")
    #time.sleep(3)
    print("If you want to see a specific company's stock analysis, press '2'. \nYou can use the found code to see the analysis here.\n")
    #time.sleep(3)
    print("If you want to quit, press '3'.\n")
    print(": ", end="")
    answer1 = input()
    print("\nYou pressed '" + answer1 + "'\n")

    if answer1 == "1":
        print("If you want to see all 970 of them, press '1'. \nIt'll be super long list :)\n")
        #time.sleep(2)
        print("If you want to search a specific industry of companies, press '2'. \nWe'll show you the list.\n")
        #time.sleep(2)
        print("If you want to search a company with a name, press '3'. \nYou must know your stock very well!\n")
        print(": ", end="")
        answer2 = input()
        print("\nYou pressed '" + answer2 + "'\n")

        if answer2 == "1":
            cur.execute("select _code, _name from code_name")
            results = cur.fetchall()
            count = 1
            print("Number\tCode\tName")
            for row in results:
                print(str(count)+ "\t" + row["_code"] + "\t" + row["_name"])
                count += 1
            print("\nAnd that's the whole list!\n")
        
        elif answer2 == "2":
            count = 0
            cur.execute("select distinct _group from list_co")
            results = cur.fetchall()
            for row in results:
                a = row["_group"]
                if(len(a) > 7): print(a, end="\t")
                elif(len(a) < 4): print(a, end="\t\t\t")
                else: print(a, end="\t\t")
                count += 1
                if(count%5 == 0): print("\n")
            print("\n\n")
            count = 0
            print("Type in the group name to see all the specific companies within that group.")
            print(": ", end=" ")
            group_name = input()
            cur.execute("select code_name._name, code_name._code, list_co._group \
                        from list_co, code_name where list_co._group like '%" + group_name + "%' \
                        and code_name._code = list_co._code")
            results = cur.fetchall()
            for row in results:
                count += 1
                print(row["_code"] +  "\t" + row["_name"])
            print("\n")
            if(count == 0): print("You may have entered a wrong name. Try again.\n")

        elif(answer2 == "3"):
            count = 0
            print("Type in the name of the desired company.")
            print(": ", end = "")
            company_name = input()
            cur.execute("select _code, _name from code_name where _name = '" + company_name + "'")
            results = cur.fetchall()
            for row in results:
                count += 1
                print(row["_code"] + "\t" + row["_name"] + "\n")
            if(count == 0): print("You may have entered a wrong name. Try again.\n")

    elif answer1 == "2": 
        print("Type in the code or name of the desired company.")
        print(": ", end="")
        company_input = input()
        if("1100" < company_input < "9999"):
            company_code = company_input
            cur.execute("select _name from code_name where _code = '" + company_code + "'")
            company_name = cur.fetchall()[0]["_name"]
        else:
            company_name = company_input
            cur.execute("select _name, _code from code_name where _name like '%" + company_name + "%'")
            result = cur.fetchall()
            company_code = result[0]["_code"]
            company_name = result[0]["_name"]

        print("Stock right now, press '1'.")
        print("Stock from the past week, press '2'.")
        print("Stock from the past month, press '3'.")
        print("Stock from the past year, press '4'.")
        print("Stock from the past 5 years, press '5'.\n")
        print(": ", end="")
        answer2 = input()
        print("\nYou pressed '" + answer2 + "'\n")

        if(answer2 == "1"):
            stock_curr_info = twstock.realtime.get(company_code)
            print("Company = " + company_name)
            print("Latest trade price = " + stock_curr_info["realtime"]["latest_trade_price"])
            print("Current trade volume = " + stock_curr_info["realtime"]["trade_volume"])
            print("Best bid price = " + str(stock_curr_info["realtime"]["best_bid_price"]))
            print("Best bid volume = " + str(stock_curr_info["realtime"]["best_bid_volume"]))
            print("Best ask price = " + str(stock_curr_info["realtime"]["best_ask_price"]))
            print("Best ask volume = " + str(stock_curr_info["realtime"]["best_ask_volume"]))
            print("Open = " + stock_curr_info["realtime"]["open"])
            print("High = " + stock_curr_info["realtime"]["high"])
            print("Low = " + stock_curr_info["realtime"]["low"])
            #time.sleep(2)

        elif(answer2 == "2"): # a wekk
            stock(7, company_code)
        elif(answer2 == "3"): # a month
            stock(30, company_code)
        elif(answer2 == "4"): # an year
            stock(230, company_code)
        elif(answer2 == "5"): # 5 years
            stock(1205, company_code)
    
    elif answer1 == "3":
        print("Thanks for using Dinu Stock Analyzer, we'll see you next time :)\n")
        done = True