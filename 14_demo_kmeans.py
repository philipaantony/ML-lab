from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


iris = load_iris()
x = iris.data
y = iris.target

kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(x)
label = kmeans.labels_
centroids = kmeans.cluster_centers_

plt.scatter(x[:,0],x[:,1],c=label,cmap="",marker="o",edgecolors="black")
plt.scatter(centroids[:,0],centroids[:,1],s=200,c="red",marker="*",label='Centroid')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()

