'''--------------Functions For Login---------------'''


def Names(firstname, lastname):
    '''This function checks if the firstname and lastname inputted by the user are only letters and do not already exist in the database. If firstname="3derfr" and lastname="456" it would return 2. If the firstname and lastname already existed in the lists of names, then it would return 2. If the name does not already exist, and is alphabtical, it returns 1.'''
    if firstname.title() in f_names and lastname.title() in l_names:
        return 2
    elif firstname.isalpha() and lastname.isalpha():
        return 1
    else:
        return 3


def Country(usercountry):
    '''This function checks if the country inputted by the user in title format matches any countries in the list of all countries in the world. If it exists, then it returns 1, if it isn't in the list, it returns 2.'''
    if usercountry.title() in countrylist:
        return 1
    else:
        return 2


def User(username):
    '''This function checks if a username already exists and if it is between 6-12 characters. If a username is in the list of usernames, the function returns 3. If it is not in the list of usernames and is not between 6-12 characters, it returns 2. If it is between 6-12 characters and does not already exist, the function returns 1.'''
    if username in usernames:
        return 3
    elif len(username) < 6 or len(username) > 12:
        return 2
    else:
        return 1


def NewPassword(password):
    '''This function checks if a password is between 8-15 characters, has at least one character that is a digit, and has at least one uppercase character. If all of these are true, it returns 1. If these are not all true, it returns 2.'''
    if len(password) >= 8 and len(password) <= 15 and any(char.isdigit() for char in password) and any(
            char.isupper() for char in password):
        return 1
    else:
        return 2


def ExistingPassword(password):
    '''This function checks if the password inputted to login matches the password at the same location in the password list as the location of the username inputted in the username list. If it matches the password associated with that username, then it returns 1. If it doesn't it returns 2.'''
    if password == passwords[usernames.index(username)]:
        return 1
    else:
        return 2


def Close():
    '''This function closes these 5 files when called upon.'''
    userfile.close()
    passfile.close()
    countryfile.close()
    firstnames.close()
    lastnames.close()


'''--------------Functions for Main Program--------------'''
def Winner():
    '''This defenition checks every possible winning combination for Tic Tac Toe. It returns True if someone has won, otherwise it doesn't return anything. If board[0][0],board[0][1], and board[0][2] all == 'X', then it would return True.'''
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        return True
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        return True
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        return True
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        return True
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        return True
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        return True
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        return True
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        return True
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        return True
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        return True
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        return True
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        return True
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return True
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return True
    elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
        return True
    elif board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
        return True


def ScoreOption(addscore, winner):
    '''If the user inputs "yes" when asked if they want to add their score, then it checks if winner == 1 or 2 to see which player won, and depending on this it will set playerturn to the amount of turns it took them to win. It then calls upon the function AddScore(playerturn) to add their score to the highscores file. If the user says "no", then their score is not added. If they iput "yes" or "no, it returns True. If they don't input "yes" or "no", it returns False.'''
    if addscore.lower() == "yes":
        if winner == 1:
            playerturn = p1turn
        else:
            playerturn = p2turn
        AddScore(playerturn)
    elif addscore.lower() == "no":
        print
        "Ok. Your score was not added to the high scores list."
    else:
        return False


def AddScore(playerturn):
    '''This function adds the player's name and the number of turns it took them to win tic tac toe to the high scores list.'''
    highscores.write("\n" + playername + " " + str(playerturn) + " turns")


def ViewScores():
    '''This function asks the user if they want to view high scores. If they input "yes", it will display the high scores list. If they say "no", it will not display it. If they do not input "yes" or "no", then this is the only case where it does not stop the while loop. It does not stop the while loop until they input a correct answer.'''
    view = 1
    while view == 1:
        viewscores = input("Would you like to view the high scores?(type yes or no) ")
        if viewscores.lower() == "yes":
            print("Here are the highscores:", scorelist)
            view = 2
        elif viewscores.lower() == "no":
            print("Ok.")
            view = 2
        else:
            print("Please input yes or no.")


'''-------------Importing Toolkits-------------'''
import time
import math

fullprogram = 1
print("Welcome to Hunter's Awesome Program!")

while fullprogram == 1:
    '''--------------Opening All Files Used in My Program--------------'''
    with open('countries.txt') as countries:
        countrylist = countries.read().splitlines()
    with open('usernames.txt') as names:
        usernames = names.read().splitlines()
    with open('passwords.txt') as passes:
        passwords = passes.read().splitlines()
    with open('firstnames.txt') as names1:
        f_names = names1.read().splitlines()
    with open('lastnames.txt') as names2:
        l_names = names2.read().splitlines()
    passfile = open('passwords.txt', 'a')
    userfile = open('usernames.txt', 'a')
    countryfile = open('userscountries.txt', 'a')
    firstnames = open('firstnames.txt', 'a')
    lastnames = open('lastnames.txt', 'a')
    '''--------------Login Program--------------'''
    '''The login program is responsible for either helping a user login to their account or create a new account. To login, user must input their username and password. The program checks if the username is in the list of existing usernames, and if the password at the same location as that in the list of passwords matches the password they inputted. If the user needs to create an account, they must give a firstname and lastname that is alphabetical and does not already exist in the database. They must input their country of residence, which is checked if it is correct in a list of all countries. They must then create a username between 6-12 characters who's length is checked by a function. They must pick a password between 8-15 characters, with at least one capital, and at least one number. All of these specifications are checked by a function.'''
    countrypick = 1
    usernamepick = 1
    passwordpick = 1
    namespick = 1
    accountpick = 1
    while accountpick == 1:
        account = input("Please input 1 if you are an existing user and 2 if you would like to create a new account. ")
        if account == "1":  # This if statement is the login option
            accountpick = 2
            while usernamepick == 1:
                username = input("Please enter your username. ")
                if User(
                        username) == 3:  # Runs and checks function User(username) to check if that is a username that exists
                    usernamepick = 2
                else:
                    print
                    "That username does not exist in our database."
            while passwordpick == 1:
                password = input("Please enter your password. ")
                if ExistingPassword(
                        password) == 1:  # Runs and checks the function ExistingPassword(password) to see if the password at the same location in the list as the username matches
                    passwordpick = 2
                else:
                    print
                    "Password incorrect."
        elif account == "2":  # This if statement is the create a new account option
            accountpick = 2
            print
            "Ok. Let's create an account."
            while namespick == 1:
                firstname = input("What is your first name? ")
                lastname = input("What is your last name? ")
                if Names(firstname,
                         lastname) == 1:  # Runs and checks this function to check that the firstname and lastname are alphabetical and do not both already exist
                    firstnames.write("\n" + firstname.title())
                    lastnames.write("\n" + lastname.title())
                    namespick = 2
                elif Names(firstname, lastname) == 2:  # If the function returns 2, this means the name already exists
                    print
                    "There is already an account under that name in our database. Please enter a different one"
                else:
                    print
                    "Names should only contain letters."
            while countrypick == 1:
                usercountry = input("What is your country of residence? ")
                if Country(
                        usercountry) == 1:  # Runs this function to check if the country they inputted in title() format exists in the list of countries
                    print
                    usercountry.title(), "is a valid country choice."
                    countryfile.write("\n" + usercountry.title())  # Adds their country to the file of user countries
                    countrypick = 2
                else:
                    print
                    "Please input a valid country. Do not use an abreviation."
            while usernamepick == 1:
                username = input("Usernames should be between 6-12 characters. Please pick a username. ")
                if User(
                        username) == 1:  # Runs this function to check that the username is between 6-12 characters and does not already exist
                    userfile.write("\n" + username)  # Adds username to file of usernames
                    print
                    "Great. Your username is:", username
                    usernamepick = 2
                else:
                    print
                    "That username may already exist or does not meet the specifications. Please pick another one."
            while passwordpick == 1:
                password = input(
                    "Passwords must be between 8-15 characters in lenght, have at least one number,\n and have at least one capital letter. ")
                if NewPassword(
                        password) == 1:  # Runs this function to check if the password meets all of the given specifications
                    passfile.write("\n" + password)  # If it meets them, it will be added to the passwords file
                    print("Ok. Your password has been set and your account has been created.")
                    passwordpick = 2
                else:
                    print("Please pick a password that fits the specifications.")
        else:
            print
            "Please input a correct number."
    Close()  # Calls upon the close function to close all files that have been opened so that next time they are opened you can see the new information that was added
    '''------------------Main Program--------------------'''
    '''This main program has 4 options. The first is for a calculator. In the calculator, the user has the option to use the pythagorean theorum to find c if they input sides a and b. They also have the option to find the area of a tringle if they give the base and the height. They also have the option to do a temperature conversion, either from celcius to ferenheight, or the opposite. The second option is to logout, which will bring the user back to the start of the login process. The third option is to play 2-player Tic Tact Toe. Once the game is over, the winning player has the choice to add the number of turns they won in to the high scores file. After this, the user has the option to view the highscores list. The last option is to quit the program, which makes all while loops end and finishes the program.'''
    mainprogram = 1  # Each of these 7 variables are responsible for running while loops in the main program
    mathpick = 1
    math1 = 1
    math2 = 1
    math3 = 1
    math4 = 1
    math5 = 1
    print
    "Welcome! You have succesfully been logged in."
    while mainprogram == 1:
        mathpick = 1
        option = input(
            "Press 1 to play blackjack, 2 to logout of your account,\n3 to play Tic Tac Toe, and 4 to quit the program. ")
        if option == "1":
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

                player = sum(player_hand)  # Figure out what each players score is
                player2 = sum(player_hand2)  # Keep track of player 2 for aces

                dealer = sum(dealer_hand)
                dealer2 = sum(dealer_hand2)

                print("\nThe dealer is showing %d" % dealer_hand[
                    0])  # Only show the first card, if it is a 1 then the user should assume it is an Ace
                print("\nYou are showing %d and %d" % (player_hand[0], player_hand[1]))  # Show your 2 cards
                hit = input("\nWould you like to hit(Y/N): ").title()  # Use .title to protect against lowercase input

                while (
                        player <= 21 or player2 <= 21) and hit == "Y":  # Run the loop while the player hasn't busted and they want to hit
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
                    print("\nThe dealer's hand is %d" % max(dealer,
                                                            dealer2))  # Since the dealer has to stop on 17 we show the max score they have
                    if player > 21:  # Figure out which is the highest non bust score the player has with these if statements
                        player_score = player2

                    elif player2 > 21:
                        player_score = player

                    else:
                        player_score = max(player, player2)

                    while max(dealer, dealer2) < 17:  # The loop should run until the dealer has a hand above 16
                        time.sleep(
                            2)  # Put this here to have the cards be dealt more slowly to better simulate a real casino, Marinah's brother taught me this
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

                    if (dealer > 21) and (
                            dealer2 > 21):  # Check if the dealer busted, if they did then add the bet to chips
                        print("\nDealer busted, you win the hand!")
                        chips = chips + bet

                    else:
                        if (dealer > 21) and (dealer2 <= 21):  # Same logic as player_score
                            dealer_score = dealer2

                        elif (dealer <= 21) and (dealer2 > 21):
                            dealer_score = dealer

                        else:
                            dealer_score = max(dealer, dealer2)

                        if dealer_score > player_score:  # Figure out who won the hand and assign chips
                            print("\nThe dealer has a better hand (%d) and has won the round!" % dealer_score)
                            chips = chips - bet

                        elif dealer_score < player_score:
                            print(
                                "\nYou have a better hand (%d) than the dealer and have won the round!" % player_score)

                        else:
                            print(
                                "\nYou and the dealer have the same hand (%d) and have tied the round!" % player_score)

                if chips > 0:  # If the player still has chips let them play another hand if they wish
                    play = input("\nWould you like to play another hand (Y/N): ").title()

            if chips <= 0:
                print("\nYou ran out of chips!")

            print("\nThanks for playing!")
            # new line
        elif option == "2":
            print("You have been successfully logged out.")
            mainprogram = 2  # Stops the current while loops but not the full program while loop so the user is brought back to the login process
            accountpick = 1
        elif option == "3":
            loop = 1
            player = 1
            turn = 0
            p1turn = 0
            p2turn = 0
            playerturn = 0
            with open(
                    'usernames.txt') as names:  # creates a new list from these 3 files every time this option is picked in case new items were added
                usernames = names.read().splitlines()
            with open('firstnames.txt') as names1:
                f_names = names1.read().splitlines()
            with open('lastnames.txt') as names2:
                l_names = names2.read().splitlines()
            highscores = open('highscores.txt', 'a')  # Only opens this file once the option has been picked
            board = ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']
            print("Welcome to TicTacToe!\n", f_names[usernames.index(username)], l_names[usernames.index(
                username)], "you will be player 1.") # Picks the current user's name from the list based on the location of their username
            p2_name = input("Player 2, what is your name? ")
            print("Here are the numbers assigned to each position on the board.\n", board[0], "\n", board[1], "\n", board[2])
            while loop == 1:
                while player == 1:
                    location = input("It is player 1's turn (X's).\nWhat spot do you want to take? ")
                    if location.isdigit() and location <= '9' and location >= '1':  # If the user input a digit from 1-9, this if statement runs
                        location = int(location)
                        turn = turn + 1
                        p1turn = p1turn + 1
                        if location == 1 and board[0][
                            0] == '1':  # Runs the correct if statement for whichever number location is set to. If the corresponding position on the board is still set to it's number (hasn't been changed to an X or O), then sets player to 2 and replaces it with an X
                            board[0][0] = 'X'
                            player = 2
                        elif location == 2 and board[0][1] == '2':
                            board[0][1] = 'X'
                            player = 2
                        elif location == 3 and board[0][2] == '3':
                            board[0][2] = 'X'
                            player = 2
                        elif location == 4 and board[1][0] == '4':
                            board[1][0] = 'X'
                            player = 2
                        elif location == 5 and board[1][1] == '5':
                            board[1][1] = 'X'
                            player = 2
                        elif location == 6 and board[1][2] == '6':
                            board[1][2] = 'X'
                            player = 2
                        elif location == 7 and board[2][0] == '7':
                            board[2][0] = 'X'
                            player = 2
                        elif location == 8 and board[2][1] == '8':
                            board[2][1] = 'X'
                            player = 2
                        elif location == 9 and board[2][2] == '9':
                            board[2][2] = 'X'
                            player = 2
                        else:
                            print("That spot is already taken.")  # If none of these statements are applicable, that means that the user has chosen a spot that has already been changed
                            turn = turn - 1  # Subtracts 1 from both these variables because a real turn was not played (nothing new was placed on the board)
                            p1turn = p1turn - 1
                        print(board[0], "\n", board[1], "\n", board[2])
                        if Winner() == True:  # If the function returns True (someone has won), this statement runs and exits the program
                            print("Player 1 wins!")
                            loop = 0
                            player = 0
                            winner = 1
                            playername = f_names[usernames.index(username)] + " " + l_names[
                                usernames.index(username)]  # Sets playername to the user who logged in's name
                            adding = 1
                            while adding == 1:
                                addscore = input(
                                    "Would you like to add your score to the high scores list?(type yes or no) ")
                                if ScoreOption(addscore,
                                               winner) == False:  # Calls upon the score option function to run add or not add the highscore. Returns false if yes or no was not inputted
                                    print ("Please input yes or no.")
                                else:
                                    adding = 2
                        else:
                            if turn == 9:  # If no one has won, it checks if turn = 9 because this means that all spots on the board are taken
                                print("That's a tie!")
                                loop = 0
                                player = 0
                    else:
                        print("Input a correct number.")
                while player == 2:
                    location = input("It is player 2's turn (O's).\nWhat spot do you want to take? ")
                    if location.isdigit() and location <= '9' and location >= '1':  # If the user input a digit from 1-9, this if statement runs
                        location = int(location)
                        turn = turn + 1
                        p2turn = p2turn + 1
                        if location == 1 and board[0][0] == '1':  # Runs the correct if statement for whichever number location is set to. If the corresponding position on the board is still set to it's number (hasn't been changed to an X or O), then sets player to 2 and replaces that location with an O
                            board[0][0] = 'O'
                            player = 1
                        elif location == 2 and board[0][1] == '2':
                            board[0][1] = 'O'
                            player = 1
                        elif location == 3 and board[0][2] == '3':
                            board[0][2] = 'O'
                            player = 1
                        elif location == 4 and board[1][0] == '4':
                            board[1][0] = 'O'
                            player = 1
                        elif location == 5 and board[1][1] == '5':
                            board[1][1] = 'O'
                            player = 1
                        elif location == 6 and board[1][2] == '6':
                            board[1][2] = 'O'
                            player = 1
                        elif location == 7 and board[2][0] == '7':
                            board[2][0] = 'O'
                            player = 1
                        elif location == 8 and board[2][1] == '8':
                            board[2][1] = 'O'
                            player = 1
                        elif location == 9 and board[2][2] == '9':
                            board[2][2] = 'O'
                            player = 1
                        else:
                            print("That spot is already taken.")  # If none of these statements are applicable, that means that the user has chosen a spot that has already been changed
                            turn = turn - 1  # Subtracts 1 from both these variables because a real turn was not played (nothing new was placed on the board)
                            p2turn = p2turn - 1
                        print(board[0], "\n", board[1], "\n", board[2])
                        if Winner() == True:  # If this function returns True (someone has won), this statement runs and exits the program
                            print("Player 2 wins!")
                            loop = 0
                            player = 0
                            winner = 2
                            playername = p2_name
                            adding = 1
                            while adding == 1:
                                addscore = input(
                                    "Would you like to add your score to the high scores list?(type yes or no) ")
                                if ScoreOption(addscore,winner) == False:  # Calls upon the score option function to run add or not add the highscore. Returns false if yes or no was not inputted
                                    print("Please input yes or no.")
                                else:
                                    adding = 2
                        else:
                            if turn == 9:  # If no one has won, it checks if turn = 9 because this means that all spots on the board are taken
                                print( "That's a tie!")
                                loop = 0
                                player = 0
                    else:
                        print("Please input a correct number.")
            highscores.close()  # Has to close this file before making it into a list so that new scores are included in the list
            with open('highscores.txt') as scores:
                scorelist = scores.read().splitlines()
            ViewScores()  # Runs this function to give the user the option to view their score or not
        elif option == "4":
            print("Thanks for using Hunter's Awesome Program!")
            mainprogram = 2  # Stops all running while loops to quit the program
            fullprogram = 2
        else:
            print("Please input a correct number.")
Close()  # Closes all files that are still open
