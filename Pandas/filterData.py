import pandas as pd
data ={
    "Name":['Mansi','Kittu','Yashi'],
    "Age":[20,20,10],
    "Salary":[2000000,4500000,504900]
}

df= pd.DataFrame(data)
print(df)
# selecting single column
print("Names (Single column returns series)")
name= df['Name']
print(name)

#selecting mutliple columns
subset= df[["Name","Salary"]]
print('\n Subset with Name & Salary')
print(subset)
