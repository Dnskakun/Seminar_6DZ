"""
Задача 30:  Заполните массив элементами
арифметической прогрессии. Её первый элемент,
разность и количество элементов нужно ввести
с клавиатуры. Формула для получения n-го члена
прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""

def user_input(message, min_elem, max_elem):
    input_error: bool = True
    while input_error:
        try:
            number = int(input(message))
        except:
            print("Вы ввели не число!")
        else:
            if min_elem < number:
                input_error = False
            else:
                print("Вы ввели число, не соответствующее условию!")
    return number

def progression_output(f_element, step, num, index = 0):
    if index == num - 1:
        return print(f_element + step * index, end = ' ')
    else:
        print(f_element + step * index, end = ' ')
        return progression_output(f_element, step, num, index + 1)

first_elem = user_input("Введите первый элемент прогрессии: ", 0, 0)
step_proges = user_input("Введите шаг прогрессии: ", 0, 0)
elements_quantity = user_input("Введите количество элементов: ", 0, 0)

progression_output(first_elem, step_proges, elements_quantity)




