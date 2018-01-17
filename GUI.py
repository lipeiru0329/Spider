from Tkinter import *
import Tkinter as tk
from MultiList import MultiListbox


window = tk.Tk()
window.title("The Spider")
# window.geometry("500x500")
list_value = tk.StringVar()
e1 = tk.Entry(window, show=None)
e1.insert(0, 'Keyword')
e2 = tk.Entry(window, show=None)
e2.insert(0, 'Time')
tx = tk.Text(window, height=2, width=16)
mlb = MultiListbox(window, (('Subject', 40), ('Sender', 20), ('Date', 10)))
# lb = tk.Listbox(window, listvariable = list_value)
lb = tk.Listbox(window)
# lmb = .MULTIPLE(window)

# # e.pack()
# tx.pack()
# # e.grid()
#
# var_value1 = tk.StringVar()
# var_value2 = tk.StringVar()
on_click = False
#
#
def confirm():
    global on_click
    var_value1 = e1.get()
    var_value2 = e2.get()
    # tx.insert('insert', var_value2)
    if var_value2:
        if var_value1:
            lb.insert('end', var_value2)
            mlb.insert(END, (var_value2 , var_value1, 'OK' ))
            e1.delete(0, 'end')
            e2.delete(0, 'end')
    # # global var_value
    # if on_click:
    #     var_value.set('Confirmed')
    #     # var_value.set('Confirmed')
    #     on_click = False
    # else:
    #     var_value.set('To Be Confirmed')
    #     on_click = True
#
#
def cancel():
    var_value1 = e1.get()
    # tx.insert('end', var_value1)


def entry_hints1(event):
    test1 = e1.focus_get()
    if test1:
        e1.delete(0, 'end')
    else:
        e1.insert(0, 'Keyword')


def entry_hints2(event):
    e2.focus_set()
    e2.delete(0, 'end')
    # else:
    #     e2.insert(0, 'Time')

    # print test.get()


def make_gui():
    # l = tk.Label(window, textvariable = var_value2, bg = 'brown', font = ('Times New Roman', 12), width = 15, height = 2)
    # l.pack()
    b1 = tk.Button(window, text = 'Confirmed', bg = 'orange', font = ('Arial', 12), width = 15, height = 2, command = confirm)
    l1 = tk.Label(window, text = 'Search')
    # b1.pack()
    l1.grid(row=0, column=0)
    # l1.grid(row=0)
    b1.grid(row=0, column=2)
    e1.grid(row=0, column=1)
    b2 = tk.Button(window, text='Cancel', bg='orange', font=('Arial', 12), width=15, height=2, command = cancel)
    l2 = tk.Label(window, text='Time')
    l2.grid(row=1)
    e2.grid(row = 1, column = 1)
    b2.grid(row=1, column=2)
    # tx.pack()

    mlb.grid(row = 2, column = 1)
    # lb.pack(row = 2, column = 1)
    e1.bind("<FocusIn>", entry_hints1)
    e2.bind("<FocusIn>", entry_hints2)
    # e2.bind("<Button-2>", entry_hints2)
    # e1.bind("<Button-1>", entry_hints)
    window.mainloop()
