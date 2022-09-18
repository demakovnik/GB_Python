import os
from statistics import mean
import re
import json


# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных будет свидетельствовать пустая строка.

def strings_to_file():
    if not os.path.exists("lessons/output_files"):
        os.mkdir("lessons/output_files")
    with open("lessons/output_files/first_task.txt", "w") as f_obj:
        while True:
            str = input()
            if str == "":
                break
            print(str, file=f_obj)


# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
def readingFile():
    try:
        with open("lessons/input_files/test.txt") as f_obj:
            strings = f_obj.readlines()
            count_string = len(strings)
            words = {}
            i = 1
            print(f'Количество строк: {count_string}')
            for str in strings:
                print(f'Количество слов в {i} строке: {len(str.split())}')
                i += 1

    except IOError:
        print("Ошибка ввода/вывода")


# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней
# величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

def less_than_20():
    try:
        with open("lessons/input_files/salary.txt") as f_obj:
            dict = {}
            for string in f_obj.readlines():
                arr = string.split()
                surname, salary = arr[0], float(arr[1])
                dict[surname] = salary
            less = [k for k, v in dict.items() if v < 20000.00]
            print(f'Средняя зарплата: {mean(dict.values())}')
            print(f'Зарплата меньше 20000: {less}')

    except IOError:
        print("Ошибка ввода/вывода")


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

def numerals():
    nums = {}
    splitter = ' — '
    russian = ('Один', 'Два', 'Три', 'Четыре')
    try:
        with open("lessons/input_files/numerals.txt") as f_obj:
            for string in f_obj.readlines():
                arr = string.split(splitter)
                numeral, meaning = arr[0], int(arr[1])
                nums[meaning] = russian[meaning - 1]
        if not os.path.exists("lessons/output_files"):
            os.mkdir("lessons/output_files")

        with open("lessons/output_files/numerals.txt", "w") as f_obj:
            for string in [f'{v}{splitter}{k}' for k, v in nums.items()]:
                print(string, file=f_obj)
    except IOError:
        print("Ошибка ввода/вывода")
    except IndexError:
        print("Ошибка ввода/вывода")


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить её на экран.

def summator(numbers):
    if not os.path.exists("lessons/output_files"):
        os.mkdir("lessons/output_files")
    with open("lessons/output_files/summa.txt", "w+") as f_obj:
        for n in numbers:
            print(n, file=f_obj, end=' ')
        f_obj.seek(0)
        print(f'Summa = {sum([float(n) for n in f_obj.readline().split()])}')


# 6 (Дополнительно). Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def lessons():
    result = {}
    splitter = ':'
    try:
        with open("lessons/input_files/task6.txt") as f_obj:
            for str in f_obj.readlines():
                name, ss = str.split(splitter)
                result[name] = sum([int(s) for s in re.findall(r'-?\d+\.?\d*', ss)])
        return result
    except IOError:
        print("Ошибка ввода/вывода")
    except IndexError:
        print("Ошибка ввода/вывода")


# 7 (Дополнительно) . Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
def firms_calculate():
    firms = {}
    try:
        with open("lessons/input_files/firms.txt") as f_obj:
            for firm in f_obj.readlines():
                name, ownership, proceeds, costs = firm.split()
                firms[name] = int(proceeds) - int(costs)
        average_profit = {'average_profit': mean([v for k, v in firms.items() if v >= 0])}

        if not os.path.exists("lessons/output_files"):
            os.mkdir("lessons/output_files")

        with open("lessons/output_files/firms.txt", "w") as write_f:
            json.dump([firms, average_profit], write_f)
    except IOError:
        print("Ошибка ввода/вывода")
    except IndexError:
        print("Ошибка ввода/вывода")
