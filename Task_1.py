# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

a = input('Enter valid number: ')

list_1 = []
for i in range(len(a)):
    list_1.append(a[i])
print(list_1)

summ = 0
for i in list_1:
    if i.isdigit(): 
        summ+=int(i)
print(summ)
