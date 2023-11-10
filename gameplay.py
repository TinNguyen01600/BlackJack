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
        
        if player_val > 21:   # Player busted
            print(f'You lost your bet ({player.bet} chips).')
        elif player.blackjack:  
            if dealer.blackjack:
                print('Dealer and Player pushed. The bet is returned')
                player.chips += (player.bet)
            else:
                if player % 2 == 0: profit = int(player/2)
                else:   profit = player/2
                print(f'You win your bet ({player.bet} chips) and profit ({profit} chips).')
                player.chips += (2*(player.bet) + player.bet/2)
        else:
            if dealer_val > 21: # Dealer busted (>21) and Player not busted (<21)
                print(f'You win your bet ({player.bet} chips).')
                player.chips += 2*(player.bet)
            elif dealer.blackjack:
                print(f'You lost your bet ({player.bet} chips).')
            else:
                if player_val > dealer_val:
                    print(f'You win your bet ({player.bet} chips).')
                    player.chips += 2*(player.bet)
                elif player_val == dealer_val:
                    print('Dealer and Player pushed. The bet is returned')
                    player.chips += (player.bet)
                else:
                    print(f'You lost your bet ({player.bet} chips).')
        print(player.chips)

if __name__ == '__main__':
    # Setting up deck, players and dealer
    deck = set_up_deck()
    players_list = set_up_players([])
    dealer = classes.Dealer()
    
    # Placing players' bets and dealing cards
    os.system('cls')
    print('New round.')
    for i in players_list:
        print(f'Player {i.name} has {i.chips} chips.')
    print()
    set_up_bet(players_list)
    dealing(players_list, deck, dealer)
    
    # Displaying players' and dealer's cards
    print('Dealer\'s cards ', end='')
    dealer.show_1_card()
    for i in players_list:
        print(f'Player {i.name}\'s cards ', end='')
        i.show_all_cards()
    
    # Each player's turn and decision
    for i in players_list:
        print()
        print(f'Player {i.name}\'s turn. Your cards ', end='')
        player_turn(i, deck)
    input('Press Enter to continue...')
    
    # Dealer's turn and reveal their cards
    os.system('cls')
    print('Dealer\'s turn.')
    dealer_turn(dealer, deck)
    input('Press Enter to continue...')
    
    # Determination of Winners, Paying and Collecting Bets
    os.system('cls')
    payout(players_list, dealer)
    input('Press Enter to continue...')
    