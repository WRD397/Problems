import pandas as pd
df = pd.read_csv("sales_dataset.csv")
df[ ['Date', 'Time'] ] = df['InvoiceDate'].str.split(" ", expand=True)
#print(df[['Date','Time']].head())

mask = df['Date'] == '2011-06-22'
df_final = df[mask][['Date','Customer ID']]
print( len(df_final['Customer ID'].unique()) )