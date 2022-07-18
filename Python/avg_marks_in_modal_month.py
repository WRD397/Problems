import pandas as pd
df = pd.DataFrame({'Date':["2015-12-06", "2011-12-27", "2015-09-07", "2012-12-21", "2020-02-13", "2015-06-09"], 'RID':[498, 721, 375, 464, 813, 853], 'Phy':[22, 45, 1, 65, 22, 17], 'Chem':[52, 56, 32, 50, 24, 61], 'Math':[63, 37, 68, 62, 43 ,42]}) 

df['Date'] = pd.DatetimeIndex(df['Date'])
df['freq'] = df['Date'].dt.month_name().str[:3]
month_freq = pd.DataFrame(df['freq'].value_counts())
month_freq['month'] = month_freq.index
month_freq = month_freq.sort_values(by='freq',ascending=False)
month_freq = month_freq.sort_values(by='month', ascending=True)
result = []

## most_feq_value and corresponding month
most_freq_value = month_freq['freq'][0]
most_freq_month = month_freq['month'][0]
result.append(most_freq_value)
result.append(most_freq_month)


## avg subject numbers
df_avg = df.groupby('freq').mean(['Phy','Chem','Math'])
df_avg = df_avg.loc[most_freq_month,['Phy','Chem','Math']]
avg_numbers = [round(df_avg['Phy'],2), round(df_avg['Chem'],2), round(df_avg['Math'],2) ]
for value in avg_numbers : result.append(value)
print(result )

