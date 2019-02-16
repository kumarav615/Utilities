# Data Pre processing Template

# Importing the libraries
import pandas as pd
from sklearn.cross_validation import train_test_split

# Importing the data set
data_set = pd.read_csv('Salary_Data.csv')
X = data_set.iloc[:, :-1].values
y = data_set.iloc[:, -1].values

# Splitting the data set into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
