from functions import comps, utils

tickers = utils.read_tickers_from_file('ticker_lists/dx_lifescitools_tickers.txt')
df = comps.build_comp_database(tickers)
df.to_csv('data_files/dx_lifescitools_database.csv')

tickers = utils.read_tickers_from_file('ticker_lists/medtech_tickers.txt')
df = comps.build_comp_database(tickers)
df.to_csv('data_files/medtech_database.csv')

