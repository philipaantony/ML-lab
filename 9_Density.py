import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]

sns.kdeplot(x)
plt.show()

sns.barplot(x=x,y=y)
plt.show()

plt.scatter(x,y,alpha=0.6)
plt.show()
