import pandas as pd

data = {
    "Name": ['Mansi', 'Kittu', 'Yashi'],
    "Age": [20, None, 10],
    "Salary": [2000000, 4500000, 504900]
}

df = pd.DataFrame(data)

print(df)
grouped = df.groupby(["Age", "Name"])["Salary"].sum()
print(grouped)