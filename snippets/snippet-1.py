# Israel Méndez Crespo
# Scripting Languages
# COP 2830C Section 13005
# Projects 1.2 and 1.3
# Cooking with Python

# This mini-game demonstrates some of the basic functionality
# provided within Python. The mini-game will make use of
# variables and conditional branching to create a game flow.

# The premise of the game is to make a perfect burger. First,
# the user must choose a recipe. After the recipe is chosen,
# ingredients will be presented to be taken out, to cook, or
# to store. Each of the beforehand tasks will take time
# to do which will affect the status of the ingredient. To
# make a perfect burger, the user will need to time the use
# of all ingredients in a strategic manner.

# This section will declare the variables to be used throughout
# the program.

total_time           = 0
burger_score         = 0

done_cooking = False

bun_time             = 0
burger_time          = 0
onion_time           = 0
bacon_time           = 0

pickle_count         = 0
tomato_count         = 0
cheese_count         = 0

bun_is_toasting      = 0
burger_is_grilling   = 0
onions_are_cooking   = 0
bacon_is_frying      = 0

pickle_count         = 0
tomato_count         = 0
cheese_count         = 0

has_bun              = False
has_burger           = False
has_onion            = False
has_bacon            = False
has_cheese           = False
has_pickles          = False
has_tomato           = False
has_lettuce          = False
has_ketchup          = False
has_mayo             = False
has_mustard          = False
has_bbq              = False

# The introduction screen will prompt out so the
# user can make a selection on the recipe to follow.

print("\t\t\tCOOKING WITH PYTHON\n"
      "\n"
      "\n"
      "\t\t\tChoose your recipe: \n\n"
      "\t01- Angela's Original Bacon Burger\n"
      "\t02- Super Deluxe Python Burger\n"
      "\t03- The Wild West Special\n")

print("\tSelection:", end=" ")
recipe_choice = int(input())
valid_recipe = False

while(valid_recipe == False):
    if (1 <= recipe_choice <= 3):
        valid_recipe = True
    else:
        print("Please make a selection from the options above.")
        recipe_choice = int(input())

# The following code corresponds to the first recipe.
# First the recipe for the burger is printed out and
# the tasks can be selected.

if recipe_choice == 1:
    print("\n\t\t\tANGELA'S ORIGINAL BACON BURGER\n"
          "\n\tDescription: 1/4 inch thick, textured,\n"
          "\tand crispy bacon, Medium done or medium \n"
          "\twell patties, toppings are optional, bun \n"
          "\ttoast is optional.\n")

if recipe_choice == 2:
    print("\n\t\t\tSUPER DELUXE PYTHON BURGER\n"
          "\n\tDescription: Medium done or medium\n"
          "\tpatties. Fresh lettuce, tomato, and\n"
          "\tketchup with mayo.\n")

if recipe_choice == 3:
    print("\n\t\t\tTHE WILD WEST SPECIAL\n"
          "\n\tDescription: Medium done or medium\n"
          "\twell patties. Perfectly cooked onions.\n"
          "\tbacon and BBQ Sauce")

# This section is the core of our program. In it we start
# counting the time units as we select the tasks to be made
# Each task will add one time unit to the total time variable.
# The less time the user takes completing this recipe, the
# higher the burger score will be.

# This section outputs the tasks available to the user

while(done_cooking == False):
    print("\t\t\t\t\tSELECT TASK:\n\n"
          "01- Toast Buns    \t05- Place Pickles  \t09- Add Ketchup\n"
          "02- Grill Burgers \t06- Fry Bacon      \t10- Add Mayo\n"
          "03- Add Cheese    \t07- Chop Lettuce   \t11- Add Mustard\n"
          "04- Cook Onions   \t08- Slice Tomatoes \t12- Add BBQ\n"
          "\n00- Done Cooking\n")

    # The following prompts notify the user of the status
    # of the food and the time units passed.

    print("\t\tTime elapsed: " + str(total_time) + "\n")

    # Bun Notifications

    if bun_is_toasting:
        bun_time += 1
        print("\t\tBun Time: " + str(bun_time))

        if 1 <= bun_time <= 3:
            print("\t\tNotification: Buns are getting toasty!")
        if 4 <= bun_time <= 5:
            print("\t\tNotification: Buns are perfect <3")
        if bun_time >= 6:
            print("\t\tNotification: This is burnt")
            bun_is_toasting = False
            bun_time = 0

    # Burger Notifications

    if burger_is_grilling:
        burger_time += 1
        print("\t\tBurger Time: " + str(burger_time))

        if 1 <= burger_time <=2:
            print("\t\tNotification: This burger is bloody.")
        if burger_time == 3:
            print("\t\tNotification: This burger is medium rare.")
        if burger_time == 4:
            print("\t\tNotification: This burger is medium.")
        if burger_time == 5:
            print("\t\tNotification: This burger is medium well")
        if burger_time == 6:
            print("\t\tNotification: This burger is well-done")
        if burger_time >= 7:
            print("\t\tNotification: Well, at least the dog will eat it.")
            burger_is_grilling = False
            burger_time = 0

    # Onion Notifications

    if onions_are_cooking == True:
        onion_time += 1
        print("\t\tOnion Time: " + str(onion_time))

        if 1 <= onion_time <= 3:
            print("\t\tNotification: Onions are getting there!")
        if 4 <= onion_time <= 5:
            print("\t\tNotification: Onions are just right :)")
        if 6 <= onion_time <= 7:
            print("\t\tNotification: Still time to save the onions")
        if onion_time >= 8:
            print("\t\tNotification: Better get new onions")
            onions_are_cooking = False
            onion_time = 0

    # Bacon Notifications

    if bacon_is_frying == True:
        bacon_time += 1
        print("\t\tBacon Time: " + str(bacon_time))

        if 1 <= bacon_time <= 3:
            print("\t\tNotification: Bacon is on!\n")
        if 4 <= bacon_time <= 5:
            print("\t\tNotification: Getting to that crispy spot...\n")
        if 6 <= bacon_time <= 7:
            print("\t\tNotification: Perfect, crispy bacon!\n")
        if bacon_time >= 8:
            print("\t\tNotification: What have you done?!\n")
            bacon_is_frying = False
            bacon_time = 0

    # This section will store the input value and make sure it doesn't
    # go above or below the options threshold. However, it only validates
    # numerical data types and not strings.

    print("\n\t\tSelection:", end=" ")
    task_choice = int(input())
    valid_task = False

    while (valid_task == False):
        if (0 <= task_choice <= 13):
            valid_task = True
        else:
            print("Please make a selection from the options above.\n")
            task_choice = int(input())

    print("\n\t\tNotification: ", end="")

    # This section handles the branches relating to tasks to be
    # by the user as it "creates" the burger. Each option itself
    # has branches to indicate the quantity of the ingredients or
    # the status of their coction.

    # TASK CHOICE 1: Toast Buns

    if task_choice  == 1:
        if has_bun == False and bun_is_toasting == False:
            total_time += 1
            print("Buns are toasting!\n")
            bun_is_toasting = True
        elif bun_is_toasting == True:
            print("Taking out the buns!\n")
            has_bun = True
            bun_is_toasting = False
        else:
            print("You already have buns for the burger!\n")

    # TASK CHOICE 2: Grill Burgers

    elif task_choice == 2:
        if has_burger == False and burger_is_grilling == False:
            total_time += 1
            print("Patties are grilling!\n")
            burger_is_grilling = True
        elif burger_is_grilling:
            print("Taking out the patties!\n")
            has_burger = True
            burger_is_grilling = False
        else:
            print("You already have a patty on your burger!\n")

    # TASK CHOICE 3: Add Cheese

    elif task_choice == 3:
        total_time   += 1
        cheese_count += 1
        if cheese_count == 0:
            print("We've got cheese!\n")
        if 0 < cheese_count < 4:
            print("Cheesy goodness :D\n")
        if 3 < cheese_count < 6:
            print("You really like cheese :O\n")
        if cheese_count >= 6:
            print("I hope you're not lactose intolerant ;)\n")

    # TASK CHOICE 4: Cook Onion

    elif task_choice == 4:
        if has_onion == False and onions_are_cooking == False:
            total_time += 1
            print("Let's add some onions for good measure\n")
            onions_are_cooking = True
        elif onions_are_cooking == True:
            print("Adding onions to the burger!\n")
            has_onion = True
            onions_are_cooking = False
        else:
            print("You already have a onions on your burger!\n")

    # TASK CHOICE 5: Place Pickles

    elif task_choice == 5:
        total_time += 1
        pickle_count += 1
        if pickle_count == 0:
            print("Don't forget the pickles!\n")
        if 0 < pickle_count < 4:
            print("Really making sure you didn't forget those, huh?\n")
        if 3 < pickle_count < 6:
            print("Can you open those jars?\n")
        if pickle_count >= 6:
            print("A real fan of the pickle\n")

    # TASK CHOICE 6: Fry Bacon

    elif task_choice == 6:
        if has_bacon == False and bacon_is_frying == False:
            total_time += 1
            print("Bacon is good for your heart :)\n")
            bacon_is_frying = True
        elif bacon_is_frying == True:
            print("Let's put some delicious pork belly on this burger!\n")
            has_bacon = True
            bacon_is_frying = False
        else:
            print("You already have a bacon on your burger!\n")

    # TASK CHOICE 7: Chop Lettuce

    elif task_choice == 7:
        total_time   += 1
        has_lettuce   = True
        print("This counts as my veggie portion!\n")

    # TASK CHOICE 8: Slice Tomatoes

    elif task_choice == 8:
        total_time   += 1
        tomato_count += 1
        if tomato_count == 0:
            print("Fresh Tomatoes :)\n")
        if 0 < tomato_count < 4:
            print("I say To-MAH-to!\n")
        if 3 < tomato_count < 6:
            print("You really dig these round red things!\n")
        if tomato_count >= 6:
            print("Might as well give you the whole thing :O\n")

    # TASK CHOICE 9: Add Ketchup

    elif task_choice == 9:
        total_time   += 1
        has_ketchup   = True
        print("Can't have a burger without ketchup!\n")

    # TASK CHOICE 10: Add Mayo

    elif task_choice == 10:
        total_time   += 1
        has_mayo      = True
        print("Just spread some Mayo!\n")

    # TASK CHOICE 11: Add Mustard

    elif task_choice == 11:
        total_time   += 1
        has_mustard   = True
        print("Mustard with a pH of 1\n")

    # TASK CHOICE 12: Add BBQ

    elif task_choice == 12:
        total_time   += 1
        has_bbq       = True
        print("This is the tasty stuff!\n")

    # TASK CHOICE 00: Done Cooking

    # The last option for the user serves to indicate they have
    # finished completing the tasks. The program will assign a score
    # depending on the recipe. Each recipe awards different scores
    # for each category and penalizes the score respective to time
    # elapsed creating the burger.

    elif task_choice == 00:
        done_cooking = True

        # These are the score setters for Angela's Original Bacon Burger.
        # It favors medium and medium well burgers, perfect crispy
        # bacon, and the inclusion of a bun. Bonus points for toasty.

        if recipe_choice == 1:
            if has_burger == True:
                if burger_score < 4:
                    burger_score += burger_time * 5
                elif 4 <= burger_time <= 5:
                    burger_score += burger_time * 10
                else:
                    burger_score -= burger_time * 10
            if has_bun == True:
                if bun_time < 4:
                    burger_score += bun_time * 5
                elif 4 <= bun_time <= 5:
                    burger_score += bun_time * 10
                else:
                    burger_score -= bun_time * 10
            if has_bacon == True:
                if bacon_time < 4:
                    burger_score += bacon_time * 5
                elif 4 <= bacon_time <= 6:
                    burger_score += bacon_time * 10
                elif 7 <= bacon_time <= 8:
                    burger_score += bacon_time * 15
                else:
                    burger_score -= bacon_time * 10

        # These are the score setters for the Super Deluxe Python Burger
        # It favors medium and medium well burgers, perfect crispy bacon,
        # and awards bonus points for lettuce, tomato, ketchup, and mayo.

        if recipe_choice == 2:
            if has_burger == True:
                if burger_score < 4:
                    burger_score += burger_time * 5
                elif 4 <= burger_time <= 5:
                    burger_score += burger_time * 10
                else:
                    burger_score -= burger_time * 10
            if has_bacon == True:
                if bacon_time < 4:
                    burger_score += bacon_time * 5
                elif 4 <= bacon_time <= 6:
                    burger_score += bacon_time * 10
                elif 7 <= bacon_time <= 8:
                    burger_score += bacon_time * 15
                else:
                    burger_score -= bacon_time * 10
            if has_lettuce == True:
                burger_score += 15
            if has_tomato == True:
                burger_score += 15
            if has_ketchup == True:
                burger_score += 15
            if has_mayo == True:
                burger_score += 15

        # These are the score setters for the The Wild West Special
        # It favors medium and medium well burgers, perfectly cooked
        # onions, and awards a substantial bonus if BBQ and Bacon is added.

        if recipe_choice == 3:
            if has_burger == True:
                if burger_score < 4:
                    burger_score += burger_time * 5
                elif 4 <= burger_time <= 5:
                    burger_score += burger_time * 10
                else:
                    burger_score -= burger_time * 10
            if has_onion == True:
                if 1 <= onion_time <= 3:
                    burger_score += onion_time * 5
                if 4 <= onion_time <= 5:
                    burger_score += onion_time * 10
                if 6 <= onion_time <= 7:
                    burger_score += onion_time * 15
                if onion_time >= 8:
                    burger_score -= onion_time * 10

            if has_bbq and has_bacon:
                burger_score += 50

            burger_score -= total_time * 3
        print("Burger score is " + str(burger_score))