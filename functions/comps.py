

tickers = ['AAPL', 'MSFT', 'CDNA', 'ME']

from functions import fmp
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
from datetime import datetime
import numpy as np
import time

def build_comp_database(tickers):

    for index, ticker in enumerate(tickers):
        print(ticker)

        df = fmp.company_profile(ticker)
        if len(df) == 0: break

        ev = fmp.download_enterprise_value(ticker).iloc[0]

        df['sharesout'] = ev['numberOfShares']
        df['cash'] = ev['minusCashAndCashEquivalents']
        df['debt'] = ev['addTotalDebt']
        df['enterprisevalue'] = ev['enterpriseValue']

        key_metrics = fmp.key_metrics(ticker)

        df = pd.concat([df, key_metrics], axis=1)

        key_ratios = fmp.key_ratios(ticker)
        df = pd.concat([df, key_ratios], axis=1)

        growth = fmp.financial_growth(ticker).loc[0]
        df = pd.concat([df, growth.to_frame().T], axis=1)

        estimates = fmp.download_analyst_estimates(ticker)

        try:
            estimates['date'] = pd.to_datetime(estimates['date'])
            current_date = pd.to_datetime(datetime.now().date())
            estimates = estimates[estimates['date'] > current_date]
            df['revenue+1'] = estimates.iloc[-1]['estimatedRevenueAvg']
            df['revenue+2'] = estimates.iloc[-2]['estimatedRevenueAvg']
            df['revenue+3'] = estimates.iloc[-3]['estimatedRevenueAvg']

            df['ebitda+1'] = estimates.iloc[-1]['estimatedEbitdaAvg']
            df['ebitda+2'] = estimates.iloc[-2]['estimatedEbitdaAvg']
            df['ebitda+3'] = estimates.iloc[-3]['estimatedEbitdaAvg']

            df['eps+1'] = estimates.iloc[-1]['estimatedEpsAvg']
            df['eps+2'] = estimates.iloc[-2]['estimatedEpsAvg']
            df['eps+3'] = estimates.iloc[-3]['estimatedEpsAvg']
        except:
            df['revenue+1'] = np.nan
            df['revenue+2'] = np.nan
            df['revenue+3'] = np.nan

            df['ebitda+1'] = np.nan
            df['ebitda+2'] = np.nan
            df['ebitda+3'] = np.nan

            df['eps+1'] = np.nan
            df['eps+2'] = np.nan
            df['eps+3'] = np.nan

        if index == 0: combined_df = df
        else: combined_df = pd.concat([combined_df, df])
        time.sleep(1)

    return combined_df



