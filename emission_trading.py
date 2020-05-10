import random


# find which company has extra emission allowances to sell due to European Union Emissions Trading Scheme.

def buy_or_sell(allocation, emissions):
    global seller
    number_seller = 0
    result = allocation - emissions
    if result > 0:  # if Allocation – Emissions > 0: the company is a seller
        seller = True
        number_seller = number_seller + 1
        print('The company can sell allocations')
    else:
        seller = False
        print('The company cannot sell allocations')
    return seller


# A seller sells allowances if its minimum price <= market price
market_price = 20


def trading(market_price, c_price):
    if seller == True and c_price <= market_price:
        trade = True
        print('Trading is possible...')
    else:
        print('Trading is not possible...')

#buy_or_sell(400, 250)
#trading(market_price, 10)
