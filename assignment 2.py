wins = 0

for i in range(6):
    result = input("Did the player win or lose game %d: " % (i+1))
    if result.capitalize() == "W": #capitalizes input to account for both lowercases and uppercases
        wins += 1

if wins > 4:
    print("The player won %d games and will be put into Group 1!" % wins)

elif (wins > 2) and (wins < 5):
    print("The player won %d games and will be put into Group 2!" % wins)

elif (wins > 0) and (wins <3):
    print("The player won %d games and will be put into Group 3!" % wins)

else:
    print("The player had a rough showing winning no games, they are eliminated!") #this code checks the number of wins the player recieved adn then prints out what group they will be entering