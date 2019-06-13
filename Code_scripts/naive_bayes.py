import numpy as np

from sklearn.naive_bayes import GaussianNB

# x is the input data
# y is the labels
# what about the features that we want or how does it differenciate between the two labels

X = np.array([[-1, -1], [-2, 1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
clf = GaussianNB()
clf.fit(X, Y)

print(clf.predict([[0.8, -1]]))
