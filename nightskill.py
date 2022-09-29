# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sklearn import datasets
import pandas as pd
iris = pd.read_csv("C:\Users\Student\Downloads\archive (7)")
print(iris.target_names)
print(iris.feature_names)
X, y = datasets.load_iris(return_X_y = True)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.30)
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
clf= RandomForestClassifier(n_estimators = 100)
clf.fit(X_train, y_train)
