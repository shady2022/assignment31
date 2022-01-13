import numpy
from numpy.lib.function_base import median
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.image as pltimg


speed =[5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]


Mean = numpy.mean(speed)
Median = numpy.median(speed)
Mode = stats.mode(speed)

x1 = numpy.std(speed)
x2 = numpy.percentile(speed, 90)

#x = numpy.random.uniform(0.0, 5.0, 250)

num = numpy.random.uniform(0.0, 5.0, 100000)

#x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
#y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(slope, intercept, r, p, std_err)

def myfunc(x):
  return slope * x + intercept
  
speed = myfunc(10)
mymodel = list(map(myfunc, x))

mymodel = np.poly1d(np.polyfit(x, y, 3))

myline = np.linspace(1, 22, 100)
print(r2_score(y, mymodel(x)))


plt.plot(myline, mymodel(myline))
#plt.hist(num, 100)

print(speed)
#print(Mean)
#print(Median)
#print(Mode)
plt.scatter(x, y)
#plt.plot(x, mymodel)
#plt.hist(x, 100)
#plt.hist(x, 5)
plt.show() 
print(x)