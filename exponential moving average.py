import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
df = yf.download('AAPL',start='2025-01-01',end='2025-07-01')
print(df)
print("The first 50 rows of the dataset are:")
print (df.head(50))
print("re-indexed dataset is:")
df=df.reindex()
print(df)
df['SMA']=df['Close'].rolling(window=25).mean()
df['EMA']=df['Close'].ewm(span=25,adjust=False).mean()
print(df)
sns.lineplot(x='Date',y='Close',data=df.droplevel(1,axis=1),label='Close')
sns.lineplot(x='Date',y='SMA',data=df.droplevel(1,axis=1),label='SMA')
sns.lineplot(x='Date',y='EMA',data=df.droplevel(1,axis=1),label='EMA')
plt.xlabel('Date')
plt.ylabel('Data')
plt.show()