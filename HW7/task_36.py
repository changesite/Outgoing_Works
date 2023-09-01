# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**

def print_operation_table (operation, num_rows, num_columns):
    
    for index1 in range (1,num_rows+1):
        line = []
        for index2 in range (1,num_columns+1):
            if index1 == 1:
                line.append (index2) # формируем первую строку из чисел по порядку
            else:
                if index2 == 1:
                    line.append (index1) # формируем первый столбец по порядку
                else:
                    line.append (operation (index1, index2)) # формируем основные элементы таблицы по загруженной формуле
        print (line)


print_operation_table(lambda x, y: x * y, 6, 6)
