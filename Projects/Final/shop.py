from inventory import Inventory

class Shop:
    def __init__(self, uid: int, name: str):
        self.name = name
        self.inventory = Inventory(gold=100)

    def __repr__(self):
        return (
            f'==== Shop {self.name} ====\n'
            f'Inventory:\n{self.inventory}\n'
        )


