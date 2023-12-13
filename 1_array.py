import numpy as np

myarr = np.array([10, 12,9, 1, 15, 15])
print(myarr)

print("new array after ",np.insert(myarr,[2,3],[100,100]))

print(np.append(myarr, [1, 2, 3]))

print(np.insert(myarr, 3, 100))

print(np.delete(myarr, 0))

print(np.unique(myarr))

print(np.sort(myarr)[::-1])
print(np.sort(myarr))

np.savetxt("myarr.txt",myarr)
mydata = np.loadtxt("myarr.txt")
print(mydata)

