# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def progress_list (first_el, d, num):
    res_list = []
    for i in range (1, num + 1):
        res_list.append(first_el + (i-1)*d)
    return res_list

in_list = list (map(int, input('Введите первый элемент, разность b количество элементов прогрессии через пробел: ').split()))
first_num = l_num = dd = 0
for i, item in enumerate (in_list):
    if i == 0:
        first_num = item
    elif i == 1:
        dd = item
    elif i == 2:
        l_num = item

print ("Прогрессия: ", progress_list (first_num, dd, l_num))
