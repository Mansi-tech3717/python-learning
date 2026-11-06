import pandas as pd
data = {
    "name":['Mansi','Kittu','Yashi'],
    "age" :[20,20,10],
    "city":['Jaipur','Pratap Nagar','Sanganer']
}
df = pd.DataFrame(data)
print(df)
# df.to_csv("output.csv",index=False) # if we not need index 
# df.to_excel("output.xlsx")
df.to_json("output.json")