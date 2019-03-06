import pandas as pd

# Read the CSV
df = pd.read_csv('./druguse.csv')
# print(df)

print(df.columns.values)
del df['amphetamine']
del df['amylnitrite']
del df['benzodiaz']
del df['cannabis']
del df['cocaine']
del df['crack']
del df['ecstasy']
del df['heroin']
del df['ketamine']
del df['legalhighs']
del df['LSD']
del df['methadone']
del df['mushrooms']
del df['volatiles']
del df['any']
del df['severity']
print(df)
print(df.columns.values)
