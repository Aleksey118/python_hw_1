# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые –
# гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Enter coins number: '))
head_coins = 0
tail_coins = 0
for i in range(n):
    head_or_tail = int(input(f'{i}:  '))
    if head_or_tail == 0:
        head_coins += 1
    else:
        tail_coins += 1
if head_coins > tail_coins:
    print(tail_coins)
else:
    print(head_coins)