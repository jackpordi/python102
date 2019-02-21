import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('./oscars.csv', skipinitialspace=True)
del df['Index']
# print(df)

df['Born'] = df['Year'] - df['Age']

# print(df)

df = df.sort_values("Name")
# print(df)

df = df.sort_values("Born")
print(df)

print(df.loc[df['Age'] < 30])

print(df[:30][["Name", "Age"]])

namecount = df.groupby("Name").count()
print(namecount)
print(namecount.sort_values("Year"))
