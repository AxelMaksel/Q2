# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной 
# последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

import random
n = int(input("Ведите размер списка: "))
ls = []
for i in range(n):
    ls.append(random.randint(0,10))
print(ls)
ls_new = []
for i in ls:
    if ls.count(i) == 1:
        ls_new.append(i)
print(ls_new)
