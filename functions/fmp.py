

'''
FMP Provides the following endpoints that can be useful:
Stock Ranking by Analyst
Analyst Estimates going back years
Analyst recommendations by month
-Income Statement, Balance Sheet, Cash Flow Statement
Price Target changes
Upgrades downgrades
Earnings and Earnings Surprises
Senate and House Trading
Historical performance on each market sector
Sector and Industry PE ratio
Biggest gainers and losers
Insider Trades Summary
Treasury Rates
Economic Indicators

'''
import os
from dotenv import load_dotenv
load_dotenv()

## Classifier Table
import os
from dotenv import load_dotenv
load_dotenv()

## Classifier Table
FMP_API_KEY = os.getenv('FMP_API_KEY')

import pandas as pd
from datetime import datetime, timedelta

import requests
import requests_cache
requests_cache.install_cache('fmp_cache')
from requests.adapters import HTTPAdapter, Retry
s = requests.Session()
retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504 ])
s.mount('http://', HTTPAdapter(max_retries=retries))


def download_income_statement(ticker):
    url = 'https://financialmodelingprep.com/api/v3/income-statement/'+ticker+'?period=quarterly&apikey=' + FMP_API_KEY

    response = s.get(url).json()
    income_statement = pd.DataFrame.from_records(response)
    return income_statement

def download_balance_sheet(ticker):
    url = 'https://financialmodelingprep.com/api/v3/balance-sheet-statement/'+ticker+'?period=quarterly&apikey=' + FMP_API_KEY

    response = s.get(url).json()
    balance_sheet = pd.DataFrame.from_records(response)
    return balance_sheet

def download_cashflow_statement(ticker):
    url = 'https://financialmodelingprep.com/api/v3/cash-flow-statement/'+ticker+'?period=quarterly&apikey=' + FMP_API_KEY
    response = s.get(url).json()
    cashflow_statement = pd.DataFrame.from_records(response)
    return cashflow_statement

def download_fmp_ratings(ticker):
    url = 'https://financialmodelingprep.com/api/v3/historical-rating/'+ticker+'?Limit=10&apikey=' + FMP_API_KEY
    response = s.get(url).json()
    ratings = pd.DataFrame.from_records(response)
    return ratings

def download_enterprise_value(ticker):
    url = 'https://financialmodelingprep.com/api/v3/enterprise-values/'+ticker+'?period=quarter&apikey=' + FMP_API_KEY
    response = s.get(url).json()
    ratings = pd.DataFrame.from_records(response)
    return ratings

def download_earnings_results(ticker):
    url = 'https://financialmodelingprep.com/api/v3/historical/earning_calendar/'+ticker+'?Limit=10&apikey=' + FMP_API_KEY
    response = s.get(url).json()
    earnings_results = pd.DataFrame.from_records(response)
    return earnings_results

def key_metrics(ticker):
    url = 'https://financialmodelingprep.com/api/v3/key-metrics-ttm/'+ticker+'?apikey=' + FMP_API_KEY
    response = s.get(url).json()
    earnings_results = pd.DataFrame.from_records(response)
    return earnings_results

def key_ratios(ticker):
    url = 'https://financialmodelingprep.com/api/v3/ratios-ttm/'+ticker+'?apikey=' + FMP_API_KEY
    response = s.get(url).json()
    earnings_results = pd.DataFrame.from_records(response)
    return earnings_results

def financial_growth(ticker):
    url = 'https://financialmodelingprep.com/api/v3/financial-growth/'+ticker+'?apikey=' + FMP_API_KEY
    response = s.get(url).json()
    earnings_results = pd.DataFrame.from_records(response)
    return earnings_results

def download_earnings_calendar(from_date, to_date):
    if type(from_date) is datetime:
        from_date = datetime.strftime(from_date, '%Y-%m-%d')
    if type(to_date) is datetime:
        to_date = datetime.strftime(to_date, '%Y-%m-%d')
    url = 'https://financialmodelingprep.com/api/v3/earning_calendar?from='+from_date+'&to='+to_date+'&apikey=' + FMP_API_KEY
    response = s.get(url).json()
    earnings_results = pd.DataFrame.from_records(response)
    return earnings_results

def download_analyst_estimates(ticker):
    url = 'https://financialmodelingprep.com/api/v3/analyst-estimates/'+ticker+'?Limit=10&apikey=' + FMP_API_KEY
    response = s.get(url).json()
    earnings_results = pd.DataFrame.from_records(response)
    return earnings_results

def download_analyst_stock_recommendations(ticker):
    url = 'https://financialmodelingprep.com/api/v3/analyst-stock-recommendations/'+ticker+'?&apikey=' + FMP_API_KEY
    response = s.get(url).json()
    df = pd.DataFrame.from_records(response)
    df['analystRatingsbuy_1month_prior'] = df['analystRatingsbuy'].shift(-1)
    df['analystRatingsHold_1month_prior'] = df['analystRatingsHold'].shift(-1)
    df['analystRatingsSell_1month_prior'] = df['analystRatingsSell'].shift(-1)
    df['analystRatingsStrongBuy_1month_prior'] = df['analystRatingsStrongBuy'].shift(-1)
    df['analystRatingsStrongSell_1month_prior'] = df['analystRatingsStrongSell'].shift(-1)

    df['analystRatingsbuy_2month_prior'] = df['analystRatingsbuy'].shift(-2)
    df['analystRatingsHold_2month_prior'] = df['analystRatingsHold'].shift(-2)
    df['analystRatingsSell_2month_prior'] = df['analystRatingsSell'].shift(-2)
    df['analystRatingsStrongBuy_2month_prior'] = df['analystRatingsStrongBuy'].shift(-2)
    df['analystRatingsStrongSell_2month_prior'] = df['analystRatingsStrongSell'].shift(-2)

    df['analystRatingsbuy_3month_prior'] = df['analystRatingsbuy'].shift(-3)
    df['analystRatingsHold_3month_prior'] = df['analystRatingsHold'].shift(-3)
    df['analystRatingsSell_3month_prior'] = df['analystRatingsSell'].shift(-3)
    df['analystRatingsStrongBuy_3month_prior'] = df['analystRatingsStrongBuy'].shift(-3)
    df['analystRatingsStrongSell_3month_prior'] = df['analystRatingsStrongSell'].shift(-3)

    df['analystRatingsbuy_4month_prior'] = df['analystRatingsbuy'].shift(-4)
    df['analystRatingsHold_4month_prior'] = df['analystRatingsHold'].shift(-4)
    df['analystRatingsSell_4month_prior'] = df['analystRatingsSell'].shift(-4)
    df['analystRatingsStrongBuy_4month_prior'] = df['analystRatingsStrongBuy'].shift(-4)
    df['analystRatingsStrongSell_4month_prior'] = df['analystRatingsStrongSell'].shift(-4)

    df['analyst_buy_percent'] = (df['analystRatingsbuy'] + df['analystRatingsStrongBuy']) / (df['analystRatingsbuy'] + df['analystRatingsHold'] + df['analystRatingsSell'] + df['analystRatingsStrongSell'] + df['analystRatingsStrongBuy'])
    df['analyst_hold_percent'] = (df['analystRatingsHold']) / (df['analystRatingsbuy'] + df['analystRatingsHold'] + df['analystRatingsSell'] + df['analystRatingsStrongSell'] + df['analystRatingsStrongBuy'])
    df['analyst_sell_percent'] = (df['analystRatingsSell'] + df['analystRatingsStrongBuy']) / (df['analystRatingsbuy'] + df['analystRatingsHold'] + df['analystRatingsSell'] + df['analystRatingsStrongSell'] + df['analystRatingsStrongBuy'])

    df['analyst_buy_percent_1month_prior'] = (df['analystRatingsbuy_1month_prior'] + df['analystRatingsStrongBuy_1month_prior']) / (df['analystRatingsbuy_1month_prior'] + df['analystRatingsHold_1month_prior'] + df['analystRatingsSell_1month_prior'] + df['analystRatingsStrongSell_1month_prior'] + df['analystRatingsStrongBuy_1month_prior'])
    df['analyst_hold_percent_1month_prior'] = (df['analystRatingsHold_1month_prior']) / (df['analystRatingsbuy_1month_prior'] + df['analystRatingsHold_1month_prior'] + df['analystRatingsSell_1month_prior'] + df['analystRatingsStrongSell_1month_prior'] + df['analystRatingsStrongBuy_1month_prior'])
    df['analyst_sell_percent_1month_prior'] = (df['analystRatingsSell_1month_prior'] + df['analystRatingsStrongBuy_1month_prior']) / (df['analystRatingsbuy_1month_prior'] + df['analystRatingsHold_1month_prior'] + df['analystRatingsSell_1month_prior'] + df['analystRatingsStrongSell_1month_prior'] + df['analystRatingsStrongBuy_1month_prior'])

    df['analyst_buy_percent_2month_prior'] = (df['analystRatingsbuy_2month_prior'] + df['analystRatingsStrongBuy_2month_prior']) / (df['analystRatingsbuy_2month_prior'] + df['analystRatingsHold_2month_prior'] + df['analystRatingsSell_2month_prior'] + df['analystRatingsStrongSell_2month_prior'] + df['analystRatingsStrongBuy_2month_prior'])
    df['analyst_hold_percent_2month_prior'] = (df['analystRatingsHold_2month_prior']) / (df['analystRatingsbuy_2month_prior'] + df['analystRatingsHold_2month_prior'] + df['analystRatingsSell_2month_prior'] + df['analystRatingsStrongSell_2month_prior'] + df['analystRatingsStrongBuy_2month_prior'])
    df['analyst_sell_percent_2month_prior'] = (df['analystRatingsSell_2month_prior'] + df['analystRatingsStrongBuy_2month_prior']) / (df['analystRatingsbuy_2month_prior'] + df['analystRatingsHold_2month_prior'] + df['analystRatingsSell_2month_prior'] + df['analystRatingsStrongSell_2month_prior'] + df['analystRatingsStrongBuy_2month_prior'])

    df['analyst_buy_percent_3month_prior'] = (df['analystRatingsbuy_3month_prior'] + df['analystRatingsStrongBuy_3month_prior']) / (df['analystRatingsbuy_3month_prior'] + df['analystRatingsHold_3month_prior'] + df['analystRatingsSell_3month_prior'] + df['analystRatingsStrongSell_3month_prior'] + df['analystRatingsStrongBuy_3month_prior'])
    df['analyst_hold_percent_3month_prior'] = (df['analystRatingsHold_3month_prior']) / (df['analystRatingsbuy_3month_prior'] + df['analystRatingsHold_3month_prior'] + df['analystRatingsSell_3month_prior'] + df['analystRatingsStrongSell_3month_prior'] + df['analystRatingsStrongBuy_3month_prior'])
    df['analyst_sell_percent_3month_prior'] = (df['analystRatingsSell_3month_prior'] + df['analystRatingsStrongBuy_3month_prior']) / (df['analystRatingsbuy_3month_prior'] + df['analystRatingsHold_3month_prior'] + df['analystRatingsSell_3month_prior'] + df['analystRatingsStrongSell_3month_prior'] + df['analystRatingsStrongBuy_3month_prior'])

    df['analyst_buy_percent_4month_prior'] = (df['analystRatingsbuy_4month_prior'] + df['analystRatingsStrongBuy_4month_prior']) / (df['analystRatingsbuy_4month_prior'] + df['analystRatingsHold_4month_prior'] + df['analystRatingsSell_4month_prior'] + df['analystRatingsStrongSell_4month_prior'] + df['analystRatingsStrongBuy_4month_prior'])
    df['analyst_hold_percent_4month_prior'] = (df['analystRatingsHold_4month_prior']) / (df['analystRatingsbuy_4month_prior'] + df['analystRatingsHold_4month_prior'] + df['analystRatingsSell_4month_prior'] + df['analystRatingsStrongSell_4month_prior'] + df['analystRatingsStrongBuy_4month_prior'])
    df['analyst_sell_percent_4month_prior'] = (df['analystRatingsSell_4month_prior'] + df['analystRatingsStrongBuy_4month_prior']) / (df['analystRatingsbuy_4month_prior'] + df['analystRatingsHold_4month_prior'] + df['analystRatingsSell_4month_prior'] + df['analystRatingsStrongSell_4month_prior'] + df['analystRatingsStrongBuy_4month_prior'])

    df['analyst_buy_change_1month'] = df['analyst_buy_percent'] / df['analyst_buy_percent_1month_prior'] - 1
    df['analyst_hold_change_1month'] = df['analyst_hold_percent'] / df['analyst_hold_percent_1month_prior'] - 1
    df['analyst_sell_change_1month'] = df['analyst_sell_percent'] / df['analyst_sell_percent_1month_prior'] - 1

    df['analyst_buy_change_2month'] = df['analyst_buy_percent'] / df['analyst_buy_percent_2month_prior'] - 1
    df['analyst_hold_change_2month'] = df['analyst_hold_percent'] / df['analyst_hold_percent_2month_prior'] - 1
    df['analyst_sell_change_2month'] = df['analyst_sell_percent'] / df['analyst_sell_percent_2month_prior'] - 1

    df['analyst_buy_change_3month'] = df['analyst_buy_percent'] / df['analyst_buy_percent_3month_prior'] - 1
    df['analyst_hold_change_3month'] = df['analyst_hold_percent'] / df['analyst_hold_percent_3month_prior'] - 1
    df['analyst_sell_change_3month'] = df['analyst_sell_percent'] / df['analyst_sell_percent_3month_prior'] - 1

    df['analyst_buy_change_4month'] = df['analyst_buy_percent'] / df['analyst_buy_percent_4month_prior'] - 1
    df['analyst_hold_change_4month'] = df['analyst_hold_percent'] / df['analyst_hold_percent_4month_prior'] - 1
    df['analyst_sell_change_4month'] = df['analyst_sell_percent'] / df['analyst_sell_percent_4month_prior'] - 1

    df = df.drop(columns=[
        'analystRatingsbuy',
        'analystRatingsHold',
        'analystRatingsSell',
        'analystRatingsStrongSell',
        'analystRatingsStrongBuy',
        'analyst_buy_percent_1month_prior',
        'analyst_hold_percent_1month_prior',
        'analyst_sell_percent_1month_prior',
        'analyst_buy_percent_2month_prior',
        'analyst_hold_percent_2month_prior',
        'analyst_sell_percent_2month_prior',
        'analyst_buy_percent_3month_prior',
        'analyst_hold_percent_3month_prior',
        'analyst_sell_percent_3month_prior',
        'analyst_buy_percent_4month_prior',
        'analyst_hold_percent_4month_prior',
        'analyst_sell_percent_4month_prior',
        'analystRatingsbuy_1month_prior',
        'analystRatingsHold_1month_prior',
        'analystRatingsSell_1month_prior',
        'analystRatingsStrongBuy_1month_prior',
        'analystRatingsStrongSell_1month_prior',
        'analystRatingsbuy_2month_prior',
        'analystRatingsHold_2month_prior',
        'analystRatingsSell_2month_prior',
        'analystRatingsStrongBuy_2month_prior',
        'analystRatingsStrongSell_2month_prior',
        'analystRatingsbuy_3month_prior',
        'analystRatingsHold_3month_prior',
        'analystRatingsSell_3month_prior',
        'analystRatingsStrongBuy_3month_prior',
        'analystRatingsStrongSell_3month_prior',
        'analystRatingsbuy_4month_prior',
        'analystRatingsHold_4month_prior',
        'analystRatingsSell_4month_prior',
        'analystRatingsStrongBuy_4month_prior',
        'analystRatingsStrongSell_4month_prior',
        ])


    return df

def download_insider_trades(ticker):
    for n in range(100):
        url = 'https://financialmodelingprep.com/api/v4/insider-trading?symbol='+ticker+'&page='+str(n)+'&apikey=' + FMP_API_KEY
        response = s.get(url).json()
        insider_trades = pd.DataFrame.from_records(response)
        if n == 0: combined_insider_trades = insider_trades.copy()
        else: combined_insider_trades = pd.concat([combined_insider_trades, insider_trades])
    combined_insider_trades = combined_insider_trades.reset_index(drop=True)
    return combined_insider_trades

def download_insider_trade_stats(ticker):
    url = 'https://financialmodelingprep.com/api/v4/insider-roaster-statistic?symbol='+ticker+'&apikey=' + FMP_API_KEY
    response = s.get(url).json()
    insider_trades = pd.DataFrame.from_records(response)
    quarters = insider_trades['quarter'].to_list()
    years = insider_trades['year'].to_list()
    date = []
    for quarter, year in zip(quarters, years):
        if quarter == 1: 
            month = '03'
            day = '31'
        elif quarter == 2:
            month = '06'
            day = '30'
        elif quarter == 3:
            month = '09'
            day = '30'
        elif quarter == 4:
            month = '12'
            day = '31'
        date.append(f'{str(year)}-{month}-{day}')
    insider_trades['date'] = date
    insider_trades['buySellDollarRatio'] = insider_trades['totalBought'] / insider_trades['totalSold']
        
    return insider_trades

def download_ratios(ticker):
    url = 'https://financialmodelingprep.com/api/v3/ratios/'+ticker+'?period=quarter&apikey=' + FMP_API_KEY
    response = s.get(url).json()
    earnings_results = pd.DataFrame.from_records(response)
    return earnings_results

def company_profile(ticker):
    url = 'https://financialmodelingprep.com/api/v3/profile/'+ticker+'?&apikey=' + FMP_API_KEY
    response = s.get(url).json()
    earnings_results = pd.DataFrame.from_records(response)
    return earnings_results

def country_risk_premiums():
    url = 'https://financialmodelingprep.com/api/v4/market_risk_premium?apikey=' + FMP_API_KEY
    response = s.get(url).json()
    earnings_results = pd.DataFrame.from_records(response)
    return earnings_results

def treasury_rates():
    url = 'https://financialmodelingprep.com/api/v4/treasury?apikey=' + FMP_API_KEY
    response = s.get(url).json()
    earnings_results = pd.DataFrame.from_records(response)
    return earnings_results

def treasury_rates_incomplete(start, end):
    if type(start) is datetime:
        start = datetime.strftime(start, '%Y-%m-%d')
    if type(end) is datetime:
        end = datetime.strftime(end, '%Y-%m-%d')
    url = f'https://financialmodelingprep.com/api/v4/treasury?from={start}&to={end}&apikey={FMP_API_KEY}'
    response = s.get(url).json()
    try: df = pd.DataFrame.from_records(response)
    except: 
        df = pd.DataFrame(columns=['date', 'Open', 'High', 'Low', 'Close', 'Volume'])
        df = df.set_index('date')
        return 0
    df = df.set_index('date')
    df.index = pd.to_datetime(df.index)
    df = df.sort_values(by=['date'])
    df = df.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'})
    return df

def treasury_rates_complete(tbill_type, start, end):
    # tbill_type: month1  month2  month3  month6  year1  year2  year3  year5  year7  year10  year20  year30
    df = treasury_rates_incomplete(start, end)
    while (df.index[0] - datetime.strptime(start, '%Y-%m-%d')) > timedelta(days=10):
        df2 = treasury_rates_incomplete(start, datetime.strftime(df.index[0], '%Y-%m-%d'))
        df = pd.concat([df2, df])
    tbill_types = ['month1','month2','month3','month6','year1','year2','year3','year5','year7','year10','year20','year30']
    tbill_types.remove(tbill_type)
    df = df.drop(columns=tbill_types)
    return df

def sp500_tickers():
    url = 'https://financialmodelingprep.com/api/v3/sp500_constituent?apikey=' + FMP_API_KEY
    response = s.get(url).json()
    df = pd.DataFrame.from_records(response)
    return df

def sp500_changes():
    # Validated through 1970-01-01
    url = 'https://financialmodelingprep.com/api/v3/historical/sp500_constituent?apikey=' + FMP_API_KEY
    response = s.get(url).json()
    df = pd.DataFrame.from_records(response)
    df = df.fillna('')
    return df

def nasdaq_tickers():
    # Validated through 1970-01-01
    url = 'https://financialmodelingprep.com/api/v3/nasdaq_constituent?apikey=' + FMP_API_KEY
    response = s.get(url).json()
    df = pd.DataFrame.from_records(response)
    return df

def nasdaq_changes():
    url = 'https://financialmodelingprep.com/api/v3/historical/nasdaq_constituent?apikey=' + FMP_API_KEY
    response = s.get(url).json()
    df = pd.DataFrame.from_records(response)
    df = df.fillna('')
    return df

def dow_tickers():
    # Validated through 1995-01-01
    url = 'https://financialmodelingprep.com/api/v3/dowjones_constituent?apikey=' + FMP_API_KEY
    response = s.get(url).json()
    df = pd.DataFrame.from_records(response)
    return df

def dow_changes():
    url = 'https://financialmodelingprep.com/api/v3/historical/dowjones_constituent?apikey=' + FMP_API_KEY
    response = s.get(url).json()
    df = pd.DataFrame.from_records(response)
    df = df.fillna('')
    return df

def peer_list(symbol):
    url = f'https://financialmodelingprep.com/api/v4/stock_peers?symbol={symbol}&apikey={FMP_API_KEY}'
    response = s.get(url).json()
    if len(response) == 0: return None
    #df = pd.DataFrame.from_records(response)
    #df = df.fillna('')
    return response[0]['peersList']

def get_historical_index_tickers(as_of_date, current_index, index_changes):
    ''' Returns the index as of the date provided. 
    Working with FMP's API. 
    as_of_date = Date targeted, either string or datetime. 
    current_index = such as sp500_tickers()
    index_changes = such as sp500_changes()
    '''
    if type(as_of_date) is not datetime:
        as_of_date = datetime.strptime(as_of_date, '%Y-%m-%d')
    
    index_changes['date'] = pd.to_datetime(index_changes['date'])
    current_index = current_index['symbol'].tolist()
    current_index = [s.replace('-', '.') for s in current_index]
        # FMP reports index tickers with classes as - such as BRK-B. 
        # Index changes are reported as . such as BRK.B. 
        # This statement makes the two equal. 
    index_changes = index_changes[index_changes['date'] > as_of_date]

    for index, row in index_changes.iterrows():
        if row['removedTicker'] != '' and row['addedSecurity'] != '':
            try: current_index.remove(row['symbol'])
            except: print(row['symbol']+' is not present in the current index.')
            current_index.append(row['removedTicker'])
        elif row['removedTicker'] != '' and row['addedSecurity'] == '':
            current_index.append(row['removedTicker'])
        elif row['removedTicker'] == '' and row['addedSecurity'] != '':
            current_index.remove(row['symbol'])
    current_index = [ x for x in current_index if "." not in x ] #clears any tickers with .
    return current_index
        

def ohlc_eod(ticker, start, end):
    if type(start) is datetime:
        start = datetime.strftime(start, '%Y-%m-%d')
    if type(end) is datetime:
        end = datetime.strftime(end, '%Y-%m-%d')
    url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?from={start}&to={end}&apikey={FMP_API_KEY}'

    response = s.get(url).json()
    try: df = pd.DataFrame.from_records(response['historical'])
    except: 
        df = pd.DataFrame(columns=['date', 'Open', 'High', 'Low', 'Close', 'Volume'])
        df = df.set_index('date')
        return df
    df = df.drop(columns=['adjClose', 'unadjustedVolume', 'change', 'changePercent', 'vwap', 'label', 'changeOverTime'])
    df = df.set_index('date')
    df.index = pd.to_datetime(df.index)
    df = df.sort_values(by=['date'])
    df = df.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'})
    return df

def ohlc_intraday(ticker, start, end, frequency):
    # Frequency options: 1min, 5min, 15min, 30min, 1hour, 4hour
    if type(start) is datetime:
        start = datetime.strftime(start, '%Y-%m-%d')
    if type(end) is datetime:
        end = datetime.strftime(end, '%Y-%m-%d')
    url = f'https://financialmodelingprep.com/api/v3/historical-chart/{frequency}/{ticker}?from={start}&to={end}&apikey={FMP_API_KEY}'
    response = s.get(url).json()
    try: df = pd.DataFrame.from_records(response)
    except: 
        df = pd.DataFrame(columns=['date', 'Open', 'High', 'Low', 'Close', 'Volume'])
        df = df.set_index('date')
        return 0
    df = df.set_index('date')
    df.index = pd.to_datetime(df.index)
    df = df.sort_values(by=['date'])
    df = df.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'})
    return df


def complete_ohlc_intraday(ticker, start, end, frequency):
    df = ohlc_intraday('SPY', start, end, frequency)
    while (df.index[0] - datetime.strptime(start, '%Y-%m-%d')) > timedelta(days=10):
        print(df.index[0] - datetime.strptime(start, '%Y-%m-%d'))
        df2 = ohlc_intraday(ticker, start, datetime.strftime(df.index[0], '%Y-%m-%d'), frequency)
        df = pd.concat([df2, df])
    return df

def current_price(ticker):
    url = 'https://financialmodelingprep.com/api/v3/stock/full/real-time-price/'+ticker+'?apikey=' + FMP_API_KEY

    response = s.get(url).json()
    order_quote = response[0]
    try: current_price = (order_quote['bidPrice'] + order_quote['askPrice']) / 2
    except: current_price = order_quote['fmpLast'] # Necessary if Bid/Ask prices do not exist. 
    return current_price

def company_profile(ticker):
    url = 'https://financialmodelingprep.com/api/v3/profile/'+ticker+'?&apikey=' + FMP_API_KEY
    response = s.get(url).json()
    earnings_results = pd.DataFrame.from_records(response)
    return earnings_results