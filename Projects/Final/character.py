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

    def __repr__(self):
        return (
            f'==== Character: {self.name} ====\n'
            f'Health: {self.health}\n'
            f'Inventory:\n{self.inventory}\n'
        )


