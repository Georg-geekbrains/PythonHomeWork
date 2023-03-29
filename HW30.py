# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15




a1 = int(input("Input first array's element: "))
d = int(input("Input difference of element: "))
n = int(input("Input number of elements: "))

prog = [0]*n
prog[0] = a1
for i in range(1,len(prog)):
    prog[i] = prog[i-1] + d
print(prog)
    