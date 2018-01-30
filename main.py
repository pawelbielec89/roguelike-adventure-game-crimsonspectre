import print_text
import os
import sys
from time import time
from tabulate import tabulate


def play_game():
    start = time()
    your_time = int(time() - start)
    high_scores(your_time)


def helps():
    pass


def show_scores():
    os.system("clear")
    print_text.print_scores()
    headers = ["name", "time spent"]
    with open("high_score.txt", "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(",") for element in lines]
    print (tabulate(table, headers, tablefmt="fancy_grid"))
    print("\n")
    input("Press Enter to continue...")


def high_scores(your_time):
    name = input("What's your name?:\t")
    high_score = "{}, {}".format(name, your_time)
    saving_to_file_highscore(high_score)


def saving_to_file_highscore(high_score):
    with open("high_score.txt", "a") as f:
        f.write(high_score)
        f.write("\n")


def intro():
    pass


def choose():
    list_options = ["(S)how scores",
                "(H)elp",
                "(I)ntro",
                "(T)erminate"]
    print_text.print_menu(list_options, "(P)lay Game")

    option = input("\n" + "-"*40 + "\nPlease enter a letter from bracket: ").lower()
    if option == "p":
        play_game()
    elif option == "s":
        show_scores()
    elif option == "h":
        helps()
    elif option == "i":
        intro()
    elif option == "t":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def print_error_message(message):
    print(message)


def main():
    while True:
        try:
            choose()
        except KeyError as err:
            print_error_message(err)


if __name__ == '__main__':
    main()
