import numpy as np
from sklearn.tree import DecisionTreeClassifier
import graphviz
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import os
data=pd.read_csv('Dataset.csv')
le=LabelEncoder()
data['Age']=le.fit_transform(data['Age'])
data['Income']=le.fit_transform(data['Income'])
data['Marital Status']=le.fit_transform(data['Marital Status'])
data['Gender']=le.fit_transform(data['Gender'])

data['Buys']=le.fit_transform(data['Buys'])
y=data['Buys']
#data=data.drop(columns="ID",axis=1)
data=data.drop(columns="Buys",axis=1)
print(data)
clf= DecisionTreeClassifier(criterion='gini')
clf.fit(data,y)
#print(clf.node_count)
test=np.array([1,3,1,0])
test=test.reshape(1,-1)
ypred=clf.predict(test)
print(ypred)
dot_data=tree.export_graphviz(clf,out_file=None,feature_names=["Age","Income","Gender","Marital Status"])
graph=graphviz.Source(dot_data)
(graph).view()
