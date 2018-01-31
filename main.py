import common
import os
from player_module import Character
from board_module import Board


def main():

    x = 1 
    y = 1

    dungeon = Board(40,100)
    dungeon.generate_dungeon()

    player_character = Character(1,1,"Player", "\033[31;47mV\033[0m", 100, 10, 10, "male")

    while True:
        os.system("clear")
        dungeon.draw_board()
        player_character.move(dungeon)


if __name__ == "__main__":
    main()