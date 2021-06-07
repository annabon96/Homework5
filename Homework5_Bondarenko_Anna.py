#Задание 1
#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
my_text = open('my_text.txt', 'w', encoding='utf-8')
str_list = input("Введите текст: ")
my_text.writelines(str_list)
my_text.close()

#Задание 2
#Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
my_list = ['1\n', '22\n', '333\n']
with open("test_2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("test_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")

#Задание 3
 #Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open('persons.txt', 'r') as my_file:
    salary = []
    surname = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           surname.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 {surname}, средний оклад {sum(map(int, salary)) / len(salary)}')

# Задание 4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в
# новый текстовый файл.

with open('numbers.txt', 'r', encoding='utf-8') as my_file:
    my_text = [item.replace('\n', '') for item in my_file.readlines()]
    new_list = [item.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре') for item in my_text]
    print(new_list)

with open('text.txt', 'w', encoding='utf-8') as new_file:
    new_file.writelines(new_list)

# Задание 5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open('number_file.txt', 'w', encoding='utf-8') as new_file:
    num_list = ['1 2 3 4 5 6 7 8 9']
    new_file.writelines(num_list)

with open('number_file.txt', 'r', encoding='utf-8') as new_2file:
    num = new_2file.readlines()[0]
    new_2list = [int(i) for i in num.split()]
    print(sum(new_2list))

# Задание 6
# -

# Задание 7
# -
