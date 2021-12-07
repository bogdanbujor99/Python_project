from Least_Squares_Regression import Least_Squares_Regression
from Point import Point
from Plot import Plot

points = []
x = [2,3,5,7,9]
y = [4,5,7,10,15]
for p in range(len(x)):
    P = Point(x[p],y[p])
    points.append(P)
list = Least_Squares_Regression(points)
Plot(list)