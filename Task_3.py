# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

import random

n = int(input('Enter number of digits n = '))
a = int(input('Enter min value: '))
b = int(input('Enter max value: '))
list_1 = []
for _ in range(1,n+1):
    list_1.append(random.randint(a,b))
print(list_1)
list_2 = []
for i in range(0,n,2):
    list_2.append(list_1[i])
for i in range(1,n,2):
    list_2.append(list_1[i])
print(list_2)
