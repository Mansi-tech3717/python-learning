import pandas as pd
data ={
    "Name":['Mansi','Kittu','Yashi'],
    "Age":[20,20,10],
    "Salary":[2000000,4500000,504900]
}
df=pd.DataFrame(data)
print(df)
print(f'Shapes: {df.shape}')
print(f'Column Names: {df.columns}')