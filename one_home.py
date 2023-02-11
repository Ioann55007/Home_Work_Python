import re

my_str = r'\+7\s\d{3}\s\d{3}\-\d{2}\-\d{2}'
my_str_1 = r'\+7\d{10}'
my_str_2 = r'7\s\(\d{3}\)\s\d{3}\s\d{2}\s\d{2}'
my_str_3 = r'7\s\(\d{3}\)\s\d{3}\-\d{2}\-\d{2}'

pr_int = input('Введите номер телефона: ')
ccb = re.findall(my_str_3, pr_int)
bbc = re.findall(my_str_2, pr_int)
oi = re.findall(my_str_1, pr_int)
cv = re.findall(my_str, pr_int)
if oi or cv or bbc or ccb:
    print('IS ok!')
else:
    print('False')
