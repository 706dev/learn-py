from character import Character
from shop import Shop
from item import Item

def main():
    player = Character(1, "Psuedo")
    shop = Shop(1, "Shop")
    sword = Item(1, "Sword", 99)

    player.inventory.add_item(sword)
    print(player)
    print(shop)

    player.inventory.sell_item(1, shop)
    print(player)
    print(shop)

if __name__ == "__main__":
    main()