from time import time
import requests
import pprint
import pandas as pd

url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&symbol=BTC&market=CAD&apikey=WV6PJES3DGJQBXFM'
response = requests.get(url)
response_json = response.json()
def keep_key(keyVar):
    return keyVar in ['1a. open (CAD)', '2a. high (CAD)', '3a. low (CAD)', '4a. close (CAD)']


time_series_data = response_json['Time Series (Digital Currency Weekly)']
for price_reference in time_series_data.values():
    for key in list(price_reference.keys()):
        if not keep_key(key):
            del price_reference[key]

data = pd.DataFrame(time_series_data)

df = data.loc[ : , data.columns >= '2022-01-01'] #get everything past start of year.
col_count = df.shape[1]
print(col_count)
print(data)
writer = pd.ExcelWriter('bitCoinValue_2022_3.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Bitcoin_Value')
worksheet = writer.sheets['Bitcoin_Value']
worksheet.set_column(0, col_count, 40)
writer.save()


