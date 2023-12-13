import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

marks = np.array([10,16,12,14,
 37, 33, 38,
 34, 24, 80,
 45, 49, 27,
 31, 35, 42])

newmark = marks.reshape(4,4)
sns.heatmap(newmark)
plt.show()



y=np.array([1,2,3,4,5])
x=np.array([10,20,30,40,50])

plt.scatter(x,y)
plt.show()

# Create a histogram
plt.hist(marks, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.show()

# Box plot using seaborn
sns.boxplot(marks, color='darkcyan')
plt.show()

# Kernel Density Estimation (KDE) plot using seaborn
sns.kdeplot(marks)
plt.show()


