import pandas as pd

data = pd.read_csv("C:/Users/rohan/Code/ug-semester-6/src/dscc-14/data.csv")
print(data.head(2))
print()
print(data.tail(2))
print()
print(data.describe(include="all"))
print()
print(data.shape)
print()
print(data[0:2])
print()
print(data.drop_duplicates())
