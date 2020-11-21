from tkinter import *
import sys

def command1():
    if entry1.get() == 'admin' and entry2.get() == 'password' or entry1.get() == 'test' and entry2.get() == 'pass':
        root.deiconify()
        top.destroy()

def command2():
    top.destroy()
    root.destroy()


root = Tk()
top = TopLevel()

top.geometry('300x260')
top.title('Login screen')
top.configure(background='white')

label1 = Label(top, text="Username: ")
entry1 = Entry(top)

label2 = Label(top, text="Password: ")
entry2 = Entry(top, show="*")

button = Button(top, text='Cancel', command= lambda:command2())

entry2.bind('<Return>', command1)

label = Label(top, text='Copyright Jose Lourenco, Rodrigo Mendes', font={'Arial', 9})

label1.pack()
label2.pack()
entry1.pack()
entry2

root.mainloop()

ISTO
E
UM TESTE

