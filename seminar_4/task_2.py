# Задача 2. Актёров разделили на списки по трём качествам «умные», «красивые», «сильные».
# На главную роль нужен актёр обладающий всеми тремя качествами. Определите, сколько есть претендентов на главную роль.
# Списки актёров поместите в соответствующие файлы.

handsome = {'Илья', 'Федор', 'Семен', 'Олег', 'Лев', 'Антон', 'Артем', 'Боря', 'Стас', 'Марк', 'Ян'}
smart = {'Илья', 'Георгий', 'Лев', 'Демьян', 'Антон', 'Владислав', 'Боря', 'Стас', 'Марк', 'Влад'}
strong = {'Федор', 'Георгий', 'Олег', 'Демьян', 'Артем', 'Елисей', 'Боря', 'Стас', 'Влад'}
res = handsome & smart & strong
print(res)


# def openFile(nameFile):
#     f = open(nameFile, encoding='utf-8')
#     phrase = f.readlines()
#     f.close()
#     list_n = phrase[0].split()
#     return set(list_n)
#
#
# beauty = openFile('beauty.txt')
# strong = openFile('strong.txt')
# smart = openFile('smart.txt')
#
# print(beauty.intersection(smart).intersection(strong))