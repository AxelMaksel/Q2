# ** 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# in
# 10 True

# out

# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый', 'город позавчера утопичный']

# in
# 10 False

# ['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый',
# 'город вчера утопичный', 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый',
# 'огонь позавчера яркий', 'огонь где-то утопичный', 'автомобиль где-то мягкий']

import random


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра",
           "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def Conct(a, b, c):
    return " ".join([a, b, c])


def Gen_Smile(a, b, c):
    return [Conct(x, y, z) for x in nouns for y in adverbs for z in adjectives]


def Gen_Smile_Unlim(a, b, c, nu):
    lst_ = []
    while nu > 0:
        lst_.append(" ".join([random.choice(nouns), random.choice(adverbs), random.choice(adjectives)]))
        nu -= 1
    return lst_


inp = input(
    "Введите сколько шуток нужно? Уникальность шуток (20, True[False]): ")
n, s = inp.split(", ")
num = int(n)
if num > 0:
    if s == "True":
        ls = Gen_Smile(nouns, adverbs, adjectives)
        lst = random.choices(ls, k=num) if len(ls) >= num else print("У нас нет столько шуток в запасе")
    else:
        lst = Gen_Smile_Unlim(nouns, adverbs, adjectives,num)
        print()

print(lst)
