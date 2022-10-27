# Задача 2. В зоопарк отправили отчёт о новом поступлении зверей с ошибкой, в результате которой некоторые данные не расшифровались.
# Расшифруйте данные. Определите, в какой клетке находится лев. Номер клетки совпадает с номером строки.

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def convert_to_binary(num):
    result = ''
    while num > 0:
        result = str(num%2) + result
        num = num//2
    return result


code_list = [int(i) for i in range(len(alphabet))]
print(code_list)


code_list = [convert_to_binary(i) for i in code_list]
print(code_list)

code_list = ['0'* (6-len(i)) + i for i in code_list]
print(code_list)
dictionary = {}
for i in range(len(code_list)):
    dictionary[code_list[i]] = alphabet[i]
print(dictionary)

data = open('animals.txt', 'r')
animalCodeList = data.readlines()
data.close()

for animal in animalCodeList:
    for i in range(len(animal)//6):
        bias = i * 6
        print(dictionary[animal[bias:bias+6]], end="")
    print()
