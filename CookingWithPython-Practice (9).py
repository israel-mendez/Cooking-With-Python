from tkinter import *

# WINDOW SETTINGS
# The following settings are used to calibrate the
# display properties of the window

my_window = Tk()

my_window.title("GUI")
my_window.iconbitmap("img/monitor_icon.ico")
my_window.configure(background="black")
my_window.resizable(width=False, height=False)

width_of_window = 700
height_of_window = 500

screen_width = my_window.winfo_screenwidth()
screen_height = my_window.winfo_screenheight()

upper_left_x = (screen_width / 2) - (width_of_window / 2)
upper_left_y = (screen_height / 2) - (height_of_window / 2)

my_window.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
                                    upper_left_x, upper_left_y))

# GUI CONTENT
# The following code has properties of the elements
# that will populate the Python windows

label_1 = Label(my_window, text="Hello, World!", bg="black", fg="white")
label_1.pack()
label_2 = Label(my_window, text="How are you doing today?", bg="black", fg="white")
label_2.pack()
label_3 = Label(my_window, text="Red text in Times font.", bg="black", fg="red",
                font="Times")
label_3.pack()
label_4 = Label(my_window, text="Green text in Broadway font.", bg="black", fg="green",
                font="Broadway")
label_4.pack()
label_5 = Label(my_window, text="Blue text in Verdana font.", bg="black", fg="blue",
                font="Verdana 32 bold italic")
label_5.pack()
label_6 = Label(my_window, text="Text before newline\n\nText after newline\n\n", font="32")
label_6.pack()
label_7 = Label(my_window, text="     ", font="32", width="100")
label_7.pack()
label_8 = Label(my_window, text="Border within label", borderwidth=1, relief="sunken",
                font="32")
label_8.pack()
label_9 = Label(my_window, text="Hello, World!\nHello, World!", bd=1, relief="solid",
                font="Times 32", height=3)
label_9.pack()

var_1 = StringVar()

label_10 = Label(my_window,
                 relief="solid",
                 font="Times 22 bold",
                 textvariable=var_1
                 )

var_1.set("Using text variable and StringVar")
label_10.pack()
# CONSOLE OUTPUT
print(label_1["text"])

# EDIT GUI
label_1['bg'] = "blue"
label_1['text'] = "Changed Text"

# EXECUTE LOOP
# This line will execute the mainloop that handles
# events for the graphical user interface

my_window.mainloop()
