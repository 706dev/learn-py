from item import Item

class Inventory:
    def __init__(self, gold: int = 0):
        self.items = []
        self.gold = gold

    def __repr__(self):
        return f'Gold: {self.gold}\n{self.items}'

    def add_gold(self, amount: int):
        self.gold += amount

    def remove_gold(self, amount: int):
        if (self.gold - amount) >= 0:
            self.gold -= amount
        else:
            return

    def get_item(self, item_id: int) -> (int, Item):
        for index, item in enumerate(self.items):
            if item.uid == item_id:
                return index, item

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item_id: int):
        index, item = self.get_item(item_id)
        if item:
            self.items.pop(index)
    
    def sell_item(self, item_id: int, buyer):
        index, item = self.get_item(item_id)
        if item:
            value = item.value
            if buyer.inventory.gold >= value:
                self.remove_item(item_id)
                self.add_gold(value)
                buyer.inventory.add_item(item)
                buyer.inventory.remove_gold(value)
                print(f'You have sold {item.name} for {item.value}')
            else:
                print('Shop is broke!')
        else:
            print('Item does not exist')

    def transfer_item(self, item, new_inventory):
        new_inventory.add_item(item)
        self.remove_item(item.uid)

    def transfer_all_items(self, new_inventory):
        for item in self.items:
            self.transfer_item(item, new_inventory)
            