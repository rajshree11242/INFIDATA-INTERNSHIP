import pandas as pd

data=pd.read_csv("diabetes.csv")
print(data)

print("display specfic columns")
print(data['Glucose'])
print(data[["glucose","BMI"]])

print(data.shape)

print(data.size)

print(data.head())
print(data.tail())