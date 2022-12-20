# print("qwe")
#
# m = 0
# for i in range(5):
#     n = int(input("Введите число "))
#     if n > m:
#         m = n
# print(f"max {m}")

while True:
    try:
        i = int(input("Input number "))
        print(i*i)
        break
    except:
        print("Я СКАЗАЛ ЧИСЛО!")