from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


iris = load_iris()
x = iris.data
y = iris.target
knn = KNeighborsClassifier(n_neighbors=7)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
knn.fit(X_train,y_train)

y_predit = knn.predict(X_test)
result = accuracy_score(y_test,y_predit)
print(y_predit)
print(result)