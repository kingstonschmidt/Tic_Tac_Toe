# -----------------------------------------TIC TAC TOE------------------------------------------------ #
import random
import os


# Functions
def game_grid(rows):
    print(" | ".join(rows[:3]))
    print("__|___|___")
    print(" | ".join(rows[3:6]))
    print("__|___|___")
    print(" | ".join(rows[6:9]))
    print("  |   |")


def player(name, num_range, symbol, grid):
    game = True
    while game:
        # What numbers can you choose
        if len(num_range) == 1:
            user = input(f"{name.title()} choose: {''.join(num_range)}\n> ")

        elif len(num_range) == len(range(int(num_range[0]), int(num_range[-1])+1)):
            user = input(f"{name.title()} choose a number between & including {'-'.join(num_range[0]+num_range[-1])}"
                         f":\n> ")

        else:
            user = input(f"{name.title()} choose a number: {', '.join(i for i in num_range)}\n> ")

        # Check, replace & delete number
        if user in num_range:
            num_range.remove(user)
            grid[int(user) - 1] = symbol
            game = False

        else:
            print(f"Number: {user} was already played")


def robot_player(num_range, symbol, grid):
    robot = random.choice(num_range)

    # Check, replace & delete number
    if robot in num_range:
        print(f"\nRobot's number: {robot}\n")
        num_range.remove(robot)
        grid[int(robot) - 1] = symbol


def end_game(counter, pl1, pl2):
    global no_winner
    rules = [[fields[0], fields[3], fields[6]], [fields[1], fields[4], fields[7]], [fields[2], fields[5], fields[8]],
             [fields[0], fields[1], fields[2]], [fields[3], fields[4], fields[5]], [fields[6], fields[7], fields[8]],
             [fields[0], fields[4], fields[8]], [fields[2], fields[4], fields[6]]]

    for i in rules:
        if i.count("X") == 3:
            print(f"{pl1.title()} is the winner")
            no_winner = False
        elif i.count("O") == 3:
            print(f"{pl2.title()} is the winner")
            no_winner = False
    if counter == 9 and no_winner:
        print("No winner")
        no_winner = False


# _______________________________________________________________________________________ #


# Variables
fields = [".", ".", ".",
          ".", ".", ".",
          ".", ".", "."]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
no_winner = True
player2 = None
count = 0


# User
print("Welcome to 'Tic Tac Toe'")
game_grid(fields)
player1 = input("Hey, What is yor name?:\n> ").lower()
answer = input(f"{player1.title()}, Is there a second player? Y/N:\n> ").lower()


# ---------------------------------------------GAME-------------------------------------------------- #


if answer == "y":
    while no_winner:
        # First player
        count += 1
        player(name=player1, num_range=num, symbol="X", grid=fields)
        game_grid(rows=fields)

        if player2 is None:
            player2 = input(f"Second player: What is yor name?\n> ").lower()

        # Game results
        end_game(counter=count, pl1=player1, pl2=player2)

        if no_winner:
            # Second player
            count += 1
            player(name=player2, num_range=num, symbol="O", grid=fields)
            game_grid(rows=fields)

            # Game results
            end_game(counter=count, pl1=player1, pl2=player2)


# Playing with the Robot
else:
    while no_winner:
        count += 1
        # First player
        player(name=player1, num_range=num, symbol="X", grid=fields)
        game_grid(rows=fields)

        # Game results
        end_game(counter=count, pl1=player1, pl2="Robot")

        if no_winner:
            # Robot
            count += 1
            robot_player(num_range=num, symbol="O", grid=fields)
            game_grid(rows=fields)

            # Game results
            end_game(counter=count, pl1=player1, pl2="Robot")


# Play Game again
answer = input("Would you like to play again?: Y/N\n> ").lower()
if answer == "y":
    if os.name == "posix":
        os.system("clear")

    else:
        os.system("cls")
