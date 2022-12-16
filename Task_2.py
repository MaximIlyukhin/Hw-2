# Задайте список из n чисел последовательности (1 + 1/n)^n, 
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Enter number n = '))
list_1 = []
summ = 0
count = 0
for i in range(1,n+1):
    summ+=(1+1/i)**i
    count = (1+1/i)**i
    list_1.append(round(count,2))
print(f'Для n = {n} -> {list_1}')
print(f'Сумма = {round(summ,2)}')   
