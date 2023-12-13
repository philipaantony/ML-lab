import pandas as pd

myfile = pd.read_csv("emp.csv")
print(myfile)
print("Rows",len(myfile))
print("Columns",len(myfile.columns))

print("Total Price",sum(myfile.price))
print(myfile.head(4))
