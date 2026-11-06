import pandas as pd
data ={
    "Name":['Mansi','Kittu','Yashi'],
    "Age":[20,30,10],
    "Salary":[2000000,4500000,504900]
}
df= pd.DataFrame(data)
print(df)
grouped= df.groupby("Age")["Salary"].sum()
print(grouped)