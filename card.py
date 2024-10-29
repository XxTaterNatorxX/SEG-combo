class Card:
    def __init__(self, id: int, consumable: bool, name: str, desc: str, rarity: str):
        self.id = id
        self.consumable = consumable
        self.name = name
        self.desc = desc
        self.rarity = rarity
        self.priority = 0


    def __repr__(self):
        return f"{self.name} | {self.desc}"
    