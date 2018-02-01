import os
import sys
import common
import player_module
from board_module import Board
from random import randint
from time import time
from tabulate import tabulate


def main():
    main_menu()

def main_menu():
    while True:
        try:
            choose()
        except KeyError as err:
            print_error_message(err)

def show_info():
    common.print_text("arts/info.txt")
    common.wait_for_enter()


def show_help():
    common.print_text("arts/help.txt")
    common.wait_for_enter()



def choose():
    list_options = ["(P)lay Game",
                "(S)how scores",
                "(H)elp",
                "(I)nfo",
                "(T)erminate"]
    common.print_menu(list_options)

    user_choice = common.getch().lower()

    functions = {"p": handle_game,
                 "s": show_highscores,
                 "h": show_help,
                 "i": show_info,
                 "t": sys.exit}

    functions[user_choice]()


def handle_game():
    common.print_text("arts/intro.txt")
    common.wait_for_enter()
    start = time()

    monsters = [["Rat", "R", 20, 20, 5, 2],
                ["Bat", "B", 40, 40, 10, 4],
                ["Snake", "S", 60, 60, 15, 6]]
    monsters_list = []
    number_of_monsters = randint(10,20)
    inventory = {}

    player = player_module.Player(1,1,"Player", "V", 30, 15, 1, "male", 100, inventory)

    for monster_properties in monsters:
        monster = player_module.Character(*monster_properties)
        monsters_list.append(monster)

    dungeon = Board(40,100)
    level = 0
    in_game = True

    while level <= 3 and in_game:
        level += 1
        in_level = True
        dungeon.generate_dungeon(player.avatar, monsters_list)

        while in_level and in_game:
            dungeon.draw_board()
            x,y = player.move(dungeon, monsters_list)
            collision = dungeon.check_collision(player.x_coord, player.y_coord)
            dungeon.update_board(x, y, player.x_coord, player.y_coord, player.avatar)

            for monster in monsters_list:
                if collision == monster.avatar:
                    common.fight(player, monster)
            in_game = common.check_game_status(player)

    if in_game:
        common.fight_boss()
    else:
        common.game_over()

    your_time = int(time() - start)
    common.save_highscores(player, your_time, level)


def show_highscores():
    common.print_text("arts/scores.txt")

    headers = ["name", "time spent", "level"]
    with open("high_score.txt", "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(",") for element in lines]
    print (tabulate(table, headers, tablefmt="fancy_grid"))

    common.wait_for_enter()




def print_error_message(message):
    print(message)


if __name__ == '__main__':
    main()
