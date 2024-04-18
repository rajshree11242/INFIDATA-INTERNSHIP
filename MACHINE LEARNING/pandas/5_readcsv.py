import pandas as pd

df=pd.read_csv("diabetes.csv")

print("accessing from the dataset from first 10 rows\n",df.head(10))
print("accessing from the dataset from first 5 rows\n",df.head())

print("accessing from the dataset from last 5 rows\n",df.tail())
print("accessing from the dataset from last 10 rows\n",df.tail(10))
print(df.shape)
print(df.columns[df.isna().any()]) 

print("basic info: \n",df.info())
print("statistical  info : \n",df.describe())