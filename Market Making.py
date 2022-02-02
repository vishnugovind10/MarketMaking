import pandas as pd
import json
import datetime

books = ['2020-07-'+str(x)+".json" for x in range(18,31,1)]

trades = pd.read_csv("trades.csv")

orders = pd.read_json("binance_iotabtc_orderbooks_json/2020-07-17.json")
orders["asks"] = orders["asks"].apply(lambda x: json.loads(x))
orders["bids"] = orders["bids"].apply(lambda x: json.loads(x))

for y in books:
    orders1 = pd.read_json("binance_iotabtc_orderbooks_json/"+y)
    orders1["asks"] = orders1["asks"].apply(lambda x: json.loads(x))
    orders1["bids"] = orders1["bids"].apply(lambda x: json.loads(x))
    orders = orders.append(orders1, ignore_index = True)

fees = 0.075
flag = 0

col0 = []
col1 = []
col2 = []

for index, row_t in trades.iterrows():
    if index%1000 == 0:
        positions = pd.DataFrame(list(zip(col0, col1, col2)), columns=['Bid', 'Ask', 'Price'])
        positions.to_csv('positions.csv')
        
    timestamp2 = row_t['timestamp']
    lastprice_t = row_t['price']
    for index, row_o in orders.iterrows():
        timestamp1 = row_o['lastUpdated']
        if datetime.datetime.strptime(timestamp1, '%Y-%m-%d %H:%M:%S.%f') > datetime.datetime.strptime(timestamp2, '%Y-%m-%d %H:%M:%S.%f'):
            break
        highestbid = max(row_o["bids"],key = lambda x : x[0])[0] 
        lowestask = min(row_o["asks"],key = lambda x : x[0])[0]
        fv = (highestbid + lowestask)/2
        spread = lowestask - highestbid
        spreadpercent = spread/lowestask * 100
        if spreadpercent <= fees:
            continue
        
        bid = max(lastprice_t-spread/2,fv-spread/2)
        ask = min(lastprice_t+spread/2,fv+spread/2)
        if (flag == 0 or flag == 2) and bid == lastprice_t:
            col0.append(1)
            col1.append(0)
            col2.append(lastprice_t)
            flag = -1
        elif (flag == 0 or flag == 1) and ask == lastprice_t:
            col0.append(0)
            col1.append(1)
            col2.append(lastprice_t)
            flag = -1
        if flag == -1:
            if sum(col0) - sum(col1) > 10:
                flag = 1
            elif sum(col1) - sum(col0) > 10:
                flag = 2
            else:
                flag = 0

positions = pd.DataFrame(list(zip(col0, col1, col2)), columns=['Bid', 'Ask', 'Price'])
positions.to_csv('positions.csv')

