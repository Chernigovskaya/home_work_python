from model import create_dic


def writing_xml():
    user = create_dic()
    with open('phonebook.xml', 'a', encoding='utf_8') as data:
        data.write(f'{user}\n')


