import random

money = 100
#Write your game of chance functions here

#Coin Flip Game

def coin_flip(guess, bet):
    #Make sure your bet is above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0")
        print("------------------")
        return 0

    #Starts the game and flips a coin

    print("------------------")
    print("Let's flip a coin! You guessed " + guess)
    result = random.randint(1,2)

    #Prints the result of the coin flip. A 1 is heads, a 2 is tails.

    if result == 1:
        print("Heads!")
    elif result == 2:
        print("Tails!")

    # Determines if you won or lost and returns either bet or -bet

    if (guess == "Heads" and result == 1) or (guess == "Tails" and result == 2):
        print("You won " + str(bet) + " dollars!")
        return bet
    else:
        print("You lost" + str(bet) + " dollars!")
        return -bet

#Cho-Han Game

def cho_han(guess, bet):
    # Make sure your bet is above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0")
        print("------------------")
        return 0

    #Starts the game and rolls the dices
    print("------------------")
    print("Let's play Cho-Han! You guessed " + guess)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum_dices = dice1 + dice2

    # Prints the result of the Cho-Han

    if sum_dices % 2 == 0:
        print("Even!")
    else:
        print("Odd!")

    # Determines if you won or lost and returns either bet or -bet

    if (guess == "Even" and sum_dices % 2 == 0):
        print("You won " + str(bet) + " dollars!")
        return bet
    else:
        print("You lost" + str(bet) + " dollars!")
        return -bet


#Highest Card Game

def highest_card(bet):
    # Make sure your bet is above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0")
        print("------------------")
        return 0

    #Starts the game and rolls the dices
    print("------------------")
    print("Let's play a game of cards!")
    my_card = random.randint(1, 20)
    their_card = random.randint(1, 20)
    print("My card was {}".format(my_card))
    print("My card was {}".format(their_card))

    # Determines if you won or lost

    if my_card > their_card:
        print("You won " + str(bet) + " dollars!")
        return bet
    elif my_card < their_card:
        print("You lost " + str(bet) + " dollars!")
        return -bet
    else:
        print("It's a tie boys!")

#Roulette Game

def roulette(guess, bet):
    # Make sure your bet is above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0")
        print("------------------")
        return 0

    #Starts the game!
    print("------------------")
    print("Let's play roulette!")
    roulette_result = random.randint(1,37)
    if roulette_result == 37:
        print("The number is 00")
    else:
        print("The number is {}".format(roulette_result))

    # Determines if you won or lost

    if guess == "Odd" or guess == "Even":
        if roulette_result == 0 or roulette_result == 37:
            print("You lost " + str(bet) + " dollars!")
            return -bet
        else:
            if roulette_result % 2 == 0 and guess == "Even":
                print ("You win " + str(bet) + " dollars!")
                return bet
            if roulette_result % 2 != 0 and guess == "Odd":
                print("You win " + str(bet) + " dollars!")
                return bet
            else:
                print("You lost " + str(bet) + " dollars!")
                return -bet

    elif guess == roulette_result:
        result = bet * 35
        print("You win " + str(result) + " dollars!")
        return result
    elif guess != roulette_result:
        result = bet * 35
        print("You lost " + str(result) + " dollars!")
        return -result

#Call your game of chance functions here

money += coin_flip("Heads", 1)
money += cho_han("Even", 20)
money += highest_card(20)
money += roulette("20", 1)
print("")
print("------------------")
print("Your outstanding amount of money in your account is {} dollars".format(money))