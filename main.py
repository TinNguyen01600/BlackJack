import classes
import gameplay
import os

def play_again():
    pass

def play():
    # Setting up deck, players and dealer
    deck = gameplay.set_up_deck()
    players_list = gameplay.set_up_players([])
    dealer = classes.Dealer()
    
    # Placing players' bets and dealing cards
    os.system('cls')
    print('New round.')
    for i in players_list:
        print(f'Player {i.name} has {i.chips} chips.')
    print()
    gameplay.set_up_bet(players_list)
    gameplay.dealing(players_list, deck, dealer)
    
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
        gameplay.player_turn(i, deck)
    input('Press Enter to continue...')
    
    # Dealer's turn and reveal their cards
    os.system('cls')
    print('Dealer\'s turn.')
    gameplay.dealer_turn(dealer, deck)
    input('Press Enter to continue...')
    
    # Determination of Winners, Paying and Collecting Bets
    os.system('cls')
    gameplay.payout(players_list, dealer)
    input('Press Enter to continue...')

if __name__ == '__main__':
    play()