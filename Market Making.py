import pandas as pd
import json
import datetime
import requests

# Define your API endpoints and keys for Binance and Kraken
binance_api_url = 'https://api.binance.com/api/v3/'
kraken_api_url = 'https://api.kraken.com/0/public/'

# Fetch initial account balance from the exchange (Replace with actual API call)
initial_balance_response = requests.get(binance_api_url + 'account', headers={'X-MBX-APIKEY': 'your-api-key'})
initial_balance_data = initial_balance_response.json()
initial_balance = float(initial_balance_data['balances'][0]['free'])

# Fetch trade data using API (Replace with actual API calls)
trades_response = requests.get(binance_api_url + 'trades', params={'symbol': 'IOTABTC', 'limit': 1000})
trades_data = trades_response.json()

# Create a DataFrame to store trade data
trades = pd.DataFrame(trades_data)

# Fetch order book data using API (Replace with actual API calls)
order_book_response = requests.get(binance_api_url + 'depth', params={'symbol': 'IOTABTC'})
order_book_data = order_book_response.json()

# Create a DataFrame to store order book data
orders = pd.DataFrame(order_book_data)
orders['asks'] = orders['asks'].apply(lambda x: x[0])
orders['bids'] = orders['bids'].apply(lambda x: x[0])

# Define the exchange fee rate for trading
exchange_fee_rate = 0.0025

# Initialize variables
flag = 0
max_loss_percentage = 5  # Example: 5% as maximum loss percentage
current_balance = initial_balance

# Lists to store trading positions and P&L
col0 = []  # Bid positions
col1 = []  # Ask positions
col2 = []  # Trade prices
col3 = []  # P&L column

# Iterate through trade data
for index, row_t in trades.iterrows():
    if index % 1000 == 0:
        # Create a DataFrame to store positions and P&L data
        positions = pd.DataFrame(list(zip(col0, col1, col2, col3)), columns=['Bid', 'Ask', 'Price', 'P&L'])
        positions.to_csv('positions.csv', index=False)

    # Extract timestamp and last price from trade data
    timestamp2 = row_t['time']
    lastprice_t = float(row_t['price'])
    
    # Iterate through order book data
    for index, row_o in orders.iterrows():
        timestamp1 = row_o['lastUpdateId']
        if timestamp1 > timestamp2:
            break
        highestbid = row_o["bids"]
        lowestask = row_o["asks"]
        
        # Calculate fair value and spread
        fv = (highestbid + lowestask) / 2
        spread = lowestask - highestbid
        spreadpercent = (spread / lowestask) * 100
        
        # Skip trade if spread is below transaction costs
        if spreadpercent <= exchange_fee_rate:
            continue
        
        # Calculate bid and ask prices
        bid = max(lastprice_t - spread / 2, fv - spread / 2)
        ask = min(lastprice_t + spread / 2, fv + spread / 2)
        
        # Perform buy or sell based on bid/ask
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
        
        # Calculate P&L dynamically, update current balance, and check stop condition
        if flag == -1:
            pnl = (sum(col0) - sum(col1)) * (lastprice_t * exchange_fee_rate)
            col3.append(pnl)
            
            current_balance = initial_balance + sum(col3)  # Update current balance
            
            # Calculate current P&L as a percentage
            current_pnl_percentage = ((current_balance - initial_balance) / initial_balance) * 100
            
            # Check stop condition
            if current_pnl_percentage <= -max_loss_percentage:
                print("Stop trading due to excessive loss.")
                positions = pd.DataFrame(list(zip(col0, col1, col2, col3)), columns=['Bid', 'Ask', 'Price', 'P&L'])
                positions.to_csv('positions.csv', index=False)
                exit()  # Exit the algorithm
                
            if sum(col0) - sum(col1) > 10:
                flag = 1
            elif sum(col1) - sum(col0) > 10:
                flag = 2
            else:
                flag = 0

# Create a final DataFrame with positions and P&L data
positions = pd.DataFrame(list(zip(col0, col1, col2, col3)), columns=['Bid', 'Ask', 'Price', 'P&L'])
positions.to_csv('positions.csv', index=False)
