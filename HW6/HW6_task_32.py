# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

def index_element (list_num, l_board, h_board):
    list_res = []
    for i, item in enumerate (list_num):
        if l_board <= item <= h_board:
            list_res.append (i)
    return list_res


n_list = int (input ("Введите количество элементов массива': "))
low_b = int (input ("Введите нижнюю границу диапазона': "))
high_b = int (input ("Введите верхнюю границу диапазона': "))
list_1 = [ random.randint(-99,99) for item in range (n_list)] # формируем массив элементов
print (list_1)

res = index_element (list_1, low_b, high_b)
if len(res) == 0:
    print ("В массиве нет элементов из указанного диапазона")
else:
    print ("Индексы элементов массива из нашего диапазона: ", res)
