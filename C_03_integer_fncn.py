def int_checker():
    """Checks user enter an integer more than / equal to 13"""

    error = "Please enter an integer more than / equal to 13."

    while True:
        try:
            response = int(input("What is the game goal? "))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine starts here
game_goal = int_checker()
print(game_goal)
