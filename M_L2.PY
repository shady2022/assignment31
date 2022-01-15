from tkinter import Scale
import numpy
import matplotlib.pyplot as plt 
import matplotlib.image as pltimg
from sklearn.metrics import r2_score
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler


numpy.random.seed(2)
scale = StandardScaler()

x1 = numpy.random.normal(3, 1, 100)
y1 = numpy.random.normal(150, 40, 100) / x1

train_x1 = x1[:80]
train_y1= y1[:80]

test_x1 = x1[80:]
test_y1 = y1[80:]

mymodel1 = numpy.poly1d(numpy.polyfit(train_x1, train_y1, 4))

r2 = r2_score(test_y1, mymodel1(test_x1))
print("r2", r2)
print(mymodel1(5))

x2 = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y2 = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel2 = numpy.poly1d(numpy.polyfit(x2, y2, 3)) 
myline = numpy.linspace(1, 22, 100)
speed = mymodel2(17)
#print(speed)

df1 = pandas.read_csv("E:\\python\\1\\cars.csv")
x = df1 [["Weight", "Volume"]]

scaledX = scale.fit_transform(x)
print(scaledX)

y = df1["CO2"]

regr = linear_model.LinearRegression()
regr.fit(x, y)

predictedCO2 = regr.predict([[2300, 1300]])


print(predictedCO2)
print(regr.coef_)
#print(r2_score(y, mymodel(x)))

plt.scatter(train_x1, train_y1)
#plt.scatter(x1, y1) 
#plt.scatter(x2, y2)
plt.plot(myline, mymodel2(myline))
plt.show() 