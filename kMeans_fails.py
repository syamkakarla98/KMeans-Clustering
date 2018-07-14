import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans

X, y = make_moons(400, noise=.05, random_state=0)
plt.scatter(X[:, 0], X[:, 1], s=25)
plt.show()

labels = KMeans(n_clusters=2, random_state=0).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels,
            s=25, cmap='viridis');
plt.show()
