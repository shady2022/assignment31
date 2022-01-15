import matplotlib.pyplot as plt 
import numpy as np

xpoints = np.array([0, 6])
y1 = np.array([0, 250])
y2 = np.array([6, 2, 7, 11])

plt.plot(xpoints, y1 ,  marker = 'o', ms = 20, mec = 'r',  mfc = 'r')

font1 = {"family": "serif", "color": "blue", "size":15}
font2 = {"family": "serif", "color": "darkred", "size":20}

plt.plot(xpoints, y1)
plt.title("the assignment of matplotlib",fontdict=font2 )
plt.xlabel("Average Pulse", fontdict=font1)
plt.ylabel("Calorie Burnage",fontdict=font1)
plt.plot(y2, color = "hotpink")
plt.plot(y1, linestyle ='dotted')
plt.show()

