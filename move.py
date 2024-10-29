class Move:
    def __init__(self, id: int, name: str, desc: str, rarity: str, special: bool):
        self.id = id
        self.name = name
        self.desc = desc
        self.rarity = rarity
        self.special = special

    def __repr__(self):
        return f"{self.name} | {self.desc}"
    