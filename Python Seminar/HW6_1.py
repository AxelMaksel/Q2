# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
# предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

import random
import itertools


def GenerList(n, min=0, max=30):
    return list(random.choices(range(min, max+1), k=num))


num = int(input("Размер списка: "))
sm = GenerList(num)
print(sm)
sm2=[sm[x] for x in range(1,len(sm)) if sm[x]>sm[x-1] ]
print(sm2)
