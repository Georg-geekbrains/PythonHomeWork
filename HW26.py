# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.
# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

x = int(input('Input x: '))
y = int(input('Input y: '))

def recurs(x,y):
    if y <= 0:
        return 1
    else:
        return x * recurs(x,y-1)

print(f'{recurs(x,y)}') 
