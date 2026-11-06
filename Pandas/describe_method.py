#step-1 sample data frame
import pandas as pd
data ={
    "Name":['Mansi','Kittu','Yashi'],
    "Age":[20,20,10],
    "Salary":[2000000,4500000,504900]
}
df= pd.DataFrame(data)
print("Sample DataFrame")
print(df)
# describe() method numerical data ki statistical summary deta hai
print("descriptive Statstics")
print(df.describe())