import pandas as pd


mydata = pd.read_csv("student.csv")
print(mydata)

age = mydata[mydata.Age >20]
print(age)

print(mydata["CGA"].mean().round(2))
print(mydata.sort_values(by='CGA', ascending=False))
print(mydata.head(3))