import pandas as pd
import yfinance as yf
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
df = yf.download('MSFT',start="2002-01-01",end='2025-07-13')
print("The dataset for the MSFT stocks is :")
print(df)
print("The first 25 rows of the dataset are :")
print(df.head(25))
print("Lets add the Simple Moving Average for the set of 25 days !")
df['Simple Moving Average'] = df['Close'].rolling(window=25).mean()
print(df)
sns.lineplot(x='Date',y='Close',data=df.droplevel(1,axis=1),label="Close")
sns.lineplot(x='Date',y='Simple Moving Average',data=df.droplevel(1,axis=1),label="S.M.A.")
plt.xlabel("Date")
plt.ylabel("Average/Close")
plt.show()
