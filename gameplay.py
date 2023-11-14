'''
This file contains stage functions in a BlackJack round
'''

import classes
import os
import time

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
    print('Dealing')
    for _ in range(3):
        time.sleep(0.4), print('.')
    for _ in range(2):
        for i in range(num_of_players):
            players_list[i].add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())      

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

def player_turn(player, deck):
    player.show_all_cards()
    if player.value == 21:
        if len(player.cards) == 2:
            print('You got blackjack.')
            player.blackjack = True
        else:   print('You got 21.')
    else:
        choice = get_player_choice(player)
        if choice == 1: # Hit
            player.add_card(deck.deal_one())
            if player.value > 21:
                player.show_all_cards()
                print(f'Player {player.name} busting')
            else:
                player_turn(player, deck)
        elif choice == 2:   # Stand
            pass
        elif choice == 3:   # Double down
            pass
        elif choice == 4:   # Split (only with same rank cards )
            pass

def dealer_turn(dealer, deck):
    print('Dealer\'s cards ', end='')
    dealer.show_all_cards()
    if dealer.value == 21:  
        if len(dealer.cards) == 2:
            print('Dealer got blackjack.')
            dealer.blackjack = True
        else:   print('Dealer got 21.')
    elif dealer.value <= 16:
        print('Dealer hits 1 card.')
        dealer.add_card(deck.deal_one())
        dealer_turn(dealer, deck)
    else: print('Dealer stands.')

def payout(players_list, dealer):
    print('Dealer\'s cards ', end='')
    dealer.show_all_cards()
    dealer_val = dealer.value
    for player in players_list:
        print()
        print(f'Player {player.name}\'s cards ', end='')
        player.show_all_cards()
        player_val = player.value
        
        if player_val > 21:   
            print('Player busted.', end=' ')
            player.lose_bet()
        elif player.blackjack:  
            if dealer.blackjack:  print('Dealer and Player pushed. The bet is returned')
            else:
                print('Player got blackjack.', end=' ')
                if player.bet % 2 == 0: profit = int(player.bet/2)
                else:   profit = player.bet/2
                player.win_bet(player.bet + profit)
        else:
            if dealer_val > 21:
                print('Dealer busted.', end=' ')
                player.win_bet(player.bet)
            elif dealer.blackjack:  
                print('Dealer got blackjack.', end=' ')
                player.lose_bet()
            else:
                if player_val > dealer_val:
                    print('Player is closer to 21.', end=' ')
                    player.win_bet(player.bet)
                elif player_val == dealer_val:  print('Dealer and Player pushed. The bet is returned')
                else:   
                    print('Dealer is closer to 21.', end=' ')
                    player.lose_bet()
        print(player)

if __name__ == '__main__':
    pass
    