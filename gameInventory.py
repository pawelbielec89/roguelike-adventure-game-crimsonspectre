def add_to_inventory(inventory, added_items):
    for key, value in added_items.items():
        if key in inventory:
            inventory[key][0] += value[0]
            inventory[key][1] += value[1]
        else:
            inventory.update(added_items)
    del added_items[key]


def print_inventory(inventory):
    sum_count = 0
    sum_weight = 0
    count = "count"
    weight = "weight"
    key_name = "item name"

    max_len_key = [key for key in inventory.keys()]
    lenght_key = len(max(max_len_key))

    if lenght_key < len(key_name):
        lenght_key = len(key_name)

    headers = ("{:>" + str(lenght_key + 3) + "}" "{:>" + str(len(count) + 3) + "}"\
    "{:>" + str(len(weight) + 3) + "}").format(key_name, count, weight)
    print("Inventory:")
    print(headers)
    print("-"*len(headers))

    for key, value in inventory.items():
        sum_count += value[0]
        sum_weight += value[1]
        print (("{:>" + str(lenght_key + 3) + "}" "{:>" + str(len(count) + 3) + "}"\
        "{:>" + str(len(weight) + 3) + "}").format(key, value[0], value[1]))
    print("-"*len(headers))
    print(("{:>" + str(lenght_key + 3) + "}" "{:>" + str(len(count) + 3) + "}"\
    "{:>" + str(len(weight) + 3) + "}").format("totality", sum_count, sum_weight))
