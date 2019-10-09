import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals.joblib import dump
from sklearn.externals.joblib import load



from sklearn.linear_model import LogisticRegression

diabetes = pd.read_csv('diabetes.csv')

X_train, X_test, Y_train, Y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)

model = LogisticRegression(C=1).fit(X_train, Y_train)
print("Training set score: {:.3f}".format(model.score(X_train, Y_train)))
print("Test set score: {:.3f}".format(model.score(X_test, Y_test)))

# save the model to disk
filename = 'finalized_logistic_reg_model.sav'
dump(model, filename)
# some time later...
# load the model from disk
loaded_model = load(filename)
print("Test set score: {:.3f}".format(loaded_model.score(X_test, Y_test)))


'''Training set score: 0.781
Test set score: 0.771
Training set accuracy: 0.700
Test set accuracy: 0.703
Training set accuracy: 0.785
Test set accuracy: 0.766'''