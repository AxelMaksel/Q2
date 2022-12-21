# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36


import random


def num_list(number):
    my_list = []
    while number > 0:
        my_list.append(round(random.uniform(1, 10), 2))
        number -= 1
    return my_list

def search_min_max(my_list):
    min,max=99,0
    for i in my_list:
        n=round(i-int(i),2)
        if n<min:
            min=n
        if n>max:
            max=n
    return min,max


n = int(input("Введите размер списка "))
q_list = num_list(n)
print(q_list)
min,max=search_min_max(q_list)
print(f"min {min}, max {max}, а их разница:{max-min}")
# print(f"Сумма нечётных элементов: {sum_list(q_list)}")
