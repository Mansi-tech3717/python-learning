import pandas as pd
data ={
    "Name":['Mansi','Kittu','Yashi'],
    "Age":[20,30,10],
    "Salary":[2000000,4500000,504900]
}
df= pd.DataFrame(data)
print(df)
df.sort_values(by="Salary",ascending=True,inplace=True)
print(df)