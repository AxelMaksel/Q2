# # def sys(simbol, count=3):
# #     return simbol*count


# # print(sys("q", 5))


# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←
# print(dictionary['up'])   # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐=='
# print(dictionary['left'])  # ⇐
# #print(dictionary['type'])  # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))


with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

colors = ['red', 'green', 'blue']
data = open('file2.txt', 'a')
data.writelines(colors) # разделителей не будет
data.close()
path = 'file.txt'
data = open(path, 'r')
for line in data:  
    print(line)
data.close()
