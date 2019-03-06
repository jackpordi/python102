import pandas as pd

from sklearn.datasets import load_diabetes

diabetes = load_diabetes()

def sklearn_to_df(sklearn_dataset):
    df = pd.DataFrame(sklearn_dataset.data, columns=sklearn_dataset.feature_names)
    df['target'] = pd.Series(sklearn_dataset.target)

    return df

df =sklearn_to_df(diabetes)
print(df)
