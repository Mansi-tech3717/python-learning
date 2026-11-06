import pandas as pd

#customer dataframe
df_customer = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4, 5],
    "CustomerName": ["John", "Alice", "Bob", "Eve", "Charlie"],
})

#order dataframe
df_order = pd.DataFrame({
    "OrderID": [1, 2, 3, 4, 5],
    "CustomerID": [1, 2, 1, 3, 4],
    "OrderAmount": [250, 150, 300, 200, 400],
})

#  merge dataframes
df_merged = pd.merge(df_customer, df_order, on="CustomerID", how="inner")
print("Merged DataFrame: Inner Join")
print(df_merged)

df_merged = pd.merge(df_customer, df_order, on="CustomerID", how="outer")
print("Merged DataFrame: outer Join")
print(df_merged)

df_merged = pd.merge(df_customer, df_order, on="CustomerID", how="left")
print("Merged DataFrame: Left Join")
print(df_merged)

df_merged = pd.merge(df_customer, df_order, on="CustomerID", how="right")
print("Merged DataFrame: Right Join")
print(df_merged)
