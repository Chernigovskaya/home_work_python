from view import create_user, create_phone


def create_dic():
    data = dict(zip(create_user(), create_phone()))
    return data


def find_user():
    # find_n = input('Ввудите имя человека: ')
    result = {}
    with open('phonebook.xml', 'r') as data:
        lines = data.read().splitlines()
        for line in lines:
            key, value = line.split(': ')
            result.update({key: value})
    print(result)

    
    # if result[key] == find_n:
    #     print(result[value])



find_user()
