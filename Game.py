from Deck import Deck
from Player import Player

class Game:
    def __init__(self, players, handsize):
        self.deck = Deck()
        self.players = [Player() for x in range(players)]
        self.handsize = handsize

    def deal(self):
        hands = self.deck.deal(len(self.players), self.handsize)
        for i,v in enumerate(hands):
            self.players[i].hand = v

if __name__ == "__main__":
    game = Game(2,2)
    game.deal()
    for player in game.players:
        player.print_hand()
    # print(game.deck)