import common
import os
import player_module
from board_module import Board
from random import randint


def main():
    monsters = [["Rat", "\033[30;47mR\033[0m", 20, 5, 2], 
                ["Bat", "\033[30;47mB\033[0m", 40, 10, 4], 
                ["Snake", "\033[30;47mS\033[0m", 60, 15, 6]]
    monsters_list = []
    number_of_monsters = randint(10,20)
    inventory = {}

    player = player_module.Player(1,1,"Player", "V", 100, 10, 10, "male", 100, inventory)

    for monster_properties in monsters:
        monster = player_module.Character(*monster_properties)
        monsters_list.append(monster)

    dungeon = Board(40,100)
    dungeon.generate_dungeon(player.avatar, monsters_list)

    while True:
        dungeon.draw_board()
        player.move(dungeon)

if __name__ == "__main__":
    main()