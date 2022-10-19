from sklearn.datasets import load_iris
iris = load_iris()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

#Parametros
n_clases = 3
plot_colors = "ryb"
plot_step = 0.02

iris

from re import X
X = iris.data[:, [0,1]]
y = iris.target

# Entrenamiento 
clf = DecisionTreeClassifier().fit(X,y)

# Plot umbral de decisión
plt.figure(figsize = (10,10))

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step), np.arange(y_min, y_max, plot_step))


z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)
cs = plt.contourf(xx, yy, z, cmap=plt.cm.RdYlBu)

plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# plit de datos de entrenamiento 
for i, color in zip(range(n_clases), plot_colors):
  idx = np.where(y == 1)
  plt.scatter( X[idx, 0], X[idx, 1], c=color, label=iris.target_names[i],
      cmap=plt.cm.RdYlBu,
      edgecolor="black",
      s=40)
  
  from sklearn.tree import plot_tree
plt.figure(figsize=(15,15))
clf = DecisionTreeClassifier().fit(iris.data, iris.target)
plot_tree(clf,filled=True)
plt.title("Arbol Entrenado")
plt.show()