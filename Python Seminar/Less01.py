# m = 0
# for i in range(5):
#     n = int(input("Введите число "))
#     if n>m:
#         m=n
# print(f"max {m}")


# def pri(n):
#     print(list(range(-n, n+1)))
#     print(*range(-n, n+1))


# m = int(input("Введите число "))
# pri(m)

# m = float(input("Введите число "))
# print(type(m),m)


# m = int(input("Введите число "))
# if (m % 5 == 0 and m % 10 == 0 or m % 15 == 0) and m % 30 != 0:
#     print(m, 'Yes')
# else:
#     print(m, 'No!')


# 6. Пример проверки ложности утверждения (x ≡ z ) ∨ (x → (y ∧ z))

# print("x y z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not (x == z or x <= y and z):
#                 print(x, y, z)


print(round(92 ** 0.5, 3))
print(f"{92 ** 0.5:.3f}")
