import matplotlib.pyplot as plt
import numpy as np

class Plot:
    def __init__(self,list_of_points):
        self.__list = list_of_points
        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        plt.grid()
        x = []
        y = []
        x1 = []
        y1 = []
        function = 'y=' + str(list_of_points.get_m()) + 'x+' + str(list_of_points.get_b())
        plt.title('Graph of ' + function)
        points = list_of_points.get_points()
        for point in points:
            plt.plot(point.get_x(), point.get_y(), marker="o", markersize=7, markeredgecolor="green", markerfacecolor="green")
            x1.append(point.get_x())
            y1.append(point.get_y())
        points = list_of_points.get_new_points()
        for point in points:
            plt.plot(point.get_x(), point.get_y(), marker="o", markersize=7, markeredgecolor="red", markerfacecolor="red")
            x.append(point.get_x())
            y.append(point.get_y())
        plt.plot(x,y)
        plt.plot(x1,y1,color='yellow')
        plt.show()