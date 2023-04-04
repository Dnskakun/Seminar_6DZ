"""
Дано 20+ значное целое число, проверить его на делимость на 7
Ввод: 234523642345789812354678654323454919865
Вывод: Делится
"""

def divisib_7(tmp_str: str):
    if len(tmp_str) % 3 == 0:
        count = len(tmp_str) // 3
    else:
        count = len(tmp_str) // 3 + 1 
    index:int = 0
    sum_tri: int = 0
    sign: bool = True
    for i in range(count):
        if sign == True:
            sum_tri += int(str_num[-3 - index:len(str_num) - index])
            index += 3
            sign = False
        else:
            sum_tri -= int(str_num[-3 - index:len(str_num) - index])
            index += 3
            sign = True
    if sum_tri % 7 == 0:
        print("Число делится на 7!")
    else:
        print("Число не делится на 7!")



str_num = input("Введите 20+ значное число: ")
divisib_7(str_num)


