# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 22:31:22 2019

@author: percy
"""
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
repString = {'Class':{'Positive':1,'Negative':0}}
df.replace(repString,inplace=True)
X = df[['X','Y']]
Y = df['Class']
xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=.2)

test_data=[[5,5]]

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(xtrain,ytrain)
print(clf.predict(test_data))

clf = KNeighborsClassifier(n_neighbors=3,weights='distance')
clf.fit(xtrain,ytrain)
print(clf.predict(test_data))
plt.scatter(X['X'],X['Y'],color='b')
plt.scatter(test_data[0][0],test_data[0][1],color='r')