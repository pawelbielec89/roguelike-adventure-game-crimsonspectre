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