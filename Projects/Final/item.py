class Item:
    def __init__(self, uid: int, name: str, value: int):
        self.uid = uid
        self.name = name
        self.value = value
    
    def __repr__(self):
        return f'\nName: {self.name}\nValue: {self.value}\n'