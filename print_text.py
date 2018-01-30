import os


def print_menu(list_options, play):
    os.system("clear")
    with open("print_menu.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line[:-1])

    print("\t\t\t\t", play)
    for i in range(len(list_options)):
        print("\t", list_options[i])



def print_scores():
    with open("scores.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line[:-1])
    print("\n")
