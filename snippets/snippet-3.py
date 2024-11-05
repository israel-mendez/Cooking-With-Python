from tkinter import *

t = 0


def set_timer():
    global t
    t = t + int(e1.get())
    return t


def countdown():
    global t
    if t > 0:
        l1.config(text=t)
        t -= 1
        l1.after(1000, countdown)
    elif t == 0:
        print("end")
        l1.config(text="Go!")


window = Tk()

window.geometry("180x150")

l1 = Label(window, font="24")
l1.grid(row=1, column=2)

times = StringVar()
e1 = Entry(window, textvariable=times)
e1.grid(row=3, column=2)

b1 = Button(window, text="Set", width=20, command=set_timer)
b1.grid(row=4, column=2, padx=20)

b2 = Button(window, text="Start", width=20, command=countdown)
b2.grid(row=6, column=2, padx=20)

window.mainloop()
