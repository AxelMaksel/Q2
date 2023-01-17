from random import sample


def Create(n):
    ls = "абв"
    n_list = []
    for i in range(n):
        t = sample(ls, 3)
        a = "".join(t)
        n_list.append(a)
    return (" ".join(n_list))


def DelWord(ls):
    n_list = ls.split()
    t_list = []
    # for i in n_list:
    #     t_list = [n for n in n_list if n != "абв"]
    t_list = list(filter(lambda x: x != 'абв', n_list))
    return (" ".join(t_list))


num = int(input("Введите размер предложения: "))
if num > 0:
    m_list = Create(num)
    print("Исхдная строка:", m_list+"\n")
    new_list = DelWord(m_list)
    if m_list == new_list:
        print("*"*50, "** Не нашёл! что можно удалить **", "*"*50)
    print("список без 'абв':", new_list)

else:
    print("Error!")
