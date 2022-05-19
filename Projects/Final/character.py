from item import Item
from inventory import Inventory

class Character:
    def __init__(self, uid: int, name: str):
        self.uid = uid
        self.name = name
        self.health = 100
        self.damage = 10
        self.inventory = Inventory()
        self.reputation = 50
        self.equipped = None
        self.is_alive = True

    def __repr__(self):
        return (
            f'==== Character: {self.name} ====\n'
            f'Health: {self.health}\n'
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