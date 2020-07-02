from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import export_graphviz
import graphviz

df = pd.read_csv('cosmetic.csv')
test = [['< 21','Low','Female','Married']]
test_data = pd.DataFrame(test,columns=['AGE','INCOME','GENDER','MARITAL STATUS'])
replace_data = {'AGE':{'< 21':1, '21-35':2, '> 35':3},
                'INCOME':{'Low':1, 'Medium':2, 'High':3},
                'GENDER':{'Male':1, 'Female':2},
                'MARITAL STATUS':{'Single':1, 'Married':2},
                'BUYS':{'N':0, 'Y':1}}
df.replace(replace_data, inplace=True)
test_data.replace(replace_data, inplace=True)

X = df[['AGE','INCOME','GENDER','MARITAL STATUS']]
Y = df['BUYS']
xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=.2)
clf = DecisionTreeClassifier()
clf.fit(xtrain,ytrain)
print(clf.predict(test_data))

x = export_graphviz(clf,rounded=True,filled=True,feature_names=['AGE','INCOME','GENDER','MARITAL STATUS'],class_names=['0','1'],out_file=None)
g = graphviz.Source(x)