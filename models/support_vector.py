import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

diabetes = pd.read_csv('diabetes.csv')

X_train, X_test, Y_train, Y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)


svc = SVC()
svc.fit(X_train, Y_train)

print("Accuracy on training set: {:.2f}".format(svc.score(X_train, Y_train)))
print("Accuracy on test set: {:.2f}".format(svc.score(X_test, Y_test)))

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

svc = SVC()
svc.fit(X_train_scaled, Y_train)

print("Accuracy on training set: {:.2f}".format(svc.score(X_train_scaled, Y_train)))
print("Accuracy on test set: {:.2f}".format(svc.score(X_test_scaled, Y_test)))

svc = SVC(C=1000)
svc.fit(X_train_scaled, Y_train)

print("Accuracy on training set: {:.3f}".format(
    svc.score(X_train_scaled, Y_train)))
print("Accuracy on test set: {:.3f}".format(svc.score(X_test_scaled, Y_test)))



'''
Accuracy on training set: 1.00
Accuracy on test set: 0.65
Accuracy on training set: 0.77
Accuracy on test set: 0.77
Accuracy on training set: 0.790
Accuracy on test set: 0.797

'''