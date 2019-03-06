import pandas as pd

pd.set_option('display.max_columns', 500)

df = pd.read_csv('oscars.csv', skipinitialspace=True)
print(df)
