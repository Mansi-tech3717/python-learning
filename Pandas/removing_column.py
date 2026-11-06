import pandas as pd
data ={
    "Name":['Mansi','Kittu','Yashi'],
    "Age":[20,20,10],
    "Salary":[2000000,4500000,504900]
}
df= pd.DataFrame(data)
print(df)

#df.drop(columns = ['ColumnName'],inplace=true)
print("Modified data")
df.drop(columns=['Salary'],inplace=True)
print(df)