# * 4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь,
# ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"

# out

# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']}, 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}, 'В': {'Ю': ['Юнона Ветрякова']}}


def Sort_Fam(ls):
    dic_ = {}
    for i in ls:
        nf = i.split()
        n_ = dic_.get(nf[1][:1], "-")
        # print(i, nf, n_)
        if n_ == "-":
            dic_[nf[1][:1]] = [i]
        else:
            n_ = dic_.pop(nf[1][:1])
            n_.append(i)
            n_ = sorted(n_)
            dic_[nf[1][:1]] = n_
    return dic_


def Sort_Name(ls):
    # print(ls)
    dic_ = {}
    k = ls.keys()
    for i in k:
        dic_st = {}
        # print("key i", i, ls[i])
        for i2 in ls[i]:
            # print("i2", i2)
            n_ = dic_st.get(i2[:1], "-")
            if n_ == "-":
                dic_st[i2[:1]] = [i2]
            else:
                n_ = dic_st.pop(i2[:1])
                n_.append(i2)
                n_ = sorted(n_)
                dic_st[i2[:1]] = n_
        # print(dic_st)
        dic_[i]=dic_st
    return dic_


nam_fam = ["Иван Сергеев", "Инна Серова", "Петр Алексеев",
           "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
           "Борис Аркадьев", "Антон Серов", "Павел Анисимов"]

dic_name = {}
# dic_fam = {}

dic_fam = Sort_Fam(nam_fam)
dic_name = Sort_Name(dic_fam)
# print(dic_fam)
print()
print(dic_name)