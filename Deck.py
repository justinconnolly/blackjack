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

        def __init__(self, value, suit, owner='dealer', visible=False):
            self.value = value
            self.suit = suit
            self.size = 10
            self.owner = owner
            self.visible = visible

        def __str__(self):
            return f"{self.value if self.value not in self.faces else self.faces[self.value]} of {self.suits[self.suit]}"


        def pretty_card(self, vis):
            vis = True
            if not vis:
                ret_str = [
                    f" {'_' * self.size} ",
                    f"|{'?|':>11}",
                    f"|{'|':>11}",
                    f"|{'Black'.center(10)}|",
                    f"|{'Jack'.center(10)}|",
                    f"|{'|':>11}",
                    f"|{'|':>11}",
                    f"|?{'|':>10}",
                    f" {'_' * self.size} "
                ]
            else:
                ret_str = [
                f" {'_' * self.size} ",
                f"|{(self.value if self.value not in self.faces else self.faces[self.value][:1]):>9}{self.suits[self.suit][:1]}|",
                f"|{'|':>11}",
                f"|{str(self.value if self.value not in self.faces else self.faces[self.value]).center(10)}|",
                f"|{'of'.center(10)}|",
                f"|{self.suits[self.suit].center(10)}|",
                f"|{'|':>11}",
                f"|{(str(self.value) if self.value not in self.faces else self.faces[self.value][:1]) + self.suits[self.suit][:1]:<10}|",
                # f"|{(self.value if self.value not in self.faces else self.faces[self.value][:1])}{self.suits[self.suit][:1]}{'|':>9}",
                f" {'_' * self.size} "
                ]
            return ret_str

    # I think this really should just inherit from Deck? Deck could be the parents with Hand and playing_deck children
    class Hand:
        def __init__(self):
            self.hand = []

        def add_card(self, card):
            self.hand.append(card)

        def print_hand(self, vis):
            hand = self.hand[0].pretty_card(vis)
            for i in range(1, len(self.hand)):
                for j,line in enumerate(self.hand[i].pretty_card(True)):
                    hand[j] += line
            for line in hand:
                print(line)

        def get_value(self):
            # hand_value = sum([x.value for x in self.hand])
            if len(self.hand) > 0:
                return self.hand[-1].value
            else:
                return "Empty hand."


    def __init__(self):
        self.deck = [self.Card(x,y) for x in range(1, 14) for y in range(4)]
    
    def __str__(self):
        return '\n'.join([str(card) for card in self.deck])

    def shuffle(self):
        random.shuffle(self.deck)
    
    # just return a card
    def draw(self, player):
        if len(self.deck) < 1:
            print("Not enough cards remaining in the deck.")
            return
        card = self.deck.pop(0)
        card.visible = player.user
        return card

    def deal(self, players: int, visible: bool) -> list(list('Card')):
        if players > len(self.deck):
            print("Not enough cards remaining in the deck.")
            return
        hands = [self.Hand() for x in range(players)]
        for i in range(players):
            # print(hands[i])
            # print(self.deck[i])
            # print(type(hands[i % players]))
            # hands[i % players].add_card(self.deck[i])
            hands[i].add_card(self.deck.pop(0))
        return hands


if __name__ == "__main__":
    deck = Deck()
    print(piece for piece in list(deck.deck[5].pretty_card()))
    for piece in deck.deck[5].pretty_card():
        print(piece)
    deck.shuffle()
    hands = deck.deal(2,False)
    # for card in 
    # print(deck)
    # print(f"|{'hello'.center(10)}|")
    # print(f"{'hello':>10}")