# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# ФУНКЦИИ ИЗМЕНЕНИЯ ЗАПИСИ change_data И УДАЛЕНИЯ ЗАПИСИ delete_data, находятся в модуле  tel_book.py

from tel_book import create_data, print_data, find_data, change_data, delete_data

print ("Добро пожаловать в телефонный справочник")

while True:
    print ()
    print ("Чтобы добавить запись - нажмите 1")
    print ("чтобы найти запись - нажмите 2")
    print ("чтобы вывести все данные на экран - нажмите 3")
    print ("чтобы изменить запись - нажмите 4")
    print ("чтобы удалить запись - нажмите 5")
    string = int (input ("чтобы окончить работу с программой - нажмите 6: "))
    print ()

    if string == 1:
        flag = True
        string1 = 0
        rec = []
        while flag == True:
            line = input ("Ведите Фамилию Имя Отчество и Телефон абонента через пробел: ")
            rec.append (line)
            print (rec)      
            string1 = int (input("Если желаете добавить еще запись нажмите 1, иначе 0:"))
            if string1 == 0:
                flag = False
        print (create_data (rec))
        
    elif string == 2:
        print ("ищем")
        string1 = (input("Введите данные для поиска:"))
        print ()
        print (find_data (string1))

    elif string == 3:
        print ("")
        print ("Выводим все данные")
        print ("")
        print_data()

    elif string == 4:
        print ()
        old_str = input ("Введите данные, которые хотите изменить: ")
        new_str = input ("Введите измененные данные: ")
        print ()
        change_data (old_str, new_str)
        
    elif string == 5:
        print ()
        del_str = input ("Введите запись, которую хотите удалить: ")
        delete_data (del_str)
        
    elif string == 6:
        break
    else:
        print ("Такой команды не существует")
