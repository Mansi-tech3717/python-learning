import pandas as pd
df = pd.read_json("output.json")

print('Displaying the info of the data sets')
print(df.info())