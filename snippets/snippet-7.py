from tkinter import *


def say_hello():
    var_1.set("Hello, " + entry_1.get() + "!")


my_window = Tk()
var_1 = StringVar()

label_1 = Label(my_window, text="Please enter your name: ")
entry_1 = Entry(my_window)
button_1 = Button(my_window, text="Click me to enter name",
                  command=say_hello)
label_2 = Label(my_window, textvariable=var_1)

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
button_1.grid(row=1, column=0)
label_2.grid(row=1, column=1)

my_window.mainloop()
