import requests
import json


url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid="
api_key = "42636c0c2b8f333b7781ecd02598b844"
url_key = url + api_key
print(url_key)

response = response.get(f"{url_key}")










import pandas as pd

# Create csv file, dataframe, print to csv
open('new_file.csv', 'wb')
dataSet1 = {'Category': ['A', 'B', 'C'],
            'Amounts': [1, 2, 4]}
df = pd.DataFrame(dataSet1)

df.to_csv('new_file.csv', sep=',', index=False)
