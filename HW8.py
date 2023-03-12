# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите количество долек n: "))
m = int(input("Введите количество долек m: "))
k = int(input("Введите количество долек k: "))

if n * m <= k:
    print(n, m, k, "No")
elif n == 1 or m == 1:
    if k <= max(n, m):
        print(n, m, k, "Yes")
    else:
        print(n, m, k, "No")
else: 
    if k % n == 0 or k % m == 0:
        print(n, m, k, "Yes")
    else:
        print(n, m, k, "No")
