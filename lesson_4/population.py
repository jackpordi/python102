import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("./births_deaths.csv", parse_dates=["Quarter"])

print(df)
print(df['Quarter'].dtype)

df = df.groupby(df.Quarter.dt.year).sum()
print(df)
print(df.columns.values)

# plt.plot(df['Quarter'], df['Male Live Births'])

plt.plot("Male Live Births", data=df)
plt.plot("Female Live Births", data=df)
plt.plot("Male Deaths", data=df)
plt.legend()

plt.show()
