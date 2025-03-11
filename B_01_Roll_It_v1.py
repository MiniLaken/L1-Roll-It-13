# function go here

def yes_no(question):
    while True:

        response = input(question).lower()

        # check the user says yes/no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
Roll the dice and try to win.
    """)


# Main routine


# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see then...
if want_instructions == "yes":
    instructions()

print()
game_goal = int_checker()
print(game_goal)
