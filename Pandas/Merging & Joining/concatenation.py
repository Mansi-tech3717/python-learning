import pandas as pd 
df_Region1 = pd.DataFrame({
    'Region': ['East', 'West', 'North', 'South'],
    'Sales': [100, 200, 300, 400]
})
print(df_Region1)

df_Region2 = pd.DataFrame({
    'Region': ['East', 'West', 'North', 'South'],
    'Sales': [150, 250, 350, 450]
})
print(df_Region2)

#concatenate vertically
df_concat = pd.concat([df_Region1, df_Region2], ignore_index=True)
print("Concatenated DataFrame (Vertical):")
print(df_concat)
