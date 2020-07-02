# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:34:52 2019

@author: percy
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
df = pd.read_csv('hours.csv')
linear = LinearRegression()
linear.fit(df[['Hours']],df['Risk'])
#regression_line = [(linear.coef_*i)+linear.intercept_ for i in list(df['Hours'])]
iVal = float(input('Enter your value: '))
iVal = np.array(iVal).reshape(1,-1)
print('Input Prediction: ',linear.predict(iVal))
plt.scatter(list(df['Hours']), list(df['Risk']))
plt.plot(list(df['Hours']), linear.predict(df[['Hours']]))
plt.scatter(iVal,int(linear.predict(iVal)))
plt.show()