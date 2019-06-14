from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1, cache=True)
print(mnist)
X, y 