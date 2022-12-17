# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random
number_list = list(range(10))
print(number_list)
for i in range(len(number_list)):
    n=number_list.pop(i)
    number_list.insert(random.randint(1,len(number_list)),n)
print(number_list)