import matplotlib.pyplot as plt
import numpy as np

#plot 1:
#x0 = np.array([0, 1, 2, 3])
#y0 = np.array([3, 8, 1, 10])

#plt.subplot(1, 2, 1)
#plt.plot(x0,y0)
#plt.title("SALES")

#plot 2:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([10, 20, 30, 40])


x2 = np.random.randint(100, size=(100))
y2 = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

x3 = np.array(["A", "B", "C", "D"])
y3 = np.array([3, 8, 1, 10])

plt.bar(x3, y3, width = 0.1)

plt.scatter(x2, y2, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")

x = np.random.normal(170, 10, 250)

plt.hist(x)

plt.colorbar()


#plt.subplot(1, 2, 2)
#plt.plot(x1,y1)
#plt.title("INCOME")

#plt.suptitle("MY SHOP")
plt.show()