import yfinance as yf
import pandas as pd

def get_stock(stock):
    stock=stock.upper()
    t = yf.Ticker(stock)
    df = t.history('max')
    df = df.reset_index()
    close_price = round(t.info['previousClose'],2)
    open_price = round(t.info['regularMarketOpen'],2)
    high = round(t.info['regularMarketDayHigh'],2)
    low = round(t.info['regularMarketDayLow'],2)
     
    return stock, close_price,open_price,high,low

def get_stocks():
    with open('stocks_list.txt', 'rt') as f:
        stocks = f.read()
        
    if ',' in stocks:
        stocks = list(stocks.split(','))
        stocks = [x.strip() for x in stocks]
        stock_values = []
        for stock in stocks:
            stock, close_price,open_price,high,low = get_stock(stock)
            stock_values.append([stock, close_price,open_price,high,low])
        return stock_values
    else:
       close_price,open_price,high,low = get_stock(stocks)
       return [stocks, close_price,open_price,high,low]

if __name__ == '__main__':
    output = get_stocks()
    df = pd.DataFrame(output, columns = ['symbol', 'Previous close', 'Current open', 'high', 'low'])
    print(df)