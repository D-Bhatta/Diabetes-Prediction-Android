import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

diabetes = pd.read_csv('diabetes.csv')

X_train, X_test, Y_train, Y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)



gb = GradientBoostingClassifier(random_state=0)
gb.fit(X_train, Y_train)

print("Accuracy on training set: {:.3f}".format(gb.score(X_train, Y_train)))
print("Accuracy on test set: {:.3f}".format(gb.score(X_test, Y_test)))

gb1 = GradientBoostingClassifier(random_state=0, max_depth=1)
gb1.fit(X_train, Y_train)

print("Accuracy on training set: {:.3f}".format(gb1.score(X_train, Y_train)))
print("Accuracy on test set: {:.3f}".format(gb1.score(X_test, Y_test)))

gb2 = GradientBoostingClassifier(random_state=0, learning_rate=0.01)
gb2.fit(X_train, Y_train)

print("Accuracy on training set: {:.3f}".format(gb2.score(X_train, Y_train)))
print("Accuracy on test set: {:.3f}".format(gb2.score(X_test, Y_test)))

diabetes_features = [x for i,x in enumerate(diabetes.columns) if i!=8]
def plot_feature_importances_diabetes(model):
    plt.figure(figsize=(8,6))
    n_features = 8
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), diabetes_features)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(-1, n_features)

plot_feature_importances_diabetes(gb1)

plt.savefig('feature_importance_gradient_boost')


'''Accuracy on training set: 0.917
Accuracy on test set: 0.792
Accuracy on training set: 0.804
Accuracy on test set: 0.781
Accuracy on training set: 0.802
Accuracy on test set: 0.776'''