import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor

from keras.models import Sequential
from keras.layers.core import Dense, Activation

# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)


df = pd.read_csv('druguse.csv')
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
del df['UseLevel']


def jitter_plot(data, x, y):
    x_data = data[x] + np.random.rand(len(data)) * 0.5
    y_data = data[y] + np.random.rand(len(data)) * 0.5
    plt.scatter(x_data, y_data, c=data["severity"], cmap="bwr")
    plt.show()
    plt.clf()

df['agegroup'] = df['agegroup'].map({
    '18-24': 0,
    '25-34': 1,
    '35-44': 2,
    '45-54': 3,
    '55-64': 4,
    '65+': 5
})

df['gender'] = df['gender'].map({
    'male':  0,
    'female': 1
})


ethnicity_df = pd.get_dummies(df['ethnicity'], prefix='ethnicity')
df = df.drop('ethnicity', axis=1)
df = df.join(ethnicity_df)

country_df = pd.get_dummies(df['country'], prefix='country')
df = df.drop('country', axis=1)
df = df.join(country_df)


train_set = df.iloc[:1500]
train_x = train_set.drop('severity', axis=1).values
train_y = train_set['severity'].values

test_set = df.iloc[1500:]
test_x = test_set.drop('severity', axis=1).values
test_y = test_set['severity'].values


model = Sequential()
model.add(Dense(32, input_shape=(28,), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(train_x, train_y, nb_epoch=100, batch_size=1)

pred_y = model.predict(test_x).reshape(len(test_x))
print(pred_y)



# We can now compare pred_y with actual test_y
results = pd.DataFrame({
    'predictions': pred_y,
    'actual': test_y,
    'error': np.absolute(pred_y - test_y)
})
print(results)
