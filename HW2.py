# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

flag = True
while flag:
    n = input("Введите число: ")
    if n.isdigit():
        n = int(n)
        flag = False   
    else:
        print("Вы ввели не число.")
        
m = n
sum = 0
while n > 0:
    x =  n % 10
    sum += x
    n = n//10
print(f'Сумма цифр числа {m} равна {sum}')

