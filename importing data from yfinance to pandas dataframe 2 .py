import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = yf.download('AAPL',start="2021-01-01",end='2025-07-13')
print(df.head()) #display the first five rows of the dataframe
print(df) #to display hte entire dataframe
print(df['Low']) #to select a particular column
print(df.head(122)) #to select a range of rows
print ( " TO CATEGORISE DATA ")
print(df[df['High']>150]) #to categorise data
df['Daily Return'] = df['Close'].pct_change() #to add new column
print(df.head())
print(df.columns) #printing the headers of the columns
df= df.reset_index()
print(df.head())
print(df.columns)
#creating a line plot of 'Close' w.r.t data
print("\nType of 'Date' column:", type(df['Date']))
print("Type of 'Close' column:", type(df['Close']))
sns.lineplot(x='Date',y='Close',data=df.droplevel(1,axis = 1))
#df=pd.DataFrame(df)
#df['Close'].plot(kind='line',x='Date',y='Close',title="Representatiion of Close w.r.t. Date")
plt.show()