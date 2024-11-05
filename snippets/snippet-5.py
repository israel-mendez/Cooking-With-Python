from tkinter import *

my_window = Tk()

def red_bg():
    color_label["bg"] = "red"


def green_bg():
    color_label["bg"] = "green"


def blue_bg():
    color_label["bg"] = "blue"


color_label = Label(my_window, bg="white",
                    width="20", height="3")
color_label.grid(column=1, row=0)

red_button = Button(my_window, text="red",
                    command=red_bg, width="6")
red_button.grid(column=0, row=1)

green_button = Button(my_window, text="green",
                      command=green_bg, width="6")
green_button.grid(column=1, row=1)

blue_button = Button(my_window, text="blue",
                     command=blue_bg, width="6")
blue_button.grid(column=2, row=1)

my_window.mainloop()
