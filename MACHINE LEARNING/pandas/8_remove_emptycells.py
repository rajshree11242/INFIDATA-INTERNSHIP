import pandas as pd

df = pd.read_csv('data.csv')
print('[info] data aloaded successfully...')

print('[info] checking forNaN values...')
print(df.columns[df.isna().any()])
print('[info] removing NaN values...')
de=df.dropna()

print('[info] checking for NaN values again...')
print(df.column[df.isna().any()])
