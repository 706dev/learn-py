from item import Item
from inventory import Inventory

class Character:
    def __init__(self, uid: int, name: str):
        self.uid = uid
        self.position = (0, 0)
        self.name = name
        self.health = 100
        self.damage = 10
        self.inventory = Inventory()
        self.reputation = 50
        self.equipped = None
        self.is_alive = True

    def __repr__(self):
        return (
            f'==== Character: {self.uid} {self.name} ====\n'
            f'Health: {self.health}\n'
            f'Location: {self.position}\n'
            f'Inventory:\n{self.inventory}\n'
        )

    def equip(self, weapon_id):
        index, weapon = self.inventory.get_item(weapon_id)
        if weapon:
            self.equipped = weapon
        else:
            print('Weapon does not exist')

    def attack(self, target):
        if target.is_alive:
            weapon = self.equipped
            if weapon:
                damage = weapon.damage + (self.damage//10) 
            else:
                damage = 1
            
            target.health -= damage
            if target.health < 0:
                target.health = 0
                target.is_alive = False
        else:
            print(f'{target.name} ded')

    def loot(self, target):
        if not target.is_alive:
            target.inventory.transfer_all_items(self.inventory)
            self.inventory.gold += target.inventory.gold
            target.inventory.gold = 0
        else:
            print(f"You can't loot an alive target!")



    def get_new_position(self, direction):

        x = self.position[0]
        y = self.position[1]

        if direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        elif direction == 'right':
            x += 1
        elif direction == 'left':
            x -= 1
        
        return (x, y)

    def update_position(self, new_position):
        self.position = new_position