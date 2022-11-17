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


# root = None
# frm = None
#
#
# def select_phonebook():
#     global root
#     global frm
#     root = Tk()
#     frm = ttk.Frame(root, padding=30)
#     frm.grid()
#     ttk.Label(frm, text="Справочник").grid(column=0, row=0)
#     ttk.Button(frm, text="Имя ", command=print_create_user()).grid(column=0, row=1)
#     ttk.Button(frm, text="Телефон ", command=print_create_phone()).grid(column=0, row=2)
#     ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
#
#     root.mainloop()
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






