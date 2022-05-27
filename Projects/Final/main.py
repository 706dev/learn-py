from game import Game


def main():
    game = Game("Psuedo")

    game.attempt_player_move('up')
    print(game.characters)

    # player = Character(1, "Psuedo")
    # enemy = Character(2, "Monster")
    # sword = Weapon(1, "Sword", 100, 5000)
    # dagger = Weapon(2, "Dagger", 10, 10)

    # player.inventory.add_item(sword)
    # enemy.inventory.add_item(dagger)

    # player.equip(1)
    # enemy.equip(2)

    # print(player)
    # print(enemy)

    # player.attack(enemy)

    # print(enemy)

    # player.loot(enemy)

    # print(player)





if __name__ == "__main__":
    main()