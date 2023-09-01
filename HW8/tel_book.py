# ФУНКЦИЯ ИЗМЕНЕНИЯ ЗАПИСИ
def change_data (old_data, new_data):
    with open ('file.txt', 'r+', encoding = 'utf-8') as data:
        recs = data.readlines()
        # Найти нужную строку в переменной
        for i, line in enumerate(recs):
            if old_data in line:
                recs[i] = new_data + "\n"
                break
        # Переместить указатель на начало файла
        data.seek(0)
        # Записать измененное содержимое обратно в файл
        data.writelines(recs)
        # Обрезать файл до новой длины (если новый размер меньше старого)
        data.truncate()

# ФУНКЦИЯ УДАЛЕНИЯ ЗАПИСИ
def delete_data (del_rec): 
    with open ('file.txt', 'r+', encoding = 'utf-8') as data:
        # Прочитать содержимое файла в переменную
        lines = data.readlines()
        # Удалить нужную запись из переменной
        lines = [line for line in lines if del_rec not in line]
        # Переместить указатель на начало файла
        data.seek(0)
        # Записать измененное содержимое обратно в файл
        data.writelines (lines)
        # Обрезать файл до новой длины (если новый размер меньше старого)
        data.truncate()

# ФУНКЦИЯ СОЗДАНИЯ/СОХРАНЕНИЯ НОВОЙ ЗАПИСИ        
def create_data (recs):
    with open ('file.txt', 'a', encoding = 'utf-8') as data:
        for i, item in enumerate (recs):
            data.write (item + '\n')
    message = "запись создана"
    return message

# ФУНКЦИЯ ПОИСКА ЗАПИСИ
def find_data (key_str):
    string1 = []
    flag = False
    with open ('file.txt', 'r', encoding = 'utf-8') as data:
        for line in data:
            # string1 = line.split()
            # for i, item in enumerate (string1):
            #     if item == key_str:
            #         print (string1)
            #         flag = True
            if key_str in line:
                string1.append (line.split())
                flag = True
        if not flag:
            print ("Данные по Вашим параметрам не найдены")
    return string1

# ФУНКЦИЯ ВЫВОДА НА ЭКРАН ВСЕХ ДАННЫХ
def print_data ():
    with open ('file.txt', 'r', encoding = 'utf-8') as data:
        for line in data:
            print(line)
    message = "Данные выведены на экран"
    return message
  
