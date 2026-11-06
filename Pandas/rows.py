import pandas as pd

#head() :- It is used to display starting rows of tables (default = 5)
#tail() :- It is used to display last rows of tables (default = 5)

df = pd.read_csv("sales_sample_data.csv")
print("Display starting rows of table")
print(df.head(4))

print("Display Last rows of table")
print(df.tail(4))
