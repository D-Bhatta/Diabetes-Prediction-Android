import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals.joblib import dump
from sklearn.externals.joblib import load

diabetes = pd.read_csv('diabetes.csv')

X_train, X_test, Y_train, Y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)


model = KNeighborsClassifier(n_neighbors=9)
model.fit(X_train, Y_train)

print('Accuracy of K-NN classifier on training set: {:.2f}'.format(model.score(X_train, Y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'.format(model.score(X_test, Y_test)))

# save the model to disk
filename = 'finalized_knn_model.sav'
dump(model, filename)
# some time later...
# load the model from disk
loaded_model = load(filename)
print('Accuracy of K-NN classifier on test set: {:.2f}'.format(model.score(X_test, Y_test)))


'''Accuracy of K-NN classifier on training set: 0.79
Accuracy of K-NN classifier on test set: 0.78
Accuracy of K-NN classifier on test set: 0.78'''