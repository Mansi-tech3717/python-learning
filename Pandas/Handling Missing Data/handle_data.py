import pandas as pd
data ={
    "Name":['Mansi',None,'Yashi'],
    "Age":[20,None,10],
    "Salary":[200000,None,504900]
}
df= pd.DataFrame(data)
print(df)
df.dropna(inplace=True)
print(df)