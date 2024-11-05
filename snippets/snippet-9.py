import tkinter as tk
from PIL import Image, ImageTk

# Create the master object
master = tk.Tk()

master.geometry("800x600")
master.title("Super Burger Challenge 2020")
master.iconbitmap('img/burger_icon.ico')

# Create the label objects and pack them using grid
tk.Label(master, text="Label 1").grid(row=0, column=0)
tk.Label(master, text="Label 2").grid(row=1, column=0)

# Create the entry objects using master
e1 = tk.Entry(master)
e2 = tk.Entry(master)

# Pack them using grid
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

button1 = tk.Button(master, text="Button 1")
button1.grid(columnspan=2, row=2, column=0)

# Create the PIL image object
image = Image.open("img/grill.png")
image = image.resize((450, 350), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

# Create an image label
img_label = tk.Label(image=photo)
# Store a reference to a PhotoImage object, to avoid it
# being garbage collected! This is necessary to display the image!
img_label.image = photo

img_label.grid(row=0, column=2)


def change_grid():
    img_label.grid(row=0, column=0)


# Create another button
button2 = tk.Button(master, text="Button 2", command=change_grid)
button2.grid(columnspan=2, row=2, column=2)

# The mainloop
tk.mainloop()
