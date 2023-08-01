# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на
# них выросло различное число ягод — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена
# система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих
# модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды
# с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод, которое
# может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# ПРОГРАММА НАХОДИТ САМУЮ ПЛОДОНОСНУЮ КОМБИНАЦИЮ ИЗ 3 КУСТОВ, С УКАЗАНИЕМ НОМЕРА ЦЕНТРАЛЬНОГО ИЗ НИХ И КОЛИЧЕСТВА ЯГОД.

import random
n_bush = int (input ("Введите количество кустов черники на грядке: "))
list_1 = [ random.randint(1,30) for item in range (n_bush)] # формируем множество N кустов с количеством ягод на каждом от 1 до 30
print (list_1)
max_berry = sum = 0
index_res = 1
for index in range (len(list_1)):
    sum = list_1 [index] + list_1 [index-1] + list_1 [index-2]  # сумма ягод с 3-х ближайших кустов
    if sum > max_berry:
        max_berry = sum
        index_res = index
#        print (index_res)
if index_res == 0:
    index_res = n_bush
print ("Максимальное количество ягод: ", max_berry, "штук, можно собрать находясь перед: ", index_res, "кустом")
