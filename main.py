import common
import os
import player_module
from board_module import Board


def main():
    inventory = {}

    player = player_module.Player(1,1,"Player", "V", 100, 10, 10, "male", 100, inventory)

    dungeon = Board(40,100)
    dungeon.generate_dungeon(player.avatar)

    while True:
        dungeon.draw_board()
        player.move(dungeon)

if __name__ == "__main__":
    main()