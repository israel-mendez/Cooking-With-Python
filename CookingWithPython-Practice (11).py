import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()

window.geometry("800x600")
window.title("Super Burger Challenge 2020")
window.iconbitmap('img/burger_icon.ico')

title_label = tk.Label(window, text="Select your recipe:",
                       font="Arial 32 bold", fg="black")

title_label.grid(row=0, column=0)


image = Image.open("img/grill.png")
image = image.resize((450, 350), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
img_label = tk.Label(image=photo, anchor=tk.W)
img_label.image = photo
img_label.grid(column=0, row=0)

tk.mainloop()
