import requests

url = "https://yh-finance.p.rapidapi.com/stock/v2/get-statistics"

print("Enter five ticker symbols:" + "\n")

symbol = []
for i in range(5):
    ip = input()
    symbol.append(ip)

for inputSymbol in symbol:

    try:
        querystring = {"symbol": inputSymbol, "region": "US"}

        headers = {
            'x-rapidapi-host': "yh-finance.p.rapidapi.com",
            'x-rapidapi-key': "2e7d47075emshd540ab6cc5624cbp1df59cjsn99d9332c4356"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()
        company = response['price']['longName']
        print("Company Name: " + company)
        print()
        print('Allotment:')
        allotment = int(input())
        print()
        fin_share_prc1 = response['price']['regularMarketPrice']['fmt']
        fin_share_prc = float(fin_share_prc1)
        print('Final Share Price:')
        print(fin_share_prc)
        print()
        print('Sell Commission:')
        sell_commission = int(input())
        print()
        print('Initial Share Price:')
        init_share_prc = int(input())
        print()
        print('Buy Commission')
        buy_commission = int(input())
        print()
        print('Capital Gain Tax Rate(%):')
        cap_gain_tax_rate = int(input())
        print()
        print('PROFIT REPORT:')
        print('Proceeds')
        proceeds = float(allotment*fin_share_prc)
        form_proceeds = "{:.2f}".format(proceeds)
        print("$",form_proceeds)
        print()
        print('Cost')
        capital_gain =(allotment*fin_share_prc)-(allotment*init_share_prc)- buy_commission - sell_commission
        cap_gain_tax = (cap_gain_tax_rate/100)*capital_gain
        cost = allotment*init_share_prc+buy_commission+sell_commission+cap_gain_tax
        form_cost = "{:.2f}".format(cost)
        print("$",form_cost)
        print()
        print('Cost DETAILS:')
        print('Total Purchase Price')
        total_purchase_price = float(allotment*init_share_prc)
        form_total_purchase_price ="{:.2f}".format(total_purchase_price)
        print(allotment, 'X$',init_share_prc,'=',form_total_purchase_price)
        print('Buy Commission :', "{:.2f}".format(buy_commission))
        print('Sell Commission :', "{:.2f}".format(sell_commission))
        print('Tax on Capital Gain :', cap_gain_tax_rate, '% of', "{:.2f}".format(cap_gain_tax_rate))
        print()
        print('Net Profit in Dollars')
        net_profit = proceeds - cost
        net_profit_formatted = "{:.2f}".format(net_profit)
        print("$",net_profit_formatted)
        print()
        print('Return on Investment in %')
        return_on_investment = (net_profit/cost)*100
        form_return_on_investment = "{:.2f}".format(return_on_investment)
        print(form_return_on_investment,"%")
        print()
        print('To break even, you should have a final share price of')
        break_even_price = ((init_share_prc*allotment) + buy_commission
        + sell_commission)/100
        form_break_even_price = "{:.2f}".format(break_even_price)
        print("$",form_break_even_price)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    except requests.exceptions.ConnectTimeout:
        print("The request timedout.")
    except requests.exceptions.HTTPError:
        print("There was an HTTP error.")
    except requests.exceptions.ConnectionError:
        print("Connection Error.")
    except:
        print("Invalid symbol.")