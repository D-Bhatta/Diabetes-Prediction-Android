import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)

from sklearn.linear_model import LogisticRegression

diabetes = pd.read_csv('diabetes.csv')

X_train, X_test, Y_train, Y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)

logreg = LogisticRegression().fit(X_train, Y_train)
print("Training set score: {:.3f}".format(logreg.score(X_train, Y_train)))
print("Test set score: {:.3f}".format(logreg.score(X_test, Y_test)))

logreg001 = LogisticRegression(C=0.01).fit(X_train, Y_train)
print("Training set accuracy: {:.3f}".format(logreg001.score(X_train, Y_train)))
print("Test set accuracy: {:.3f}".format(logreg001.score(X_test, Y_test)))

logreg100 = LogisticRegression(C=100).fit(X_train, Y_train)
print("Training set accuracy: {:.3f}".format(logreg100.score(X_train, Y_train)))
print("Test set accuracy: {:.3f}".format(logreg100.score(X_test, Y_test)))

diabetes_features = [x for i,x in enumerate(diabetes.columns) if i!=8]
plt.figure(figsize=(8,6))
plt.plot(logreg.coef_.T, 'o', label="C=1")
plt.plot(logreg100.coef_.T, '^', label="C=100")
plt.plot(logreg001.coef_.T, 'v', label="C=0.001")
plt.xticks(range(diabetes.shape[1]), diabetes_features, rotation=90)
plt.hlines(0, 0, diabetes.shape[1])
plt.ylim(-5, 5)
plt.xlabel("Feature")
plt.ylabel("Coefficient magnitude")
plt.legend()
plt.savefig('log_coef')

'''Training set score: 0.781
Test set score: 0.771
Training set accuracy: 0.700
Test set accuracy: 0.703
Training set accuracy: 0.785
Test set accuracy: 0.766'''