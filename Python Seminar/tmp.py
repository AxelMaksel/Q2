# print("qwe")
#
# m = 0
# for i in range(5):
#     n = int(input("Введите число "))
#     if n > m:
#         m = n
# print(f"max {m}")

# while True:
#     try:
#         i = int(input("Input number "))
#         print(i*i)
#         break
#     except:
#         print("Я СКАЗАЛ ЧИСЛО!")

l = {"a": 1, 2: 4}
for i, o in enumerate(l):
    print(i, o, l[o])

i = [f"{i}" for i in range(1, 8)]
print(i)


def f(ii):
    ii = int(ii)
    if ii % 2:
        return 1
    return 0


q = list(map(lambda x: int(x)*3, i))
print(q)
