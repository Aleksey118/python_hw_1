# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.


n = int(input('Enter number: '))
index = 0
while 2 ** index <= n:
    print(2 ** index)
    index += 1