'''
This file contains stage functions in a BlackJack round
'''

import classes
import os

def set_up_deck():
    new_deck = classes.Deck()
    new_deck.shuffle()
    return new_deck

def set_up_players(players_list):
    num_of_players = classes.Player.get_integer('Number of Players: ')
    for i in range(num_of_players):
        print(f'Player {i+1}. ')
        player = classes.Player()
        players_list.append(player)
        print()
    return players_list

def set_up_bet(players_list):
    for i in players_list:
        i.place_bet()
        print()  

def dealing(players_list, deck, dealer):
    num_of_players = len(players_list)
    for _ in range(2):
        for i in range(num_of_players):
            players_list[i].add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())
        
def print_player_infor(p):
    print(f'Player {p.name} bets {p.bet} chips.')
    print(f'Player {p.name}\'s cards ', end='')
    i.show_all_cards()

def get_player_choice(p):
    possible_choices = ['Hit', 'Stand', 'Double Down']
    if p.cards[0].rank == p.cards[1].rank:
        possible_choices.append('Split')
    for i in range(len(possible_choices)):
        print(f'{i+1}. {possible_choices[i]}')
        
    choice = classes.Player.get_integer('Enter your choice: ')
    while choice < 0 or choice > len(possible_choices):
        print('Invalid choice. Try again.')
        choice = classes.Player.get_integer('Enter your choice: ')
    return choice

def player_turn(player, choice, deck):
    if player.value == 21:
        print('You got blackjack.')
    else:
        choice = get_player_choice(player)
        if choice == 1: # Hit
            player.add_card(deck.deal_one())
            print_player_infor(player)
            if player.value > 21:
                print(f'Player {player.name} busting')
            else:
                player_turn(player, get_player_choice(player), deck)
        elif choice == 2:   # Stand
            pass
        elif choice == 3:   # Double down
            pass
        elif choice == 4:   # Split (only with same rank cards )
            pass

if __name__ == '__main__':
    deck = set_up_deck()
    players_list = set_up_players([])
    dealer = classes.Dealer()
    
    set_up_bet(players_list)
    dealing(players_list, deck, dealer)
    
    os.system('cls')
    print('Dealer\'s cards ', end='')
    dealer.show_1_card()
    print()
    for i in players_list:
        print_player_infor(i)
        print()
    
    for i in players_list:
        print(f'Player {i.name}\'s turn.')
        player_turn(i, get_player_choice(i), deck)
    