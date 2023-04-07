##########import json
import random
import urllib.request
import time

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server requests
N = 500

def getDataPoint(quote):
    """ Produce all of the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        return
    return price_a / price_b

# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    while True:
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        # calculate and output the price ratio
        if 'STOCKA' in prices and 'STOCKB' in prices:
            price_a = prices['STOCKA']
            price_b = prices['STOCKB']
            ratio = getRatio(price_a, price_b)
            print("Ratio of price_a and price_b: ", ratio)

        # wait for some time before making the next request
        time.sleep(5)
