"""
1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки и
сохраните в переменные, затем выведите на экран.
2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
while и арифметические операции.
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите
численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен
увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня, на который результат спортсмена
составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
"""


# 1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки
# и сохраните в переменные, затем выведите на экран.
def variables_function():
    a = 152
    b = 3.4
    print('Переменная a = %d' % a)
    print('Переменная b = %f' % b)
    c = int(input('Введите целое число: '))
    d = float(input('Введите вещественное число: '))
    string1 = input('Введите строку: ')
    print('Переменная c = %d' % c)
    print('Переменная d = %f' % d)
    print('Строка string1: %s' % string1)


# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

def time_convert():
    sec = int(input('Введите время в секундах: '))
    hour = sec // 3600
    minutes = (sec - hour * 3600) // 60
    seconds = sec - hour * 3600 - minutes * 60
    print('%d:%02d:%2d' % (hour, minutes, seconds))


# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
def digits_player():
    n = int(input('Введите число: '))
    first = int(str(n))
    second = int(str(n)+str(n))
    third = int(str(n) + str(n) + str(n))
    print(first+second+third)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.
def find_max_digit():
    n = int(input('Введите целое положительное число: '))
    max = 0
    while n > 0:
        c = int(n % 10)
        if max < c:
            max = c
        n //= 10
    print(max)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
def economics_1():
    vir = int(input('Введите выручку: '))
    izd = int(input('Введите издержки: '))
    pribil = vir - izd

    if pribil > 0:
        print ('Фирма работает с прибылью')
    else:
        print ('Фирма работает в убыток')

# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
def economics_2():
    vir = float(input('Введите выручку: '))
    izd = float(input('Введите издержки: '))
    pribil = vir - izd
    if pribil > 0:
        rent = pribil / vir
        print('Рентабельность: %.2f %%' % (rent * 100))
        chislennost = int(input('Введите численность сотрудников: '))
        print (f'Прибыль фирмы в рассчете на одного сотрудника: {pribil / chislennost} р.')
    else:
        print ('Фирма работает в убыток')

# 7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен
# увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня, на который результат спортсмена
# составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

def sport():
    a = float(input('Введите a:'))
    b = int(input('Введите b:'))
    n = 0
    while True:
        n +=1
        if a>=b:
            print(f'На {n} день спортсмен достиг результата - не менее {b} км')
            return
        a += 0.1*a


