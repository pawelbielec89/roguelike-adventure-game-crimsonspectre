import os


def print_menu(list_options):
    os.system("clear")
    with open("print_menu.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line[:-1])

    for i in range(len(list_options)):
        print("\t", list_options[i])


def printed(files):
    with open(files, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line[:-1])
    print("\n")
