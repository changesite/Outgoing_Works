# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
N = int(input("Введите число N: "))
dvoika = 2
deg = 2
while dvoika <= N:
    print(dvoika)
    dvoika = 2**deg
    deg += 1
    