import numpy as np

arr1 = np.array([[1,2,3],[5,6,7],[8,3,4]])
arr2 = np.array([[7,9,5],[2,6,7],[4,3,2]])

print((arr1+arr2))
print(arr1*arr2)
print(np.dot(arr1,arr2))
print(np.transpose(arr1))

print(np.linalg.det(arr1))
print(np.linalg.eig(arr1))
a,b = np.linalg.eig(arr1)
print(a)
print(b)

U,S,VT = np.linalg.svd(arr1)
print("\nLeft singular vectors (U):")
print(U)
print("\nSingular values (Sigma):")
print(np.diag(S))
print("\nRight singular vectors transpose (VT):")
print(VT)