# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]


from random import sample


def num_list(len_list, number):
    new_list = sample(range(1, len_list * 2), k=len_list)
    return new_list


def composition_list(n_list):
    comp_list = []
    for i in range(len(n_list) // 2):
        comp_list.append(n_list[i]*n_list[-i-1])
    if len(n_list) % 2:
        comp_list.append(n_list[len(n_list) // 2])
    return comp_list


n = int(input("Введите размер списка "))
q_list = num_list(n, 20)
print(" ".join(map(str, q_list)))
print("\nОбработанный список:")
print(" ".join(map(str, composition_list(q_list))))
