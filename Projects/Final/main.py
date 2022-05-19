from character import Character
from shop import Shop
from item import Item, Weapon

def main():
    player = Character(1, "Psuedo")
    enemy = Character(2, "Monster")
    sword = Weapon(1, "Sword", 100, 5000)
    dagger = Weapon(2, "Dagger", 10, 10)

    player.inventory.add_item(sword)
    enemy.inventory.add_item(dagger)

    player.equip(1)
    enemy.equip(2)

    print(player)
    print(enemy)

    player.attack(enemy)

    print(enemy)

    player.loot(enemy)

    print(player)



if __name__ == "__main__":
    main()