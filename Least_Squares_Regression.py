from Point import Point

class Least_Squares_Regression:
    def __init__(self,array_points):
        self.__points = array_points
        self.__x_square = []
        self.x_to_square()

    def x_to_square(self):
        for point in self.__points:
            self.__x_square.append(point.get_x() * point.get_x())
            print(point.get_x() * point.get_x())
    
    def x_multiplied_by_y(self):
        self.__xy= []
