from Least_Squares_Regression import Least_Squares_Regression
from Point import Point
from Plot import Plot

points = []
x = [1.21,3,5.16,8.31,10.21]
y = [1.69,5.89,4.11,5.49,8.65]
for p in range(len(x)):
    P = Point(x[p],y[p])
    points.append(P)
list = Least_Squares_Regression(points)
Plot(list)