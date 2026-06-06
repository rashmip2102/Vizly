import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf
import seaborn as sns
df = yf.download('TSLA',start='2024-07-01',end='2025-07-15')
print(df)
df = df.reset_index()
df['SMA'] = df['Close'].rolling(window = 7).mean() #Calculating the Simple Moving Average
print(df)
df['Standard Deviation'] = df['Close'].rolling(window=7).std() #Calcualting the standard deviation of close
print(df)
df['Upper Bound'] = df['SMA'] + (2 * df['Standard Deviation']) #Formula for upper bound of Bollinger's Band
df['Lower Bound'] = df['SMA'] - (2 * df['Standard Deviation']) #Formula for lower bound of Bollinger's Band
print(df)
#sns.lineplot(x='Date',y='SMA',data=df.droplevel(1,axis=1))
#sns.lineplot(x='Date',y='Upper Bound',data= df.droplevel(1,axis=1))
#sns.lineplot(x='Date',y='Lower Bound',data=df.droplevel(1,axis=1))
x=df['Date']
y1=df['Upper Bound']
y2=df['Lower Bound']
#plt.fill_between(x,y1,y2,color='#6ffbff',alpha=0.3)
plt.plot(df['Date'],df['SMA'],label='SMA',color='orange',linestyle='--')
plt.plot(df['Date'],df['Upper Bound'],label='Upper Bound',color='Green')
plt.plot(df['Date'],df['Lower Bound'],label='Lower Bound',color="#073F1E")
plt.fill_between(x,y1,y2,color="#86D5EF",alpha=0.25) #Filling colour between the upper bound and lower bound of the Bollinger's Band
plt.show()