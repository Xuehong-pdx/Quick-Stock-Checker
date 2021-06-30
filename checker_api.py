import yfinance as yf
import pandas as pd
import time

def check_symbol(symbol):
    ticker = yf.Ticker(symbol)
    try:
        ticker.info['symbol']
        return True
    except (KeyError):
        print(f'{symbol.upper()} is not a valid symbol.')
        
def get_info(ticker):
    t = yf.Ticker(ticker)
    # df = t.history('max')
    # df = df.reset_index()
    close_price = round(t.info['previousClose'],2)
    open_price = round(t.info['regularMarketOpen'],2)
    high = round(t.info['regularMarketDayHigh'],2)
    low = round(t.info['regularMarketDayLow'],2)
    return ticker,close_price,open_price,high,low 
  
def get_stocks(symbols):
    
    if ',' in symbols:
        tickers = list(symbols.split(','))
        stock_values = []
        for ticker in tickers:
            ticker = ticker.upper().strip()
            if check_symbol(ticker) == True:
                ticker,close_price,open_price,high,low = get_info(ticker)
                stock_values.append([ticker, close_price,open_price,high,low])
        return stock_values

    else:
        ticker = symbols.upper().strip()
        if check_symbol(ticker) == True:
            ticker,close_price,open_price,high,low = get_info(symbols)
            return [[ticker, close_price,open_price,high,low]]

if __name__ == '__main__':
    # start_time = time.time()
    stocks = input('Enter your stocks and separate by comma: ')
    print()
    output = get_stocks(stocks)
    if output is None:
        pass
    else:
        df = pd.DataFrame(output, columns = ['symbol', 'Previous close', 'Current open', 'high', 'low'])
        print('Please see the info on your stocks below.', '\n')
        print(df)
    # print("--- %s seconds ---" % (time.time() - start_time))