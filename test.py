import pybithumb

#get tickers
tickers = pybithumb.get_tickers()
# print(tickers)

#get price
price = pybithumb.get_current_price("BTC")
#print(price)

#거래소 거래 정보
detail = pybithumb.get_market_detail("BTC")
print(detail)