class Student:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.k = self.PropertyLaptop()

    def cal_student(self):
        print(f'Ноутбук был подарен студентам {self.a, self.b}, с характеристиками: {self.k.show()}')


    class PropertyLaptop:
        def __init__(self):
            self.model = 'HP'
            self.proc = 'i7'
            self.memory = '16GB'

        def show(self):

            message = f"модель ноутбука {self.model}, процессор {self.proc}, и память {self.memory}"
            return message


show_answear = Student('Роману', 'Владимиру')
show_answear.cal_student()
s = show_answear.PropertyLaptop()
s.show()
