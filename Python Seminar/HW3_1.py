# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

from random import sample


def num_list(len_list, number):
    new_list = sample(range(1, len_list * 2), k=len_list)
    return new_list


def sum_list(n_list):
    sum = 0
    for i in range(len(n_list)):
        if (i+1) % 2:
            sum += n_list[i]
    return sum


n = int(input("Введите размер списка "))
q_list = num_list(n, 20)
print(" ".join(map(str, q_list)))
print(f"Сумма нечётных элементов: {sum_list(q_list)}")
