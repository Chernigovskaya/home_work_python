
def read_last_row():
    data = open('text.txt', encoding='UTF-8')
    text = data.readlines()
    print(text[-1])
    data.close()



