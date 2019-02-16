# Encoding categorical data

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


# Importing the data set
data_set = pd.read_csv('50_Startups.csv')
X = data_set.iloc[:, :-1].values
y = data_set.iloc[:, 4].values

label_encoder = LabelEncoder()
X[:, 3] = label_encoder.fit_transform(X[:, 3])
one_hot_encoder = OneHotEncoder(categorical_features=[3])
X = one_hot_encoder.fit_transform(X).toarray()

# Avoiding dummy variable trap
X = X[:, 1:]