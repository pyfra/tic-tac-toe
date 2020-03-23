import pandas as pd
import os
"""
The outcome are based on X winning
"""
# read data and prepare
# read data
dir_path = os.path.dirname(os.path.realpath(__file__))
data_raw = pd.read_csv(os.path.join(dir_path, 'dataset', 'tic-tac-toe.data'))

X = data_raw.iloc[:, :9]


y = data_raw.iloc[:, 9:]

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
labelencoder_y = LabelEncoder()
y[:, 0] = labelencoder_y.fit_transform(y[:, 0])