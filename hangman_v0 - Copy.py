import random
import string

def show_start_screen():
    print("Let's play Hangman!")


def show_credits():
    print('by Ian Thompson')

def get_puzzle():
    words = ["lion", "tiger", "bear", "baked ziti", "america", "donald"]
    return random.choice(words)

def check(word, solved, guesses):
    for i in range(len(word)):
     if word[i] in guesses or not word[i].isalpha():
        solved = solved[:i] + word[i] + solved[i+1:]
    return solved

def get_guess():
    while True:
        guess = input('Guess a letter ')

        if len(guess) == 1:
            return guess
        else:
            print("please enter one character")
    
    return guess

def confirm():
    pass

def display_board(solved, guesses, strikes):

    if strikes == 1:
       print("""
             ___________
            |         |
            |         0
            |        /|\
            |        / \
            |
            |
        ------------------- """)
    
    print(solved + "[" + guesses + "]")

def play_again():

    question = input("Do you want to play again? (y/n) ")

    if question == "y":
        return True
    elif question == "n":
        return False

def play():

    word = get_puzzle()
    solved = "-" * len(word)
    guesses = "" 
    solved = check(word, solved, guesses)
    strikes = 0
    limit = 6

    display_board(solved, guesses, strikes)

    while word != solved and strikes < limit:

        letter = get_guess()

        if letter not in word:
            strikes += 1

        guesses += letter

        solved = check(word, solved, guesses)
        display_board(solved, guesses, strikes)


    print("You win!")


def main():
    play()
    show_start_screen()

    playing = True

    while playing:
        play()
        playing = play_again()
    

# code execution begins here
if __name__ == "__main__":
    main()
    
