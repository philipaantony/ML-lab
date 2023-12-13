from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score

iris = load_iris()
x = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
d = DecisionTreeClassifier(max_depth=3)

clf = d.fit(X_train,y_train)
y_predit = d.predict(X_test)
print(y_predit)
print(classification_report(y_test,y_predit))
print(accuracy_score(y_test,y_predit))

plot_tree(clf,filled=True,feature_names=iris.feature_names,class_names=iris.target_names)
plt.show()
