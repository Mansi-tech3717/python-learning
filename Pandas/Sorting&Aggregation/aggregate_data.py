import pandas as pd
data ={
    "Name":['Mansi','Kittu','Yashi'],
    "Age":[20,30,10],
    "Salary":[2000000,4500000,504900]
}
df= pd.DataFrame(data)
print(df)
avg_salary= df["Salary"].mean()
print("Average Salary:",avg_salary)