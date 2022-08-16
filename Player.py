import Deck


class Player:
    def __init__(self, name="Bot", user=False):
        self.hands = Deck.Deck.Hand()
        self.name = name
        self.user = user
        self.score = 0

    def print_hand(self):
        print(f"{self.name}:")
        print(f"Score: {self.score}")
        self.hands.print_hand(self.user)
    
    def get_value(self):
        return self.hands.get_value()