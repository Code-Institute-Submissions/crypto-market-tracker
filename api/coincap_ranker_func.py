import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

local_currency = 'EUR'
local_symbol = '€'

API_KEY = "ae55d981-0a3f-4fab-82d8-bfd27701bda3"
headers = {"X-CMC_PRO_API_KEY": API_KEY}

BASE_URL = 'https://pro-api.coinmarketcap.com'

# Menu for Ranking Function
print()
print("CoinMarketCap Explorer Menu")
print()
print("[1]- Top 100 sorted by market cap")
print("[2]- Top 100 sorted by 24hr percent change")
print("[3]- Top 100 sorted by 24hr trading volume")
print("[0]- Exit")

choice = input("What information would you like to view? (1-3)")

sort = ""

if choice == "1":
    sort = "market_cap"
elif choice == "2":
    sort = "percent_change_24h"
elif choice == "3":
    sort = "volume_24h"
elif choice == "0":
    exit(0)
else:
    print("Invalid choice")
    exit(1)


quote_url = BASE_URL + "/v1/cryptocurrency/listings/latest?convert=" + local_currency + "&sort=" + sort

request = requests.get(quote_url, headers=headers)
results = request.json()

# Api Data
data = results["data"]

#Table Varible
table = PrettyTable(["Asset", "Price", "Market_Cap", "Volume", "1hr", "24hr" ,"7d", "30d"])

print()

for currency in data:
    name = currency["name"]
    symbol = currency["symbol"]
    # Data for Table
    quote = currency["quote"][local_currency]
    market_cap = quote["market_cap"]

    percent_change_1hr = quote["percent_change_1h"]
    percent_change_24hr = quote["percent_change_24h"]
    percent_change_7d = quote["percent_change_7d"]
    percent_change_30d = quote["percent_change_30d"]

    price = quote["price"]
    volume = quote["volume_24h"]
    # Formatting data    
    if percent_change_1hr is not None:
        percent_change_1hr = round(percent_change_1hr, 2)
        
    if percent_change_24hr is not None:
        percent_change_24hr = round(percent_change_24hr, 2)

    if percent_change_7d is not None:
        percent_change_7d = round(percent_change_7d, 2)

    if percent_change_30d is not None:
        percent_change_30d = round(percent_change_30d, 2)            

    if volume is not None:
        volume_string = "{:,}".format(round(price, 2))

    if market_cap is not None:
        market_cap_string = "{:,}".format(round(price, 2))

    price_string = "{:,}".format(round(price, 2)) 

    table.add_row([name + " (" + symbol + ')',
                   local_symbol + price_string,
                   local_symbol + market_cap_string,
                   local_symbol + volume_string,
                   str(percent_change_1hr),
                   str(percent_change_24hr),
                   str(percent_change_7d),
                   str(percent_change_30d),]) 
print()
print(table)
print()           