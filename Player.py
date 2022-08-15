class Player:
    def __init__(self, name="Bot"):
        self.hand = []
        self.name = name
    def print_hand(self):
        hand = self.hand[0].pretty_card()
        for i in range(1, len(self.hand)):
            for j,line in enumerate(self.hand[i].pretty_card()):
                hand[j] += line
        for line in hand:
            print(line)