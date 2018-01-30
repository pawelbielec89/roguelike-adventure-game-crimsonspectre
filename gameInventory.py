# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
import csv
import sys


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    print("\nAdded to inventory:", added_items, "\n")


def print_table(inventory):
    print("\nInventory:")
    lenght_item = 0
    lenght_count = 0
    title_number = "count"
    item_name = "item name"

    for item, count in inventory.items():
        if lenght_item < len(item):
            lenght_item = len(item)
        if lenght_count < len(str(count)):
            lenght_count = len(str(count))
    if lenght_count < len(title_number):
        lenght_count = len(title_number)
    if lenght_item < len(item_name):
        lenght_item = len(item_name)
    headers = ("{:>" + str(lenght_count + 2) + "}" "{:>" + str(lenght_item + 2) + "}").format("count", "item name")
    print(headers)
    print("-"*len(headers))

    for key, value in inventory.items():
        print (("{:>" + str(lenght_count + 2) + "}" "{:>" + str(lenght_item + 2) + "}").format(value, key))

    print("-"*len(headers))
    print("Total number of items: ", sum(inventory.values()), "\n")


def open_the_door(inventory):
    if "key" in inventory:
        for element in dragon_inventory:
            inventory[element] = 1
        del inventory["sword"]
        return True
    else:
        print("\nYou don't have any key\n")


# Main function sets initial variables and stores rest of the functions
def main():
    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


if __name__ == '__main__':
    main()
