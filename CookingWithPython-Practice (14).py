import threading
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from threading import *
from time import sleep

# Global variables for time functions
countdown = 3
timer = 59
total_burgers = 0
top_occupied = False
bottom_occupied = False
kitchen_full = False
multi_time1 = 0
multi_time2 = 0

# Main GUI Object
window = Tk()

# Title Settings
window.title("Super Burger Challenge 2020")
window.iconbitmap('img/burger_icon.ico')
window.resizable(width=False, height=False)

width_of_window = 705
height_of_window = 505

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

upper_left_x = (screen_width / 2) - (width_of_window / 2)
upper_left_y = (screen_height / 2) - (height_of_window / 2)

window.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
                                 upper_left_x, upper_left_y))

# Create Image Objects

previous_image = Image.open("img/previous.png")
previous_image = previous_image.resize((100, 100), Image.ANTIALIAS)
previous_photo = ImageTk.PhotoImage(previous_image)

next_image = Image.open("img/next.png")
next_image = next_image.resize((100, 100), Image.ANTIALIAS)
next_photo = ImageTk.PhotoImage(next_image)

bun_image = Image.open("img/buns.png")
bun_image = bun_image.resize((100, 100), Image.ANTIALIAS)
bun_photo = ImageTk.PhotoImage(bun_image)

patty_image = Image.open("img/patty.png")
patty_image = patty_image.resize((100, 100), Image.ANTIALIAS)
patty_photo = ImageTk.PhotoImage(patty_image)

bacon_strip_image = Image.open("img/bacon.png")
bacon_strip_image = bacon_strip_image.resize((100, 100), Image.ANTIALIAS)
bacon_strip_photo = ImageTk.PhotoImage(bacon_strip_image)

cheese_image = Image.open("img/cheese.png")
cheese_image = cheese_image.resize((100, 100), Image.ANTIALIAS)
cheese_photo = ImageTk.PhotoImage(cheese_image)

onion_image = Image.open("img/onions.png")
onion_image = onion_image.resize((100, 100), Image.ANTIALIAS)
onion_photo = ImageTk.PhotoImage(onion_image)

lettuce_image = Image.open("img/lettuce.png")
lettuce_image = lettuce_image.resize((100, 100), Image.ANTIALIAS)
lettuce_photo = ImageTk.PhotoImage(lettuce_image)

tomatoes_image = Image.open("img/tomatoes.png")
tomatoes_image = tomatoes_image.resize((100, 100), Image.ANTIALIAS)
tomatoes_photo = ImageTk.PhotoImage(tomatoes_image)

pickle_image = Image.open("img/pickles.png")
pickle_image = pickle_image.resize((100, 100), Image.ANTIALIAS)
pickle_photo = ImageTk.PhotoImage(pickle_image)

ketchup_image = Image.open("img/ketchup.png")
ketchup_image = ketchup_image.resize((100, 100), Image.ANTIALIAS)
ketchup_photo = ImageTk.PhotoImage(ketchup_image)

mustard_image = Image.open("img/mustard.png")
mustard_image = mustard_image.resize((100, 100), Image.ANTIALIAS)
mustard_photo = ImageTk.PhotoImage(mustard_image)

bbq_image = Image.open("img/bbq.png")
bbq_image = bbq_image.resize((100, 100), Image.ANTIALIAS)
bbq_photo = ImageTk.PhotoImage(bbq_image)

mayo_image = Image.open("img/mayo.png")
mayo_image = mayo_image.resize((100, 100), Image.ANTIALIAS)
mayo_photo = ImageTk.PhotoImage(mayo_image)


# Burger Object
class Burger:
    def __init__(self, arg_bun, arg_patty, arg_bacon, arg_cheese, arg_onion,
                 arg_lettuce, arg_tomato, arg_pickle, arg_ketchup, arg_mustard,
                 arg_mayo, arg_bbq):
        self.bun = arg_bun
        self.patty = arg_patty
        self.bacon = arg_bacon
        self.cheese = arg_cheese
        self.onion = arg_onion
        self.lettuce = arg_lettuce
        self.tomato = arg_tomato
        self.pickle = arg_pickle
        self.ketchup = arg_ketchup
        self.mustard = arg_mustard
        self.mayo = arg_mayo
        self.bbq = arg_bbq
        self.is_ready = False
        self.type = 0

    def add_list(self):
        ready_list = Label(window, text="Ingredients Ready:\n" +
                                        "\nBun: " + str(self.bun) +
                                        "\nPatty: " + str(self.patty) +
                                        "\nBacon: " + str(self.bacon) +
                                        "\nCheese:" + str(self.cheese) +
                                        "\nOnions:" + str(self.onion) +
                                        "\nLettuce: " + str(self.lettuce) +
                                        "\nTomatoes: " + str(self.tomato) +
                                        "\nPickles: " + str(self.pickle) +
                                        "\nKetchup: " + str(self.ketchup) +
                                        "\nMustard: " + str(self.mustard) +
                                        "\nMayo: " + str(self.mayo) +
                                        "\nBBQ: " + str(self.bbq),
                           justify="left")
        ready_list.grid(column=4, row=2, rowspan=2)

        # Burger Aggregator
        def add_burger():
            self.is_ready = False
            self.bun = False
            self.patty = False
            self.bacon = False
            self.cheese = False
            self.onion = False
            self.lettuce = False
            self.tomato = False
            self.pickle = False
            self.ketchup = False
            self.mustard = False
            self.mayo = False
            self.bbq = False

            self.add_list()

            global total_burgers
            total_burgers += 1

        # Done Button
        done_button = Button(text="DONE", state="disabled", command=add_burger)
        done_button.grid(column=5, row=3)

        # Readiness Verifier
        if self.type == 1:
            if self.bun and self.patty and self.bacon:
                done_button.config(state="active")
        elif self.type == 2:
            if self.bun and self.patty and self.bacon \
                    and self.lettuce and self.tomato \
                    and self.ketchup and self.mayo:
                done_button.config(state="active")
        elif self.type == 3:
            if self.bun and self.patty and self.onion \
                    and self.bacon and self.bbq:
                done_button.config(state="active")


# Creates Burger Objects

current_burger = Burger(False, False, False, False,
                        False, False, False, False,
                        False, False, False, False)

previous_burger = Burger(False, False, False, False,
                         False, False, False, False,
                         False, False, False, False)

next_burger = Burger(False, False, False, False,
                     False, False, False, False,
                     False, False, False, False)


def cycle_forward():
    global current_burger, previous_burger, next_burger

    previous_burger.type = current_burger.type
    next_burger.type = current_burger.type

    temp_burger = current_burger
    current_burger = next_burger
    next_burger = previous_burger
    previous_burger = temp_burger

    current_burger.add_list()


def cycle_backwards():
    global current_burger, previous_burger, next_burger

    previous_burger.type = current_burger.type
    next_burger.type = current_burger.type

    temp_burger = current_burger
    current_burger = previous_burger
    previous_burger = next_burger
    next_burger = temp_burger

    current_burger.add_list()


# General Function Definitions

def toast_buns():
    global top_occupied, bottom_occupied, kitchen_full
    position = 0

    # Nested Function
    def add_bun():
        global top_occupied, bottom_occupied, kitchen_full

        if toast_progress["value"] >= 100:
            if position == 0:
                current_burger.bun = True
                current_burger.add_list()
                toast_buns_button.destroy()
                toast_buns_label.destroy()
                toast_progress.destroy()
                top_occupied = False
                kitchen_full = False
            if position == 1:
                current_burger.bun = True
                current_burger.add_list()
                toast_buns_button.destroy()
                toast_buns_label.destroy()
                toast_progress.destroy()
                bottom_occupied = False
                kitchen_full = False

    def step():
        for i in range(100):
            toast_progress["value"] += 2
            window.update_idletasks()
            sleep(.1)

    if not kitchen_full:
        if not top_occupied:
            top_occupied = True
            if bottom_occupied:
                kitchen_full = True
        elif not bottom_occupied:
            bottom_occupied = True
            position += 1
            if top_occupied:
                kitchen_full = True

        # Toast Buns Label
        toast_buns_label = Label(window, text="Toasting Buns")
        toast_buns_label.grid(column=4, row=0 + position, sticky="s")

        # Toast Buns Button
        toast_buns_button = Button(image=bun_photo, command=add_bun)
        toast_buns_button.grid(column=4, row=0 + position, sticky="n")

        # Toast Buns Progressbar
        toast_progress = ttk.Progressbar(window, orient="horizontal",
                                         length=75, mode="determinate")
        toast_progress.grid(column=5, row=0 + position)
        threading.Thread(target=step).start()


def delete_grill_label():
    grill_img_label.destroy()


def delete_bacon_label():
    bacon_label.destroy()
    bacon_img_label.destroy()


def delete_deluxe_label():
    deluxe_label.destroy()
    deluxe_img_label.destroy()


def delete_western_label():
    western_label.destroy()
    western_img_label.destroy()


def delete_main_labels():
    delete_bacon_label()
    delete_deluxe_label()
    delete_western_label()
    delete_grill_label()
    start_countdown()


def change_to_ready(label):
    label.config(text="Get ready!")
    current_burger.add_list()


def enable_button(self):
    self["state"] = "active"


def disable_button(self):
    self["state"] = "disable"


def abb_chosen():
    current_burger.type = 1
    delete_main_labels()


def spd_chosen():
    current_burger.type = 2
    delete_main_labels()


def wbq_chosen():
    current_burger.type = 3
    delete_main_labels()


# def add_bun():
#     current_burger.bun = True
#     current_burger.add_list()


def add_patty():
    current_burger.patty = True
    current_burger.add_list()


def add_bacon():
    current_burger.bacon = True
    current_burger.add_list()


def add_cheese():
    current_burger.cheese = True
    current_burger.add_list()


def add_onion():
    current_burger.onion = True
    current_burger.add_list()


def add_lettuce():
    current_burger.lettuce = True
    current_burger.add_list()


def add_tomatoes():
    current_burger.tomato = True
    current_burger.add_list()


def add_pickles():
    current_burger.pickle = True
    current_burger.add_list()


def add_ketchup():
    current_burger.ketchup = True
    current_burger.add_list()


def add_mustard():
    current_burger.mustard = True
    current_burger.add_list()


def add_mayo():
    current_burger.mayo = True
    current_burger.add_list()


def add_bbq():
    current_burger.bbq = True
    current_burger.add_list()


# Time Functions
def start_countdown():
    global countdown
    if countdown > 0:
        main_label.config(text="Starting in: " + str(countdown))
        countdown -= 1
        main_label.after(1000, start_countdown)
    elif countdown == 0:
        main_label.config(text="Go!")
        main_label.after(1000, start_timer)
        add_ingredient_grid()
        current_burger.add_list()


def start_timer():
    global timer
    if timer > 0:
        main_label.config(text="Time Left: " + str(timer) +
                               "\nBurgers: " + str(total_burgers))
        timer -= 1
        main_label.after(1000, start_timer)
    elif timer == 0:
        main_label.config(text="Game Over!")


def add_ingredient_grid():
    # Previous Selection Label
    previous_selection_label = Label(window, text="Previous")
    previous_selection_label.grid(column=2, row=0, sticky="s")

    # Previous Button
    previous_selection_button = Button(image=previous_photo, command=cycle_backwards)
    previous_selection_button.grid(column=2, row=0, sticky="n")

    # Next Selection Label
    next_selection_label = Label(window, text="Next")
    next_selection_label.grid(column=3, row=0, sticky="s")

    # Next Button
    next_selection_button = Button(image=next_photo, command=cycle_forward)
    next_selection_button.grid(column=3, row=0, sticky="n")

    # Bun Selection Label
    bun_selection_label = Label(window, text="Bun")
    bun_selection_label.grid(column=0, row=1, sticky="s")

    # Bun Button
    bun_selection_button = Button(image=bun_photo, command=toast_buns)
    bun_selection_button.grid(column=0, row=1, sticky="n")

    # Patty Selection Label
    patty_selection_label = Label(window, text="Patty")
    patty_selection_label.grid(column=1, row=1, sticky="s")

    # Patty Button
    patty_selection_button = Button(image=patty_photo, command=add_patty)
    patty_selection_button.grid(column=1, row=1, sticky="n")

    # Bacon Selection Label
    bacon_selection_label = Label(window, text="Bacon")
    bacon_selection_label.grid(column=2, row=1, sticky="s")

    # Bacon Button
    bacon_selection_button = Button(image=bacon_strip_photo, command=add_bacon)
    bacon_selection_button.grid(column=2, row=1, sticky="n")

    # Cheese Selection Label
    cheese_selection_label = Label(window, text="Cheese")
    cheese_selection_label.grid(column=3, row=1, sticky="s")

    # Cheese Button
    cheese_selection_button = Button(image=cheese_photo, command=add_cheese)
    cheese_selection_button.grid(column=3, row=1, sticky="n")

    # Onion Selection Label
    onion_selection_label = Label(window, text="Onions")
    onion_selection_label.grid(column=0, row=2, sticky="s")

    # Onion Button
    onion_selection_button = Button(image=onion_photo, command=add_onion)
    onion_selection_button.grid(column=0, row=2, sticky="n")

    # Lettuce Selection Label
    lettuce_selection_label = Label(window, text="Lettuce")
    lettuce_selection_label.grid(column=1, row=2, sticky="s")

    # Lettuce Button
    lettuce_selection_button = Button(image=lettuce_photo, command=add_lettuce)
    lettuce_selection_button.grid(column=1, row=2, sticky="n")

    # Tomato Selection Label
    tomato_selection_label = Label(window, text="Tomatoes")
    tomato_selection_label.grid(column=2, row=2, sticky="s")

    # Tomato Button
    tomato_selection_button = Button(image=tomatoes_photo, command=add_tomatoes)
    tomato_selection_button.grid(column=2, row=2, sticky="n")

    # Pickle Selection Label
    pickle_selection_label = Label(window, text="Pickles")
    pickle_selection_label.grid(column=3, row=2, sticky="s")

    # Pickle Button
    pickle_selection_button = Button(image=pickle_photo, command=add_pickles)
    pickle_selection_button.grid(column=3, row=2, sticky="n")

    # Ketchup Selection Label
    ketchup_selection_label = Label(window, text="Ketchup")
    ketchup_selection_label.grid(column=0, row=3, sticky="s")

    # Ketchup Button
    ketchup_selection_button = Button(image=ketchup_photo, command=add_ketchup)
    ketchup_selection_button.grid(column=0, row=3, sticky="n")

    # Mustard Selection Label
    mustard_selection_label = Label(window, text="Mustard")
    mustard_selection_label.grid(column=1, row=3, sticky="s")

    # Mustard Button
    mustard_selection_label = Button(image=mustard_photo, command=add_mustard)
    mustard_selection_label.grid(column=1, row=3, sticky="n")

    # Mayo Selection Label
    mayo_selection_label = Label(window, text="Mayo")
    mayo_selection_label.grid(column=2, row=3, sticky="s")

    # Mayo Button
    mayo_selection_button = Button(image=mayo_photo, command=add_mayo)
    mayo_selection_button.grid(column=2, row=3, sticky="n")

    # BBQ Selection Label
    bbq_selection_label = Label(window, text="BBQ")
    bbq_selection_label.grid(column=3, row=3, sticky="s")

    # BBQ Button
    bbq_button = Button(image=bbq_photo, command=add_bbq)
    bbq_button.grid(column=3, row=3, sticky="n")


# Label Grid

label_01 = Label(window, width=16, height=8)
label_01.grid(column=0, row=0)
label_02 = Label(window, width=16, height=8)
label_02.grid(column=1, row=0)
label_03 = Label(window, width=16, height=8)
label_03.grid(column=2, row=0)
label_04 = Label(window, width=16, height=8)
label_04.grid(column=3, row=0)
label_05 = Label(window, width=16, height=8)
label_05.grid(column=4, row=0)
label_06 = Label(window, width=16, height=8)
label_06.grid(column=5, row=0)
label_07 = Label(window, width=16, height=8)
label_07.grid(column=0, row=1)
label_08 = Label(window, width=16, height=8)
label_08.grid(column=1, row=1)
label_09 = Label(window, width=16, height=8)
label_09.grid(column=2, row=1)
label_10 = Label(window, width=16, height=8)
label_10.grid(column=3, row=1)
label_11 = Label(window, width=16, height=8)
label_11.grid(column=4, row=1)
label_12 = Label(window, width=16, height=8)
label_12.grid(column=5, row=1)
label_13 = Label(window, width=16, height=8)
label_13.grid(column=0, row=2)
label_14 = Label(window, width=16, height=8)
label_14.grid(column=1, row=2)
label_15 = Label(window, width=16, height=8)
label_15.grid(column=2, row=2)
label_16 = Label(window, width=16, height=8)
label_16.grid(column=3, row=2)
label_17 = Label(window, width=16, height=8)
label_17.grid(column=4, row=2)
label_18 = Label(window, width=16, height=8)
label_18.grid(column=5, row=2)
label_19 = Label(window, width=16, height=8)
label_19.grid(column=0, row=3)
label_20 = Label(window, width=16, height=8)
label_20.grid(column=1, row=3)
label_21 = Label(window, width=16, height=8)
label_21.grid(column=2, row=3)
label_22 = Label(window, width=16, height=8)
label_22.grid(column=3, row=3)
label_23 = Label(window, width=16, height=8)
label_23.grid(column=4, row=3)
label_24 = Label(window, width=16, height=8)
label_24.grid(column=5, row=3)

# Main Label Objects

main_label = Label(window, text="Choose your recipe: ",
                   font="Arial 24 italic bold")
main_label.grid(column=0, row=0, columnspan=3, sticky="nw")

# Main Image and Photo Objects
grill_image = Image.open("img/grill.png")
grill_image = grill_image.resize((250, 250), Image.ANTIALIAS)
grill_photo = ImageTk.PhotoImage(grill_image)
grill_img_label = Label(image=grill_photo)
grill_img_label.grid(column=3, row=1, columnspan=3, rowspan=3, sticky="n")

# BACON BURGER
# Bacon Burger Label
bacon_label = Label(window, text="ANGELA'S ORIGINAL BACON BURGER\n"
                                 "1/4 inch thick, textured, and crispy bacon\n"
                                 "Medium done or medium well patties either\n"
                                 "regular/vegan/organic, toppings are optional,\n"
                                 "bun toast is optional.", justify="right")
bacon_label.grid(column=1, row=1, columnspan=2, sticky="ne")

# Bacon Burger Image Settings
bacon_image = Image.open("img/bacon_burger.png")
bacon_image = bacon_image.resize((100, 100), Image.ANTIALIAS)
bacon_photo = ImageTk.PhotoImage(bacon_image)
bacon_img_label = Button(image=bacon_photo, command=abb_chosen)
bacon_img_label.grid(column=0, row=1, sticky="nw")

# PYTHON DELUXE
# Deluxe Burger Label

deluxe_label = Label(window, text="SUPER DELUXE PYTHON BURGER\n"
                                  "Medium done or medium well\n"
                                  "patties. Fresh lettuce, tomato, and\n"
                                  "ketchup with mayo.", justify="right")
deluxe_label.grid(column=1, row=2, columnspan=2, sticky="ne")

# Deluxe Burger Image Settings
deluxe_image = Image.open("img/python_deluxe.png")
deluxe_image = deluxe_image.resize((100, 100), Image.ANTIALIAS)
deluxe_photo = ImageTk.PhotoImage(deluxe_image)
deluxe_img_label = Button(image=deluxe_photo, command=spd_chosen)
deluxe_img_label.grid(column=0, row=2, sticky="nw")

# WESTERN BBQ
# Western Burger Label

western_label = Label(window, text="THE WILD WEST SPECIAL\n"
                                   "Medium done or medium well patties\n"
                                   "Perfectly cooked onions, with just enough\n"
                                   "crispiness, smoked bacon and BBQ Sauce",
                      justify="right")
western_label.grid(column=1, row=3, columnspan=2, sticky="ne")

# Western Burger Image Settings
western_image = Image.open("img/western_bbq.png")
western_image = western_image.resize((100, 100), Image.ANTIALIAS)
western_photo = ImageTk.PhotoImage(western_image)
western_img_label = Button(image=western_photo, command=wbq_chosen)
western_img_label.grid(column=0, row=3, sticky="nw")

# Event Handler
window.mainloop()
