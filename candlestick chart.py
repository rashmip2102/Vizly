
import pandas as pd

import yfinance as yf
import mplfinance as mpf
df = yf.download('AMZN',start='2020-01-01',end='2025-07-31')
print(df)
#mpf.plot(df['2020-01-01':'2020-06-01'], type='candle', volume=True)
df = df.xs('AMZN', axis=1, level=1)

# Now you can plot
mpf.plot(df['2020-01-01':'2020-06-01'], type='candle', volume=True)
