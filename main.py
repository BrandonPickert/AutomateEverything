import pandas as pd

open('new_file.csv', 'wb')
dataSet1 = {'Category': ['A', 'B', 'C'],
            'Amounts': [1, 2, 4]}
df = pd.DataFrame(dataSet1)

df.to_csv('new_file.csv', sep=',', index=False)
