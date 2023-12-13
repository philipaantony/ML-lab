from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
print(iris)
x = iris.data
y = iris.target

kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(x)
centroid = kmeans.cluster_centers_
label = kmeans.labels_

plt.scatter(x[:, 0], x[:, 1], c = label, cmap = 'viridis', marker = 'o', edgecolors = 'black')
plt.scatter(centroid[:, 0], centroid[:, 1], marker = "*", s = 200, c = 'red', label = 'Centroids')
plt.title('KMeans Cluster of Iris Dataset') 
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()




