a = [1, 15, 66]
b = [22, 33, 15]
d = [5, 6799]
e = [14, 44, 999]
c = [a, b, d, e]
p = c[0]
t = c[1]
p_1 = c[2]
p_2 = c[3]
r = *p, *t, *p_1, *p_2
last_list = list(r)
print(last_list)

user_entered = int(input('Введите число сортировки, если 1 - по возрастанию, 2 - по убыванию: '))

if user_entered == 1:
    last_list.sort()
    print(last_list)
elif user_entered == 2:
    last_list.sort(reverse=True)
    print(last_list)


def sequential_search(x, y):
    element__position = 0
    while element__position < len(x):
        if x[element__position] == y:
            function_print = 'Ваш выбор был: ', y
            return function_print

        elif x[element__position] != y:
            print('Вы ввели несуществующий элемент списка')
            break
        else:
            element__position += 1


user_choices = int(input('Введите искомый элемент: '))
print(sequential_search(last_list, user_choices))








