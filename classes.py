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
        for i in range(-10, 0, 1):
            print(self.deck[i])
        return ''
    def shuffle(self):
        random.shuffle(self.deck)
    def deal_one(self):
        return self.deck.pop()  # deal the last (top) card of the deck to player
        
class Hand:
    def __init__(self):
        self.cards = []
        self._value = 0
        self._aces = False
    def add_card(self, new_card):
        self.cards.append(new_card)
    def show_all_cards(self):
        print('[ ', end='')
        for i in self.cards:
            print(i, end='| ')
        print(']')
    @property
    def value(self):
        return self.calculate_value()
    @property
    def aces(self):
        num = 0
        for i in self.cards:
            if i.rank == 'Ace': num += 1
        return num
    def calculate_value(self):
        val = 0
        for i in self.cards:
            val += values[i.rank]
        if val > 21 and self.aces > 0:  val -= 10
        return val

class Player(Hand):
    def __init__(self):
        super().__init__()
        self.name = input('Enter your name: ')
        self.chips = self.get_integer('Buy in: ')
    @staticmethod
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
        string = f'Player {self.name} has {self.chips} chips. '
        string += f'His cards [ '
        for i in self.cards:
            string += f'{i}| '
        string += ']'
        return string
    def place_bet(self):
        self.bet = self.get_integer(f'Player {self.name} bets: ')
        if self.bet > self.chips:
            print('Not enough chips.')
            self.place_bet()
        else:
            self.chips -= self.bet

class Dealer(Hand):
    def show_1_card(self):
        print('[ Hole card | ', self.cards[1], ']')

if __name__ == '__main__': 
    new_deck = Deck()
    new_deck.shuffle()
    
    p1 = Player()
    for _ in range(2):
        p1.add_card(new_deck.deal_one())
    print(p1)
    print(p1.aces)