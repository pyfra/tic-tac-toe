import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

######### Read and prepare the data
dir_path = os.path.dirname(os.path.realpath(__file__))
data_raw = pd.read_csv(os.path.join(dir_path, 'dataset', 'tic-tac-toe.data'))

# Define and prepare y
y = data_raw['positive']
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Define and prepare X
X = data_raw.iloc[:, :9]
X = OneHotEncoder().fit_transform(X).toarray()

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from keras.models import Sequential
from keras.layers import Dense, ReLU, Activation, LeakyReLU, Dropout

# Initialize neural network
nn = Sequential()

# Add first hidden layer (and input layer)
nn.add(Dense(units=9, kernel_initializer='glorot_normal', input_dim=27))
nn.add(Activation('tanh'))
nn.add(Dropout(.5))

# Add second hidden layer
nn.add(Dense(units=5, kernel_initializer='glorot_normal'))
nn.add(Activation('tanh'))
nn.add(Dropout(.5))

# Add second hidden layer
nn.add(Dense(units=3, kernel_initializer='glorot_normal'))
nn.add(Activation('tanh'))

# Add output layer
nn.add(Dense(units=1, kernel_initializer='glorot_normal'))
nn.add(Activation('sigmoid'))

# Compile network
nn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout

# Initialize neural network
nn = Sequential()

# Add first hidden layer (and input layer)
nn.add(Dense(units=9, kernel_initializer='glorot_normal', input_dim=27))
nn.add(Activation('tanh'))
nn.add(Dropout(.5))

# Add second hidden layer
nn.add(Dense(units=5, kernel_initializer='glorot_normal'))
nn.add(Activation('tanh'))
nn.add(Dropout(.5))

# Add second hidden layer
nn.add(Dense(units=3, kernel_initializer='glorot_normal'))
nn.add(Activation('tanh'))

# Add output layer
nn.add(Dense(units=1, kernel_initializer='glorot_normal'))
nn.add(Activation('sigmoid'))

# Compile network
nn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train network

# Train network
nn.fit(X_train, y_train, batch_size=20, epochs=100)

# score on validation test
score = nn.evaluate(X_test, y_test)
_, accuracy = nn.evaluate(X_test, y_test)

print('accuracy on validation test %.4f' % accuracy)

##### Save model
print('Saving model...')
import os

target_path = os.path.join(os.path.dirname(__file__), 'trained_models', 'nn_model.h5')
nn.save(target_path)
print('model saved in %s' % target_path)
