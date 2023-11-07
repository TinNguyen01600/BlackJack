import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                c = Card(suit, rank)
                self.deck.append(c)
    def __str__(self):
        for i in self.deck:
            print(i)
        return ''
    def shuffle(self):
        random.shuffle(self.deck)
    def deal_one(self):
        return self.deck.pop()  # deal the last (top) card of the deck to player

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, new_card):
        self.cards.append(new_card)
    def show_all_cards(self):
        print('[', end='')
        for i in self.cards:
            print(i, end=' ')
        print(']')
        
class Player(Hand):
    def __init__(self):
        super().__init__()
        self.name = input('Enter your name: ')
        self.chips = self.get_integer('Buy in: ')
    def get_integer(text):
        while True:
            try:
                result = int(input(text))
            except:
                print('Not a number. Try again')
                continue
            else:
                break
        return result
    def __str__(self):
        return f'{self.name} has {self.chips} chips.'

if __name__ == '__main__': 
    player1 = Player()
    print(player1)