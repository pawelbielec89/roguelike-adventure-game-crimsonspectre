import os
import player_module
import board_module
import random

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

def save_highscores(player, your_time, level, monsters):
    high_score = "{}, {}, {}, {}".format(player.name, your_time, level, monsters)
    with open("high_score.txt", "a") as f:
        f.write(high_score)
        f.write("\n")


def print_statistics(statistics):
    print("Thirst: " + "=" * statistics.thirst)
    print("HP: " + str(statistics.health_points))
    print("Dmg: " + str(statistics.damage))
    print("Dex: " + str(statistics.dexterity))


def print_inventory(inventory):
    sum_count = 0
    sum_weight = 0
    count = "count"
    weight = "weight"
    key_name = "item name"

    max_len_key = [key for key in inventory.keys()]
    lenght_key = len(max(max_len_key))

    if lenght_key < len(key_name):
        lenght_key = len(key_name)

    headers = ("{:>15}" "{:>" + str(len(count) + 3) + "}"\
    "{:>" + str(len(weight) + 3) + "}").format(key_name, count, weight)
    print("Inventory:")
    print(headers)
    print("-"*len(headers))

    for key, value in inventory.items():
        sum_count += value[0]
        sum_weight += value[1]
        print (("{:>15}" "{:>" + str(len(count) + 3) + "}"\
        "{:>" + str(len(weight) + 3) + "}").format(key, value[0], value[1]))
    print("-"*len(headers))
    print(("{:>15}" "{:>" + str(len(count) + 3) + "}"\
    "{:>" + str(len(weight) + 3) + "}").format("total: ", sum_count, sum_weight))
    print("\nAvailable storage: {}".format(100-sum_weight))
    wait_for_enter()

def win():
    print_text("arts/you_win.txt")
    wait_for_enter()


def cold_warm_hot():
    repeat = True
    guesses = 0
    searched_number = random.sample([num for num in range(10)], 3)

    while guesses < 10 and repeat:
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

        guesses += 1

        print(", ".join(returns))

        if returns == 3 * ["Hot"]:
            repeat = False
            win()



def fight_boss():
    print_text("arts/boss.txt")
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
    os.system("clear")
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
        player.monsters_killed += 1
        player.thirst = 25
        enemy.reset_hp()
        getch()
    else:
        print("{} killed you! What a shame! press any key to continue...".format(enemy.name))
        enemy.reset_hp()
        getch()
