test = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        total += v

    print(f"Total number of items: {total}")


def addToInventory(inventory, addedItems):

    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
