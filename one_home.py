class Car:
    def __init__(self, name_model, year_of_issue, manufacturer, power_engine, colored_car, price):
        self.name_model = name_model
        self.year_of_issue = year_of_issue
        self.manufacturer = manufacturer
        self.power_engine = power_engine
        self.colored_car = colored_car
        self.price = price

    def set_car(self):
        print('Установите: ', self.name_model, self.year_of_issue, self.manufacturer, self.power_engine,
              self.colored_car,
              self.price)

    def get_data(self):
        data_car = (
            'Автомобиль марки - ', self.name_model, 'года выпуска -', self.year_of_issue, 'производителя - ',
            self.manufacturer,
            'мощностью двигателя - ', self.power_engine, 'цвета - ', self.colored_car, 'стоимость - ', self.price)

        return data_car


new_my_car = Car('БМВ,', '2017,', 'Германия,', '2100 лошадинных сил,', 'чёрного,', '10000 $')
new_my_car.set_car()
car_nw = new_my_car.get_data()
print(car_nw)
g = new_my_car.colored_car
r = new_my_car.power_engine
rg = new_my_car.price
print(g, r, rg)



