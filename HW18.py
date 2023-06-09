# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
# Ввод: 10
# Ввод: 7 
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random
n = int(input("Введите количество элементов в массиве: "))
x = int(input("Введите число X: "))
arr = []
for i in range(n):
    arr.append(random.randint(1,n))
print(arr)

min_diff = abs(x - arr[0])
result = arr[0]

for i in range(1, n):
    diff = abs(x - arr[i])
    if diff < min_diff:
        min_diff = diff
        result = arr[i]

print('Ближайший к', x, 'элемент массива:', result)