import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

print(np.add(arr1,arr2))
print(arr1+arr2)

print(np.multiply(arr1,arr2))
print(arr1*arr2)

arr3 = np.concatenate((arr1, arr2)) #NEED TWO ((.....))
print(arr3)
print(np.max(arr3))

print(np.mean(arr3))


