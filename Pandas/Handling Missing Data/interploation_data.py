import pandas as pd

data = {
    "Name": ['Mansi', 'Kittu', 'Yashi'],
    "Age": [20, None, 10],
    "Salary": [2000000, 4500000, 504900]
}

df = pd.DataFrame(data)

print(df)

df[["Age", "Salary"]] = df[["Age", "Salary"]].interpolate(
    method='linear', axis=0
)

print("Modified data")
print(df)