
class Player:
    def __init__(self, name: str):
        self.name = name
        self.title = ""
        self.moves = []
        self.cards = []
        hp = 100
        atk = 10
        defc = 10
        spatk = 10
        spdef = 10
        spe = 10

    def __repr__(self):
        return f"{self.name} | {self.desc}"
    