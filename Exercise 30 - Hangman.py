# The task is to write a function that picks a random word from a list of words from the WordList text file.

import random

with open("wordlist.txt", "r") as words:
    word_list = words.readlines()

random_word = random.choice(word_list)
print(random_word)
lines = "_" * (len(random_word)-1)


def hangman():

    print("\nWelcome to Hangman! You have 6 tries to guess the word.")
    print(f"\nThe word is: {lines}")

    word_listed1 = list(random_word)
    word_listed1.pop()

    guessed_word_list = list(lines)
    count = 1

    while count < 7:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_word_list:
            print("You have already guessed that letter. Guess again. Your guess count won't be penalized.")
            count -= 1
 
        if guess not in word_listed1:
            print("Not in word. Try Again.")

        for i in range(0, len(word_listed1)):
            if guess == word_listed1[i]:
                guessed_word_list[i] = guess

        print("".join(guessed_word_list))

        if '_' not in guessed_word_list:
            print("Congratulations. You've won!")
            replay1 = input("Do you want to play again? y/n: ").lower()
            if replay1 == 'y':
                hangman()
            else:
                print("You have quit the game.")
        count += 1

    print("You are out of tries. You lose!")
    word_listed1 = "".join(word_listed1)
    print(f"The word was: {word_listed1}")
    replay2 = input("Do you want to play again? y/n: ").lower()
    if replay2 == 'y':
        hangman()
    elif replay2 == 'n':
        print("You have quit the game.")


hangman()
