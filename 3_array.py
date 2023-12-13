import numpy as np


grades = np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])
print("Avg Garde :",np.mean(grades))

filter_grade = grades[grades>90]
print(filter_grade)
print("count :",len(filter_grade))

print("SD :",np.std(grades))

print("SD :",np.round(18.989098,decimals=2)) #decimals need s 
