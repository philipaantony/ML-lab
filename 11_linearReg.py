import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

mydata = pd.read_csv("mark.csv")
x = mydata["studyhr"].values.reshape(-1, 1)
y = mydata["mark"].values

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_predt = model.predict(X_test)
print(model.coef_[0])
print(model.intercept_)
print(r2_score(y_test,y_predt))

plt.scatter(X_test, y_test, label="Actual Data")
plt.plot(X_test, y_predt, color="red", label="Predicted Data")
plt.xlabel("Study hr")
plt.ylabel("Mark obtained")
plt.legend()
plt.show()
new_mark = int(input("Enter your study hr: "))
pred_mark = model.predict(np.array([[new_mark]]))
print("Predicted Mark:", pred_mark)

