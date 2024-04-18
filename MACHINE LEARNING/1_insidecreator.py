import pandas as pd

data=pd.DataFrame({
    "name":["ali","khan","mahesh","vinit"],
    "age":[20,30,40,50],
    "branch":["cse","me","ise","ece"],
    "place":["delhi","mysore","porbandar"]
})
print(data)

data.to_csv('id.csv', index=False)