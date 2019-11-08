import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.externals.joblib import dump
from sklearn.externals.joblib import load


diabetes = pd.read_csv('diabetes.csv')

X_train, X_test, Y_train, Y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)



scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
model = MLPClassifier(random_state=0)
model.fit(X_train_scaled, Y_train)
print("Accuracy on training set: {:.3f}".format(
    model.score(X_train_scaled, Y_train)))
print("Accuracy on test set: {:.3f}".format(model.score(X_test_scaled, Y_test)))





# save the model to disk
filename = 'finalized_deep_learning_model.sav'
dump(model, filename)
# some time later...
# load the model from disk
loaded_model = load(filename)
print("Test set score: {:.3f}".format(loaded_model.score(X_test_scaled, Y_test)))

'''
Accuracy on training set: 0.823
Accuracy on test set: 0.802
Test set score: 0.802
'''