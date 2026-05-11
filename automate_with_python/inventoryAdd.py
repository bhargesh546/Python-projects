def main():
    inv = {'gold coin': 40, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)

def add_to_inventory(inventory: dict, added_items: list):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

def display_inventory(inventory: dict):
    print("Inventory:")
    total_items = 0
    for k, v in inventory.items():
        total_items += v
        print(f"{v} {k}")
    print(f"Total number of items: {total_items}")

if __name__ == "__main__":
    main()
