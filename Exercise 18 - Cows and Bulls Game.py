# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess the 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout the game and tell the user at the end.


import random


def cows_and_bulls():

    game_number_list = random.sample(range(0, 10), 4)

    print("\n\nWelcome to the Cows and Bulls Game. \nGuess the 4-digit number in 8 tries.")
    guess_count = 0

    while guess_count < 8:
        cow_count = 0
        bull_count = 0
        guess_list = list(input("Guess a 4-digit number: "))
        guess_count += 1

        for i in range(4):
            if game_number_list[i] == int(guess_list[i]):
                cow_count += 1

        if cow_count == 4:
            print("That's correct. Well Done! You have won the game.")
            replay1 = input("Do you want to play again? y/n: ")
            if replay1 == "y":
                cows_and_bulls()
            else:
                print("You have quit the game. Come again sometime.")
                quit()

        for x in range(4):
            if str(game_number_list[x]) in guess_list and str(game_number_list[x]) != guess_list[x]:
                bull_count += 1

        if cow_count == 1:
            cow_name = "cow"
        else:
            cow_name = "cows"

        if bull_count == 1:
            bull_name = "bull"
        else:
            bull_name = "bulls"

        print(f'You have {cow_count} {cow_name} and {bull_count} {bull_name}')

    print("You have exceeded your guessing limit. You lose!")
    print(f"The answer was {game_number_list}")
    replay2 = input("Do you want to play again? y/n: ")
    if replay2 == "y":
        cows_and_bulls()
    else:
        print("You have quit the game. Come again sometime.")
        quit()


try:
    cows_and_bulls()
except IndexError:
    print("\nPlease enter a 4-digit number.")
except ValueError:
    print("\nPlease enter a 4-digit number.")

cows_and_bulls()
