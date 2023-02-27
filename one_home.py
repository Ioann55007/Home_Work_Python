import math
from math import pi


class Sphere:

    def __init__(self, get_square, set_radius, get_volume, set_center, get_center, get_radius, is_point_inside):
        self.get_volume = get_volume
        self.get_square = get_square
        self.get_radius = get_radius
        self.get_center = get_center
        self.set_radius = set_radius
        self.get_radius = get_radius
        self.set_center = set_center
        self.is_point_inside = is_point_inside


    @property
    def get_sphere(self):
        self.get_square = 4 * pi * self.set_radius ** 2
        self.get_volume = 4 / 3 * (pi * self.set_radius ** 3)
        get_square = ('Выводим площадь сферы: ', self.get_square)
        get_volume = ('Выводим обьём шара: ', self.get_volume)
        self.get_center = self.set_center
        get_center = ("Выводим центр сферы: ", self.get_center)
        self.get_radius = self.set_radius
        get_radius = ('Выводим радиус сферы ', self.get_radius)

        return get_square, get_volume, get_center, get_radius

    @get_sphere.setter
    def get_sphere(self, value):
        self.set_radius = value

        self.set_center = value

    def point_inside(self, x, y, z):

        if math.sqrt((x - x) ** 2 + (y - y) ** 2 + (z - z) ** 2) <= self.set_radius:

            return True
        else:
            return False


t = 12, 32, 11
oz = Sphere(None, 18, None, t, None, None, None)
print(oz.get_sphere)
print(oz.point_inside(12, 13, 444))
print('Радиус сферы установлен в значении: ', oz.set_radius)


