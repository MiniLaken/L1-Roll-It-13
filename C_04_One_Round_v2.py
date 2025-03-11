import random


def initial_points(which_player):...


def make_statement(statement, decoration):
        """Adds emoji / additional characters to the start and end of headings"""

        ends = decoration + 3
        print(f"\n{ends} {statement} {ends}")

    double_user = "no"
# Roll the dice for the user and note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    total = roll_one + roll_two

    if roll_one == roll_two:
        double_user = "yes"

    print("{} no")

# return total, double_user


# At start of game, the scores are zero

# roll dice twice at start of round...

    user_start = initial_points("user")
    comp_start = initial_points("computer")

user_points = user_start[0]
comp_points = comp_start[0]

double_user = user_points[1]

# Let the user know if they qualify for double points
if double_user == "yes":
    print("Great news - if you win, you will earn double points!")

while comp_points < 13 and user_points < 13:
    # roll the dice for the computer
    comp_one = random.randint(1, 6)

# assume user goes first...
first = "User"
second = "computer"
player_1_points = user_points
player_2_points = comp_points

# if the user has fewer points, they start the game
if user_points < comp_points:
    print("You start because your initial roll was less than the computer\n")

# if the user has computer roll equal points, the user is player 1...
elif user_points == comp_points:
    print("The initial rolls are the same, the user starts!")

# if the computer has fewer points, switch the computer to "player 1"
else:
    player_1_points, player_2_points = player_2_points, player_1_points
    first, second = second, first

# loop until we have a winner...
while player_1_points < 13 and player_2_points < 13:
    print()
    input("Press <enter> to continue this round\n")

    # first person rolls the dice and score is updated
    player_1_roll = random.randint(1, 6)
    player_1_points += player_1_roll

    print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

    # if the first person's score is over 13, end the round
    if player_1_points >= 13:
        break

        # second person rolls the dice (and score is updated)
        player_2_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

        print(f"{first}: {player_1_points}  |  {second} {player_2_points}")

    # end of round

    # associate player points with the user on the computer
    user_points = player_1_points
    comp_points = player_2_points

    if first == "Computer":
        user_points, comp_points = comp_points, user_points

    # work out who won...
    if user_points > comp_points:
        winner = "user"
    else:
        winner = "computer"

    round_feedback = f"The {winner} won."

    # double user points if eligible
    if winner == "user" and double_user == "yes":
        user_points = user_points

        # output round results
        make_statement("Round Results", "🦡")
        print("\Round Results")
        print(f"User Points: {user_points} | Computer Points: {comp_points}")
        print(Round_feedback)
        print()
