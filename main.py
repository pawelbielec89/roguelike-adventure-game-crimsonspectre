<<<<<<< HEAD
import print_text
import os
import sys
from time import time
from tabulate import tabulate
from board_module import Board
import common
from player_module import Character

def play_game():
    start = time()
    player = Character(1, 1, "Rafaal", "@", 100, 10, 10)

    board = Board(10, 10)
    board.build_board()

    while True:
        os.system("clear")
        board.draw_board()
        player.move(board)

    your_time = int(time() - start)
    high_scores(your_time)


def helps():
    pass


def show_scores():
    os.system("clear")
    print_text.printed("scores.txt")
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


def info():
    os.system("clear")
    print_text.printed("info.txt")
    input("Press Enter to continue...")


def choose():
    list_options = ["(S)how scores",
                "(H)elp",
                "(I)nfo",
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
        info()
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
=======
import common
import os
from player_module import Character
from board_module import Board


def main():

    x = 1 
    y = 1


    board = Board(40,40)
    board.build_board()
    #board.draw_board()
    
    dungeon = Board(40,100)
    dungeon.generate_dungeon()
    dungeon.draw_board()

    player_character = Character(1,1,"Player", "@", 100, 10, 10)

    while True:
        os.system("clear")
        dungeon.draw_board()
        player_character.move(dungeon)


if __name__ == "__main__":
    main()
>>>>>>> 53e262c3a5a52fb149b9af7e8cfe0da57bce10a0
