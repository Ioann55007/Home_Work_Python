class Account:
    rate_us = 0.013
    rate_eur = 0.011
    sufix = 'RUB'
    sufix_usd = 'USD'
    sufix_er = 'EUR'
    commission = 5


    def __init__(self, num, surname, percent, value=0):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f"Счёт #{self.num} принадлежащий {self.surname} был открыт")
        print("*" * 50)

    def __del__(self):
        print(f'Счёт владельца {self.surname} закрыт')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    @staticmethod
    def give_commission():
        return Account.commission


    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_us)
        usd_vale = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счёта: {usd_val}{Account.sufix}.")
        print(f"Состояние счёта: {usd_vale}{Account.sufix_usd}.")

    def print_balanc(self):
        print(f'Текущий баланс {self.value}{Account.sufix}')

    def print_info(self):
        print('Инфа о счёте')
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balanc()
        print(f'Процент: {self.percent:.0%}')
        print('-' * 20)

    def edit_owner(self, surname):
        self.surname = surname

    def add_percent(self):
        self.value += self.value * self.percent
        print('Проценты начислены!')
        self.print_balanc()


    def with_drow_many(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет заданной суммы  денег {val}{Account.sufix}")


        else:
            print(f'Ваша коммиссия: {self.give_commission()}%')
            print_commission = (self.value / 100) * self.give_commission()
            val -= print_commission
            self.value -= val
            print(f"{val}{Account.sufix} было успешно снято!")
        self.print_balanc()

    def add_many(self, val):
        self.value += val
        print(f"{val}{Account.sufix} было успешно добавлено!")
        self.print_balanc()


account = Account('12345', 'Долгих', 0.03, 1000)
account.print_info()
account.convert_to_usd()
account.edit_owner('Дима')
account.print_info()
account.add_percent()
print()
account.with_drow_many(100)
account.add_many(5000)
account.with_drow_many(2000)






