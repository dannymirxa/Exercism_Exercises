
from collections import Counter

def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inventory = {}
    for item in items:
        inventory.setdefault(item, items.count(item) )
    return inventory

# print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    return dict(Counter(inventory) + Counter(create_inventory(items)))

# print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    # return dict(Counter(inventory) - Counter(create_inventory(items)))
    # combined_inventory = inventory.copy()
    # combined_inventory.update(create_inventory(items))
    # return combined_inventory

    for key, value in inventory.items():
        if key in items:
            if inventory[key] - create_inventory(items)[key] < 0:
                inventory[key] = 0
            else:
                inventory[key] -= create_inventory(items)[key]

    
    return inventory

"""{"iron": 1, "diamond": 3, "gold": 0}"""

# print(decrement_items({"wood": 2, "iron": 3, "diamond": 1},
#                               ["wood", "wood", "wood", "iron", "diamond", "diamond"]))


# inventory = {"coal":2, "wood":1, "diamond":2}
# print({k: v for k,v in inventory.items() if k != "coal"})

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    pass

inventory = {"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}

print([(k,v) for k,v in inventory.items() if v > 0])

# print(list_inventory(inventory))

# print(tuple({"coal":7}))