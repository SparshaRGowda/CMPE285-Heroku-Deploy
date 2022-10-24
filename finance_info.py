# Name: Sparsha Ramakrishna
# SJSU ID: 015274571

import requests
import datetime


url = "https://yh-finance.p.rapidapi.com/stock/v2/get-statistics"

print("Enter a symbol:")
input_symbol = input()

try:
    querystring = {"symbol":input_symbol,"region":"US"}

    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': "2e7d47075emshd540ab6cc5624cbp1df59cjsn99d9332c4356"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response = response.json()
    stock_time = response['price']['regularMarketTime']
    stock_datetime = datetime.datetime.fromtimestamp(stock_time)
    print(stock_datetime)

    company = response['price']['longName']
    print(company)

    stock_price = response['price']['regularMarketPrice']['fmt']
    print(stock_price)

    price_change = response['price']['regularMarketChange']['fmt']
    print(price_change)

    percentage_change = response['price']['regularMarketChangePercent']['fmt']
    print(percentage_change)
except requests.exceptions.ConnectTimeout:
    print("Timedout Error")
except requests.exceptions.HTTPError:
    print("HTTP Error")
except requests.exceptions.ConnectionError:
    print("Connection Error")
except:
    print("Invalid symbol Error")