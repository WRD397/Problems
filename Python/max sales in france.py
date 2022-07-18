import pandas as pd
df = pd.read_csv("sales_dataset.csv")
df['sales']=df['Quantity']*df['Price']

df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])
df['Date']=df['InvoiceDate'].dt.date
mod1=df.groupby(['Country','Date']).sum()
ans=max(mod1.loc['France','sales'])
print(mod1[mod1['sales']==ans])  #This will retrieve the row of grouped dataframe along with date and country.