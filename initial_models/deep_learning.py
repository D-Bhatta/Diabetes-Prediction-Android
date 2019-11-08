import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

diabetes = pd.read_csv('diabetes.csv')

X_train, X_test, Y_train, Y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)

mlp = MLPClassifier(random_state=42)
mlp.fit(X_train, Y_train)
print("Accuracy on training set: {:.2f}".format(mlp.score(X_train, Y_train)))
print("Accuracy on test set: {:.2f}".format(mlp.score(X_test, Y_test)))


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
mlp = MLPClassifier(random_state=0)
mlp.fit(X_train_scaled, Y_train)
print("Accuracy on training set: {:.3f}".format(
    mlp.score(X_train_scaled, Y_train)))
print("Accuracy on test set: {:.3f}".format(mlp.score(X_test_scaled, Y_test)))

mlp = MLPClassifier(max_iter=1000, random_state=0)
mlp.fit(X_train_scaled, Y_train)
print("Accuracy on training set: {:.3f}".format(
    mlp.score(X_train_scaled, Y_train)))
print("Accuracy on test set: {:.3f}".format(mlp.score(X_test_scaled, Y_test)))

mlp = MLPClassifier(max_iter=1000, alpha=1, random_state=0)
mlp.fit(X_train_scaled, Y_train)
print("Accuracy on training set: {:.3f}".format(
    mlp.score(X_train_scaled, Y_train)))
print("Accuracy on test set: {:.3f}".format(mlp.score(X_test_scaled, Y_test)))

diabetes_features = [x for i,x in enumerate(diabetes.columns) if i!=8]
plt.figure(figsize=(20, 5))
plt.imshow(mlp.coefs_[0], interpolation='none', cmap='viridis')
plt.yticks(range(8), diabetes_features)
plt.xlabel("Columns in weight matrix")
plt.ylabel("Input feature")
plt.colorbar()
plt.savefig('feature_importance_deep_learning')

'''
Accuracy on training set: 0.73
Accuracy on test set: 0.72
Accuracy on training set: 0.823
Accuracy on test set: 0.802
Accuracy on training set: 0.908
Accuracy on test set: 0.792
Accuracy on training set: 0.806
Accuracy on test set: 0.797
'''