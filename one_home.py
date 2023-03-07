class Pair:
    def __init__(self, a, b):
        self.A = a
        self.B = b

    def multiple_pair(self):
        print('Произведение чисел:')
        return self.A * self.B

    def sum_pair(self):
        print('Сумма:')
        return self.A + self.B


pt = Pair(17, 32)
print(pt.sum_pair())
print(pt.multiple_pair())


class RightTriangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_method(self):
        f = self.a ** 2 + self.b ** 2
        print(f'Выводим гипотенузу треугольника: {f}')
        return f

    def square_method(self):
        g = (self.a * self.b) // 2
        print(f'Выводим площадь треугольника: {g}')
        return g

    def print_methods(self):
        c = f' Прямоугольный треугольник с гипотенузой : {self.my_method()} и площадью: {self.square_method()} задан'
        return c


o = RightTriangle(10, 20)
# print(o.my_method())
# print(o.square_method())
print(o.print_methods())


class Parent:
    def __init__(self, sx):
        self.sx = sx


class Sun(Parent):


    def func_sun(self, x):
        d = f"Возвращаем: {self.sx, x}"
        return d


o = Sun(Parent(120))
print(o)
print(o.func_sun(2))
po = Sun(120)
print(po.func_sun(19))


class Parent:
    def __init__(self, sx):
        self.sx = sx


#
class Sun(Parent):

    def __init__(self, sx, v):
        self.v = v
        self.sx = sx
        super().__init__(self)

    def op(self, a, b):
        self.sx = a
        self.v = b
        ret = f"Выводим {a, b}"
        return ret


oop = Sun(Parent(120), 2)
print(oop.op(120, 12))


