# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 23:30:09 2019

@author: Dario
"""

import datetime
print(datetime.datetime.now())
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
sexencoder_X = LabelEncoder()
X[:, 2] = sexencoder_X.fit_transform(X[:, 2])
# countryencoder_X = LabelEncoder()
ct = ColumnTransformer([("trcountry", OneHotEncoder(),[1])],remainder="passthrough")
X = ct.fit_transform(X)[:,1:] #.astype(float)

#X[:, 2] = countryencoder_X.fit_transform(X[:, 2])
#onehotencoder = OneHotEncoder(categorical_features = [1])
#X = onehotencoder.fit_transform(X).toarray()

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
#X_test = np.append(X_test, np.asarray([[0,0,600,1,40,3,60000,2,1,1,50000]]), axis=0)
#y_test = np.append(y_test, np.asarray([1]),axis=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
#import keras
from keras.models import Sequential
from keras.layers import Dense

# Create your classifier here
# Initializing the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(6, input_shape=(11,), kernel_initializer='glorot_uniform', activation='relu'))

classifier.add(Dense(6, kernel_initializer='glorot_uniform', activation='relu'))

classifier.add(Dense(1, kernel_initializer='glorot_uniform', activation='sigmoid'))

classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Fitting classifier to the Training set
classifier.fit(X_train, y_train, batch_size=100, epochs=100)

# Part 3 - Making predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

X_test_homework=np.array([[0,0,600,1,40,3,60000,2,1,1,50000]])
y_pred_homework = classifier.predict(sc.transform(X_test_homework))
y_pred_homework = (y_pred_homework > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

print(datetime.datetime.now())
