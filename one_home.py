with open('my_homework_file.txt', 'w+') as home_file:
    home_file.write('Заменить строки в текстовом файле; \nизменить строку в списке; \nзаписать список в файл')

hom_fil = open('my_homework_file.txt', 'r')
read_file = hom_fil.readlines()
print(read_file)
x_file = read_file[0]
read_file[0] = read_file[1]
read_file[1] = x_file
print(read_file)
read_file[0] = 'Изменить строку толь ко одну'
print(read_file)
last_file = open('my_homework_file.txt', 'w')
last_file.writelines(read_file)
last_file.close()


with open('my_homework.txt', 'w+') as home_file:
    home_file.write('Заменить строки в текстовом файле; \nизменить строку в списке; \nзаписать список в файл')

f = open('my_homework.txt', 'r')
reading_file = f.readlines()
print(reading_file)

reading_file.reverse()
print(reading_file)


a_d = 'my_homework_file.txt'
d_a = 'my_homework.txt'

with open(a_d, 'r') as f, open(d_a, 'r') as fi:
    new = f.read(), fi.read()
    print(new)

print(new)
fo = open('threefile.txt', 'w+')
fo.writelines(new)
fo.close()

