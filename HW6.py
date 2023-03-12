# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# .
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета
#  385916 -> yes
# 123456 -> no

# flag = True
# while flag:
#     tiket = input('Введите число: ')
#     if tiket.isdigit():
#         flag = False
#         tiket = int(tiket)
#     else:
#         print('Это не число')

# i = 0
# n = tiket
# while n > 0:
#     n = n // 10
#     i = i + 1
# count = i

# print(count, tiket)
# tiket = str(tiket)
# print(len(tiket))
# if count % 2 == 0:
flag = True
while flag:
    ticket = input('Введите число: ')
    if ticket.isdigit():
        flag = False
    else: print('Это не число')

count = len(ticket)
if count % 2 == 0:
    n = int(count/2)
    first = int(ticket[:n])
    second = int(ticket[-n:]) # если нет указываю тип, выдает ошибку TypeError: not all arguments converted during string formatting
sum1 = 0
x = 0
while first > 0:
    x = first % 10
    sum1 += x
    first = first // 10
print(sum1)
sum2 = 0
y = 0
while second > 0:
    y = second % 10
    sum2 += y
    second = second // 10
print(sum2)
if sum1 == sum2:
    print(ticket, '- Счатливый билет')
else:
    print('Купите еще один билет')

