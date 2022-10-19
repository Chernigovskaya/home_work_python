# Задача 4. Считайте строковые данные из файла. Создайте словарь, содержащий все символы в файле.

def create_dict():
    data = open('text.txt', encoding='utf-8')
    text = data.read()

    data.close()
    new_dict = {}
    for i in range(0, len(text), 2):
        new_dict[i] = text[i]
    print(new_dict)


create_dict()