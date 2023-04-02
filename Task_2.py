"""
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше
заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Диапазон от 6 до 12
Вывод: [1, 9, 13, 14, 19]
"""
from random import randint

def user_input(message, min_elem, max_elem):
    input_error: bool = True
    while input_error:
        try:
            number = int(input(message))
        except:
            print("Вы ввели не число!")
        else:
            if min_elem <= number <= max_elem:
                input_error = False
            else:
                print("Вы ввели число, не соответствующее условию!")
    return number

def find_index(list_tmp, low_tmp, up_tmp):
    print(list_tmp)
    print('[', end = ' ')
    for i in range(len(list_tmp)):
        if low_tmp <= list_tmp[i] <= up_tmp:
            print(i, end = ' ')
    print(']')


number_elements = user_input("Введите количество элементов массива: ", 1, 1000)
list_elements = [randint(0, 99) for i in range(number_elements)]
lower_bound = user_input("Введите нижнюю границу диапазона (от 1 до 50): ", 1, 50)
upper_bound = user_input("Введите верхнюю границу диапазона (от 50 до 99): ", 50, 99)

find_index(list_elements, lower_bound, upper_bound)



