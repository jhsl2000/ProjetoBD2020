from tkinter import *
import sys


def command1(event):
    if entry1.get() == 'admin' and entry2.get() == 'password' or entry1.get() == 'test' and entry2.get() == 'pass':
        root.deiconify()
        top.destroy()


def command2():
    top.destroy()
    root.destroy()


def command3():
    top.destroy() 
    root.deiconify()



root = Tk()
top = Toplevel()
top.geometry('1280x720')
top.title('Login screen')
top.configure(background='white')


photo2 = PhotoImage(file='NETFLOX.png')
photo = Label(top, image=photo2, height=300, width= 250)

button2 = Button(top, text='Registar', command=lambda: command3())
button3 = Button(top, text='Login', command=lambda: command3())
button2.pack()
button3.pack()

root.title('Main Screen')
root.configure(background="white")
root.geometry('1280x720')

label1 = Label(top, text="Username: ")
entry1 = Entry(top)
label2 = Label(top, text="Password: ")
entry2 = Entry(top, show="*")

button = Button(top, text='Cancel', command=lambda: command2())

entry2.bind('<Return>', command1)      # Tecla enter com a combinacao certa avança para a proxima janela

label3 = Label(top, text='Copyright Jose Lourenco, Rodrigo Mendes', font={'Arial', 9})

photo.pack()
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button.pack()
label3.pack()   

root.title('Main Screen')
root.configure(background="white")
root.geometry('1280x720')




root.withdraw()
root.mainloop()


