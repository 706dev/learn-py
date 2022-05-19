class Item:
    def __init__(self, uid: int, name: str, value: int):
        self.uid = uid
        self.name = name
        self.value = value
    
    def __repr__(self):
        return f'\nName: {self.name}\nValue: {self.value}\n'

class Weapon(Item):
    def __init__(self, uid, name, value, damage):
        Item.__init__(self, uid, name, value)
        self.damage = damage