import random

class Deck:

    class Card:
        suits = {
            0: "Spades",
            1: "Hearts",
            2: "Diamonds",
            3: "Clubs"
        }
        faces = {
            11: "Jack",
            12: "Queen",
            13: "King",
            1: "Ace"
        }

        def __init__(self, value, suit):
            self.value = value
            self.suit = suit
            self.size = 10
        
        def __str__(self):
            return f"{self.value if self.value not in self.faces else self.faces[self.value]} of {self.suits[self.suit]}"


        def pretty_card(self):
            ret_str = [
            f" {'_' * self.size} ",
            f"|{(self.value if self.value not in self.faces else self.faces[self.value][:1]):>9}{self.suits[self.suit][:1]}|",
            f"|{'|':>11}",
            f"|{str(self.value if self.value not in self.faces else self.faces[self.value]).center(10)}|",
            f"|{'of'.center(10)}|",
            f"|{self.suits[self.suit].center(10)}|",
            f"|{'|':>11}",
            f"|{(self.value if self.value not in self.faces else self.faces[self.value][:1])}{self.suits[self.suit][:1]}{'|':>9}",
            f" {'_' * self.size} "]
            return ret_str

    def __init__(self):
        self.deck = [self.Card(x,y) for x in range(1, 14) for y in range(4)]
    
    def __str__(self):
        return '\n'.join([str(card) for card in self.deck])

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, players: int, cards: int) -> list(list('Card')):
        if players * cards > len(self.deck):
            print("Not enough cards remaining in the deck.")
            return
        hands = [[] for x in range(players)]
        for i in range(players * cards):
            hands[i % players].append(self.deck.pop(0))
        return hands

if __name__ == "__main__":
    deck = Deck()
    print(piece for piece in list(deck.deck[5].pretty_card()))
    for piece in deck.deck[5].pretty_card():
        print(piece)
    deck.shuffle()
    hands = deck.deal(2,5)
    # for card in 
    # print(deck)
    # print(f"|{'hello'.center(10)}|")
    # print(f"{'hello':>10}")