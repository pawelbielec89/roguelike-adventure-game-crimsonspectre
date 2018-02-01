import os
import player_module
import board_module

def getch():    # define function getch() to read exactly one character from user's input
    import sys, tty, termios    # include librares sys, tty and termios to the project
    fd = sys.stdin.fileno() # assign file descriptor (int) returned by stdin.fileno() method to fd variable
    old_settings = termios.tcgetattr(fd)    # assign a list containing the tty attributes for file descriptor fd returned by tcgetattr() method
    try:    # execute the statements if no exceptions occures
        tty.setraw(sys.stdin.fileno())  # change the mode of the file descriptor returned by stdin.fileno() to raw
        ch = sys.stdin.read(1)  # call function stdin.read with argument 1 to read into the user-entered string of length 1
    finally:    # do the following statements even if exception occurs
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # change tty attributes for file descriptor fd from attributes list old_settings after transmitting all queued output
    return ch


def wait_for_enter():
    input("\nPress Enter to continue...\n")


def print_text(files):
    os.system("clear")

    with open(files, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line[:-1])



def print_menu(list_options):
    print_text("arts/print_menu.txt")

    for i in range(len(list_options)):
        print("\t", list_options[i])

    print("\n" + "-"*40 + "\nPlease enter a letter from bracket: ", end="")

def save_highscores(player, your_time, level):
    high_score = "{}, {}, {}".format(player.name, your_time, level)
    with open("high_score.txt", "a") as f:
        f.write(high_score)
        f.write("\n")


def win():
    print_text("arts/you_win.txt")
    save_highscores()


def cold_warm_hot():
    is_play = True

    while is_play:
        guesses = 0
        searched_number = sample([num for num in range(10)], 3)

        # print(searched_number)

        while guesses < 10:
            user_guess = input("I am thinking of a 3-digit number. Try to guess what it is: ")
            user_guess = list(map(int, user_guess))
            returns = []

            if (user_guess[0] in searched_number or
                user_guess[1] in searched_number or
                user_guess[2] in searched_number):

                for i, number in enumerate(user_guess):
                    if number in searched_number:
                        if number == searched_number[i]:
                            returns.append("Hot")
                        else:
                            returns.append("Warm")
            else:
                returns.append("Cold")

            if returns == 3 * ["Hot"]:
                win()

            print("Guess #{}".format(str(guesses+1)))
            print("".join(map(str, user_guess)))
            print(", ".join(returns))
            guesses += 1


def fight_boss():
    common.print_text("arts/boss.txt")
    cold_warm_hot()


def set_step(starting_point, destination):
    if starting_point > destination:
        return -1
    else:
        return 1


def game_over():
    print_text("arts/you_lose.txt")
    wait_for_enter()


def check_game_status(player):
    if player.health_points <= 0:
        return False
    else:
        return True


def fight(player, enemy):
    attacker = player
    defender = enemy
    while player.health_points > 0 and enemy.health_points > 0:
        hitted = attacker.attack(defender)
        if hitted:
            print("{} attack  {} and dealt {} damage. {} HP left".format(attacker.name, defender.name, str(attacker.damage), defender.health_points))
        else:
            print("{} dodged.".format(defender.name, defender.health_points))
        attacker, defender = defender, attacker

    if player.health_points > 0:
        print("You defeated {}! press any key to continue...".format(enemy.name))
        enemy.reset_hp()
        getch()
    else:
        print("{} killed you! What a shame! press any key to continue...".format(enemy.name))
        enemy.reset_hp()
        getch()
