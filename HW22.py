# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

n = int(input("input numbers first set: "))
m = int(input("Input numbers second set: "))
arrN = []
arrM = []
for i in range(n+1):
    arrN.append(random.randint(1,n))
for i in range(m+1):
    arrM.append(random.randint(1,m))
lotN = set(arrN) 
lotM = set(arrM)   
i = lotN.intersection(lotM)

print(arrN)
print(arrM)
print(i)


