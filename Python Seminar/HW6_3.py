# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


nam = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
dic_name = {}

for i in nam:
    n_ = dic_name.get(i[:1], "-")
    if n_ == "-":
        dic_name[i[:1]] = [i]
    else:
        n_ = dic_name.pop(i[:1])
        n_.append(i)
        n_ = sorted(n_)
        dic_name[i[:1]] = n_

print(dic_name)
dic_name = dict(sorted(dic_name.items(), key=lambda x: x[0]))
print(dic_name)
