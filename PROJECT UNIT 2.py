import random
import time

chips = 500
play = "Y"

while chips > 0 and play == "Y":
    dealer_hand = []  # Use lists to keep track of cards at the start
    dealer_hand2 = []  # Since an Ace can be a 1 or an 11 we have two lists, one where ace is treated as 1 and one where it is treated as 11

    player_hand = []
    player_hand2 = []

    print("You currently have %d chips" % chips)
    bet = chips + 1  # Want to make sure user inputs a valid bet
    while bet > chips:  # You can't bet more chips than you currently have
        bet = int(input("\nHow many chips would you like to bet: "))

    for i in range(2):

        dealer_card = random.randint(1, 13)
        if dealer_card == 11 or dealer_card == 12 or dealer_card == 13:  # account for jack, queen, king, should be 10
            dealer_card = 10

        if dealer_card == 1:  # If they are dealt an ace we need to account that it can be an 11 as well
            dealer_hand2.append(11)
        else:
            dealer_hand2.append(dealer_card)
        dealer_hand.append(dealer_card)  # Put the dealt card into the dealer's list

        player_card = random.randint(1, 13)
        if player_card == 11 or player_card == 12 or player_card == 13:  # Same logic as dealer card
            player_card = 10

        if player_card == 1:
            player_hand2.append(11)

        else:
            player_hand2.append(player_card)

        player_hand.append(player_card)

    player = sum(player_hand) # Figure out what each players score is
    player2 = sum(player_hand2) # Keep track of player 2 for aces

    dealer = sum(dealer_hand)
    dealer2 = sum(dealer_hand2)

    print("\nThe dealer is showing %d" % dealer_hand[0])  # Only show the first card, if it is a 1 then the user should assume it is an Ace
    print("\nYou are showing %d and %d" % (player_hand[0], player_hand[1]))  # Show your 2 cards
    hit = input("\nWould you like to hit(Y/N): ").title()  # Use .title to protect against lowercase input

    while (player <= 21 or player2 <= 21) and hit == "Y":  # Run the loop while the player hasn't busted and they want to hit
        card = random.randint(1, 13)
        if card == 11 or card == 12 or card == 13:  # Adjust if they are dealt a royal card
            card = 10

        print("\nYou were dealt a %d" % card)
        if card == 1:  # Account for an ace being dealt
            if (player + 11) < 21:  # If the hand wouldn't bust if the ace is an 11 then we switch it to 11
                player = player + 11

            else:  # Otherwise we keep it as a 1 if it would make the player bust
                player = player + card

            if (player2 + 11) < 21:
                player2 = player2 + 11
            else:

                player2 = player2 + card

        else:
            player = player + card
            player2 = player2 + card

        if player <= 21 or player2 <= 21:  # If the player didn't bust we need to figure out what hand(s) they have
            if player == player2:  # If no aces have been dealt we know that these 2 should be equal
                print("\nYou are showing %d" % player)
            else:  # Show them the two hands they have with the way the ace is played, note that one hand could be a bust
                print("\nYou have %d or %d" % (player, player2))

            hit = input("\nWould you like to hit(Y/N): ").title()

    if player > 21 and player2 > 21:  # If the player busted we let the user know and take away their bet from their chips
        chips = chips - bet
        print("\nSorry, you busted this hand")

    else:
        print("\nThe dealer's hand is %d" % max(dealer, dealer2))  #Since the dealer has to stop on 17 we show the max score they have
        if player > 21:  #Figure out which is the highest non bust score the player has with these if statements
            player_score = player2

        elif player2 > 21:
            player_score = player

        else:
            player_score = max(player, player2)

        while max(dealer, dealer2) < 17:  # The loop should run until the dealer has a hand above 16
            time.sleep(2)  # Put this here to have the cards be dealt more slowly to better simulate a real casino, Marinah's brother taught me this
            card = random.randint(1, 13)
            if card == 11 or card == 12 or card == 13:  # Adjust for royalty
                card = 10
            print("\nDealer was dealt a %d" % card)
            if (card + dealer) > 21 and (card + dealer2) > 21:  # If this is true we know the dealer busted
                dealer = 22  # Set the scores to 22 so we can identify they are > 21
                dealer2 = 22

            else:
                if card == 1:  # Adjust for ace, same logic as the player hand
                    if (11 + dealer) <= 21:
                        dealer = dealer + 11

                    else:
                        dealer = dealer + card

                    if (11 + dealer2) <= 21:
                        dealer2 = dealer + 11

                    else:
                        dealer2 = dealer + card

                else:
                    dealer = dealer + card
                    dealer2 = dealer2 + card

                if dealer > 21 and dealer2 < 17:  # If one of the hands busted we want to reset it to what the non bust hand is so our while loop continues
                    dealer = dealer2

                elif dealer < 17 and dealer2 > 21:
                    dealer2 = dealer

            if dealer <= 21 or dealer2 <= 21:  # Let the user know where the dealer is at in the hand
                if dealer == dealer2:
                    print("\nThe dealer is showing %d" % dealer)
                else:
                    print("\nThe dealer has %d or %d" % (dealer, dealer2))

        if (dealer > 21) and (dealer2 > 21):  # Check if the dealer busted, if they did then add the bet to chips
            print("\nDealer busted, you win the hand!")
            chips = chips + bet

        else:
            if (dealer > 21)and (dealer2 <= 21):  #Same logic as player_score
                dealer_score = dealer2

            elif (dealer <= 21) and (dealer2 > 21):
                dealer_score = dealer

            else:
                dealer_score = max(dealer, dealer2)

            if dealer_score > player_score:  # Figure out who won the hand and assign chips
                print("\nThe dealer has a better hand (%d) and has won the round!" % dealer_score)
                chips = chips - bet

            elif dealer_score < player_score:
                print("\nYou have a better hand (%d) than the dealer and have won the round!" % player_score)

            else:
                print("\nYou and the dealer have the same hand (%d) and have tied the round!" % player_score)

    if chips > 0:  # If the player still has chips let them play another hand if they wish
        play = input("\nWould you like to play another hand (Y/N): ").title()

if chips <= 0:
    print("\nYou ran out of chips!")

print("\nThanks for playing!")
#new line