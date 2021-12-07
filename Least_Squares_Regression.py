from Point import Point

class Least_Squares_Regression:
    def __init__(self,array_points):
        self.__points = array_points
        self.__x_square = []
        self.__xy= []
        self.__sum_x = 0
        self.__sum_y = 0
        self.__sum_x_square = 0
        self.__sum_xy = 0
        self.__m = 0
        self.__b = 0
        self.__new_points = []
        self.__x_to_square()
        self.__x_multiplied_by_y()
        self.__sum_of_x()
        self.__sum_of_y()
        self.__sum_x_to_square()
        self.__sum_of_xy()
        self.__calculate_spole_m()
        self.__calculate_intercept_b()
        self.__calculate_newPoints()

    def __x_to_square(self):
        for point in self.__points:
            self.__x_square.append(point.get_x() * point.get_x())
    
    def __x_multiplied_by_y(self):
        for point in self.__points:
            self.__xy.append(point.get_x() * point.get_y())

    def __sum_of_x(self):
        for point in self.__points:
            self.__sum_x += point.get_x()

    def __sum_of_y(self):
        for point in self.__points:
            self.__sum_y += point.get_y()

    def __sum_x_to_square(self):
        for x_square in self.__x_square:
            self.__sum_x_square += x_square

    def __sum_of_xy(self):
        for xy in self.__xy:
            self.__sum_xy += xy

    def __calculate_spole_m(self):
        self.__m = (len(self.__points) * self.__sum_xy - self.__sum_x * self.__sum_y) / (len(self.__points) * self.__sum_x_square - self.__sum_x * self.__sum_x )
        
    def __calculate_intercept_b(self):
        self.__b = (self.__sum_y - self.__m * self.__sum_x ) / len(self.__points)
    
    def __calculate_newPoints(self):
        for point in self.__points :
            self.__new_points.append( Point( point.get_x(), self.__m * point.get_x() + self.__b ) )
            print("Error for x=" + str(point.get_x()) + " and y=" + str(point.get_y()) + " is " + str( abs(point.get_y()-(self.__m * point.get_x() + self.__b))) )
    
    def get_points(self):
        return self.__points

    def get_new_points(self):
        return self.__new_points

    def get_m(self):
        return self.__m

    def get_b(self):
        return self.__b