from tkinter import *
from tkinter import ttk


def create_user():
    user = []
    name = input('Введите имя: ')
    user.append(name)
    return user


def create_phone():
    phone = []
    phone_num = input('Введите номер телефонa: ')
    phone.append(phone_num)
    return phone


def add_contact():
    create_user()
    create_phone()




# def select_phonebook():
#     global root
#     global frm
#     root = Tk()
#
#     button_add_contact = Button(root, text="Добавить контакт ", command=add_contact)
#     button_add_contact.grid(row=4, column=0, columnspan=2)
#
#     label_name = Label(root, text='Введите имя')
#     label_name.grid(row=0, column=0)
#     label_surname = Label(root, text='Введите фамилию')
#     label_surname.grid(row=1, column=0)
#     label_phone = Label(root, text='Введите телефон')
#     label_phone.grid(row=2, column=0)


    # ttk.Button(frm, text="Телефон ", command=print_create_phone()).grid(column=0, row=2)
    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)

root = Tk()
root.geometry('300x200')

button_add_contact = Button(root, text="Добавить контакт ", command=add_contact)
button_add_contact.grid(row=4, column=0, columnspan=2)

label_name = Label(root, text='Введите имя')
label_name.grid(row=0, column=0)
label_surname = Label(root, text='Введите фамилию')
label_surname.grid(row=1, column=0)
label_phone = Label(root, text='Введите телефон')
label_phone.grid(row=2, column=0)

# entry_name = Entry(root, width=15)
# entry_name.grid(row=0, column=0)
# entry_surname = Entry(root, width=15)
# entry_surname.grid(row=1, column=0)
# entry_phone = Entry(root, width=15)
# entry_phone.grid(row=2, column=0)

root.mainloop()
#
#
# def print_create_user():
#     global frm
#     ttk.Label(frm, text=f'{create_user}').grid(column=1, row=1)
#
#
# def print_create_phone():
#     global frm
#     ttk.Label(frm, text=f'{create_phone}').grid(column=1, row=1)






