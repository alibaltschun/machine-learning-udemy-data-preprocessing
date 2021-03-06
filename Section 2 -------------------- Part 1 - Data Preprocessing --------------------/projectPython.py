# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:04:26 2017

@author: Ali Baltschun
"""

# Data Processing

# importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

# taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values= 'NaN' , strategy= 'mean' , axis=0)
imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

# Encoding categorial data
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelEncoder_X = LabelEncoder()
x[:,0] = labelEncoder_X.fit_transform(x[:,0]) 

oneHotEncoder = OneHotEncoder(categorical_features = [0])
x = oneHotEncoder.fit_transform(x).toarray()

labelEncoder_Y = LabelEncoder()
y = labelEncoder_Y.fit_transform(y) 

# Splitting the dataset into Trainsing set and Test set
from sklearn.cross_validation import train_test_split
x_train , x_test , y_train, y_test = train_test_split(x,y ,test_size = 0.2, random_state = 0)

# Feature Scalling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)


























