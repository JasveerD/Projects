import random
from sys import exit


print('''Commands:
hit = to get another card
stop = to stop the game''')

dealer_total = 0
player_total = 0

while dealer_total <= 21 and player_total <= 21:

    cmd = input('Enter Cmd: ').strip().lower()

    if cmd == 'hit':
        player_total = player_total + random.randrange(1, 11)
        dealer_total = dealer_total + random.randrange(1, 11)
        print(player_total)

    if player_total > 21:
        print("Dealer: " + str(dealer_total))
        print('Player: ' + str(player_total))
        print('Dealer Wins')
        exit()

    if dealer_total > 21:
        print("Dealer: " + str(dealer_total))
        print('Player: ' + str(player_total))
        print("Player Wins")
        exit()

    elif cmd == 'stop':
        break

print('Player: ' + str(player_total) + '   ' + 'Dealer: ' + str(dealer_total))

if player_total > dealer_total:
    print('Player Wins')
elif player_total < dealer_total:
    print('Dealer Wins')
else:
    print("Draw")
