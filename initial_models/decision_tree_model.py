import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.externals.joblib import dump
from sklearn.externals.joblib import load


diabetes = pd.read_csv('diabetes.csv')

X_train, X_test, Y_train, Y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)

from sklearn.tree import DecisionTreeClassifier



model = DecisionTreeClassifier(max_depth=3, random_state=0)
model.fit(X_train, Y_train)

print("Accuracy on training set: {:.3f}".format(model.score(X_train, Y_train)))
print("Accuracy on test set: {:.3f}".format(model.score(X_test, Y_test)))

# save the model to disk
filename = 'finalized_decision_tree_model.sav'
dump(model, filename)
# some time later...
# load the model from disk
loaded_model = load(filename)
print("Test set score: {:.3f}".format(loaded_model.score(X_test, Y_test)))




'''Accuracy on training set: 0.773
Accuracy on test set: 0.740
Test set score: 0.740'''