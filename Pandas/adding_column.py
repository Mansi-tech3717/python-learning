
import pandas as pd
data ={
    "Name":['Mansi','Kittu','Yashi'],
    "Age":[20,20,10],
    "Salary":[2000000,4500000,504900]
}
df= pd.DataFrame(data)
print(df)
df["Bonus"]= df["Salary"] *0.1
print(df)

#using insert()
#df.insert(loc,"Column_name",data)
df.insert(0     ,"Employee_id",[10,20,30])
print(df)