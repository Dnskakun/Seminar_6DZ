"""
Даны числа a и b. Определите, сколько существует
последовательностей из a нулей и b единиц, в
которых никакие два нуля не стоят рядом.
Ввод 5 8
Вывод 126
"""

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

def find_quantity(a: int, b: int):
    if a == 0: return 1
    if a == 1: return b + 1
    if a > 1 and b == 0: return 0
    return find_quantity(a - 1, b - 1) + find_quantity(a, b - 1)

num_a = user_input("Введите количество нулей: ", 1, 1000)
num_b = user_input("Введите количество единиц: ", 1, 1000)

print(find_quantity(num_a, num_b))

