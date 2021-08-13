


class Rectangle:
    __width, __height = 0, 0

    def __init__(self,width,height):
        self.__width = width
        self.__height = height
    def area_calc(self):
        area = self.__width * self.__height
        return area
    def circum_calc(self):
        circum = (self.__width + self.__height) * 2
        return circum

