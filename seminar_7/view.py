from model import time_new_year
from tkinter import *
from tkinter import ttk


root = None
frm = None


def create_menu():
    global root
    global frm
    root = Tk()
    frm = ttk.Frame(root, padding=30)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Дни до Нового года", command=print_result).grid(column=0, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)

    root.mainloop()


def print_result():
    global frm
    ttk.Label(frm, text=f'{time_new_year()} дней до нового года').grid(column=1, row=1)




