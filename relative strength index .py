import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
df = yf.download('TSLA',start='2004-01-01',end='2025-07-14')
print(df)
print(df.head(25))
delta = df['Close'].diff(1) #taking difference of close of a day with that of previous one
delta.dropna(inplace=True) #data cleaning : removing values that are N/A 
positive = delta.copy() #copying the delta data
negative = delta.copy()#copying the delta data

positive[positive < 0] = 0 #making all the values (that are less than 0) in the positive date equal to 0
negative[negative > 0] = 0 #making all the values (that are greater than 0) in the negative date equal to 0

average_gain = positive.rolling(window = 25).mean() #calculating the average gain, used for RSI
average_loss = negative.rolling(window = 25).mean() #calculating the average loss, used for RSI

relative_strength = average_gain / average_loss # claculating the relative strength, used for RSI
rsi = 100.0 - (100.0/(1+relative_strength)) # calculating RSI with the formula

combined = pd.DataFrame() #creating a new data frame with pandas called combined
combined['Close'] = df['Close'] # creating a 'Close' column in combined and copying the close data of df ('TSLA') in the 'Close' column of combined
combined['RSI'] = rsi # storing the data of rsi in a column (which we created and added just now) in the 'RSI' column of combined
print(combined)

# plotting both rsi and close in the same plot (sub-plotting)
plt.figure(figsize=(12,8))
ax1 = plt.subplot(211)
ax1.plot(df.index,df['Close'])
ax1.set_title('Close Price',color='black')
ax1.grid(True,color='#555555')
ax1.set_axisbelow(True)
ax1.set_facecolor('white')
ax1.figure.set_facecolor('white')
ax1.tick_params(axis='x',color='white')
ax1.tick_params(axis='y',color='white')

ax2 = plt.subplot(212)
ax2.plot(combined.index,combined['RSI'])
ax2.set_title('RSI',color='black')
ax2.grid(False)
ax2.set_axisbelow(True)
ax2.set_facecolor('white')
ax2.figure.set_facecolor('white')
ax2.tick_params(axis='x',color='white')
ax2.tick_params(axis='y',color='white')
ax2.axhline(0, linestyle='--',color='red')
ax2.axhline(30, linestyle='--',color='blue')
ax2.axhline(70, linestyle='--',color='green')
ax2.sharex(ax1)
#ax2.sharey(ax1)

plt.show()
