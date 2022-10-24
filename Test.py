# Name: Sparsha Ramakrishna
# SJSU ID: 015274571

# Following formulae has been used in the program:
# Proceeds = Final Share Price * Allotment
# Purchase Price = initialSharePrice * allotment
# Raw Profit = (Final Share Price - Initial Share Price) * Allotment - Buy Commission - Sell Commission
# Tax = Raw Profit * Tax Rate%
# ToBreakEvenPrice = (Buy Commission + Sell Commission) / Allotment +  Initial Share Price
# String of floating number with only two decimals

import requests

url = "https://yh-finance.p.rapidapi.com/stock/v2/get-statistics"

print("\n"+ "Enter five stock symbols:" + "\n")

symbol = []
for i in range(5):
    ip = input()
    symbol.append(ip)

for ipSymbol in symbol:

    try:
        querystring = {"symbol": ipSymbol, "region": "US"}

        headers = {
            'x-rapidapi-host': 'yh-finance.p.rapidapi.com',
            'x-rapidapi-key': 'cfd3441bf8msh026386777cfb2bfp199fdfjsn178eb4670d35'
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        response = response.json()
        company_name = response['price']['longName']

        print("Company Name: " + company_name + "\n")
        print("Allotment:" + "\n")

        allotment = int(input())

        sharePrice = response['price']['regularMarketPrice']['fmt']

        finalSharePrice = float(sharePrice)

        print("Final Share Price:" + "\n" + finalSharePrice)

        print("Sell Commission:" + "\n")
        sell_commission = int(input())

        print("Initial Share Price:" + "\n")
        init_share_prc = int(input())

        print("Buy Commission" + "\n")
        buy_commission = int(input())

        print("Capital Gain Tax Rate(%):")
        cap_gain_tax_rate = int(input())

        print("PROFIT REPORT:")

        print("Proceeds")
        proceeds = float(allotment*finalSharePrice)

        form_proceeds = "{:.2f}".format(proceeds)
        print("$", form_proceeds + "\n")

        print('Cost')
        capital_gain = (allotment*finalSharePrice)-(allotment *
                                                    init_share_prc) - buy_commission - sell_commission
        cap_gain_tax = (cap_gain_tax_rate/100)*capital_gain
        cost = allotment*init_share_prc+buy_commission+sell_commission+cap_gain_tax

        form_cost = "{:.2f}".format(cost)
        print("$", form_cost + "\n")

        print("Cost DETAILS:")

        print("Total Purchase Price")
        total_purchase_price = float(allotment*init_share_prc)
        form_total_purchase_price = "{:.2f}".format(total_purchase_price)

        print(allotment, 'X$', init_share_prc, '=', form_total_purchase_price)

        print("Buy Commission :", "{:.2f}".format(buy_commission))

        print("Sell Commission :", "{:.2f}".format(sell_commission))

        print("Tax on Capital Gain :", cap_gain_tax_rate,
              '% of', "{:.2f}".format(cap_gain_tax_rate) + "\n")

        print("Net Profit in Dollars")
        net_profit = proceeds - cost

        net_profit_formatted = "{:.2f}".format(net_profit)
        print("$", net_profit_formatted + "\n")

        print("Return on Investment in %")
        return_on_investment = (net_profit/cost)*100
        form_return_on_investment = "{:.2f}".format(return_on_investment)
        print(form_return_on_investment, "%" + "\n")
        print("Final share price must be")

        break_even_price = ((init_share_prc*allotment) + buy_commission
                            + sell_commission)/100
        form_break_even_price = "{:.2f}".format(break_even_price)
        print("$", form_break_even_price)

        print("-------------------------")

    except requests.exceptions.ConnectTimeout:
        print("Time Out Error.")
    except requests.exceptions.HTTPError:
        print("HTTP Error.")
    except requests.exceptions.ConnectionError:
        print("Connection Error.")
    except:
        print("Invalid symbol Error.")
