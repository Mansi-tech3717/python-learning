import pandas as pd
data ={
    "Name":['Mansi','Kittu','Yashi'],
    "Age":[20,20,10],
    "Salary":[2000000,4500000,504900]
}
df= pd.DataFrame(data)
print(df)

#.loc[]
#df.loc[row_index,"column name",] = new_value
df.loc[0,'Salary'] = 550000000
print(df)