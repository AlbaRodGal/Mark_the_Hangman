"Second attempt of building a word guessing game."

import random
from colorama import init
from termcolor import colored
import sys

# Welcome and instructions:

def print_instructions(welcome, instructions):
    print(welcome.center(150))
    print(instructions.center(150))
    print(lives_color)
    return None

def print_hint(word):
    print(f'{len(word)} letters')

# Choose random word of list_of_words

def generate_random_word(list_of_words):
    word = random.choice(list_of_words)
    word = word.rstrip("\n")
    return word

# Function to hide random_word

def print_underscores(word):
    hidden_word = ["_"] * len(word)
    print(" ".join(hidden_word))
    return hidden_word
    
# Function for user to input a letter

def user_input():
    input_letter = input("Please type a letter or a word: ")
    return input_letter

# Function to check whether the input_letter is a letter

def validate_input_letter(input_letter):
    if input_letter.isalpha():
        return True
    else:
        print("Sorry, that's not a letter. Please try again.")
        return False

# Function to check whether or not input_letter in in word

def check_and_print_letter(word):
    for index, letter in enumerate(word):
        if letter is input_letter:
            hidden_word[index] = input_letter
    new_word = current_word_to_guess(hidden_word)


# Funtion to print an updated version of hidden_word
def current_word_to_guess(hidden_word):
    current_word_to_guess = colored(" ".join([letter for letter in hidden_word]), "yellow", attrs=['bold'])
    print(current_word_to_guess)

def check_word(word, hidden_word):
    for index, letter in enumerate(word):
        if hidden_word is word:
            return True

# Import file

with open("/Users/albarodriguez/Projects/Mark_the_Hangman/ListOfWords.txt") as f:
    list_of_words = f.readlines()

welcome = "Hello from the other side!"
instructions = """Can you guess the word?"""
LIVES = 5
lives_color = colored(f'{LIVES} lives', "magenta", attrs=["bold"])

print_instructions(welcome, instructions)
word = generate_random_word(list_of_words)
print_hint(word)
hidden_word = print_underscores(word)

while hidden_word != list(word):
    input_letter = user_input()
    validation = validate_input_letter(input_letter)
    if validation is True:
        new_word = check_and_print_letter(word)
    else: 
        input_letter = user_input()

    if input_letter in word:
       right_answer = colored(f'Well Done! {input_letter.upper()} is correct!', 'green', attrs=['bold'])
       print(right_answer)
    else:
        wrong_answer = colored(f'Sorry, {input_letter.upper()} is not in the word', 'red', attrs=['bold'])
        print(wrong_answer)
        LIVES -= 1
        print(f'{LIVES} lives')
        if LIVES <1:
            game_over = colored("Game Over", 'red', attrs=['bold'])
            print(game_over)
            answer = colored(f'The correct word is {word.upper()}', 'magenta', attrs=['bold'])
            print(answer)
            sys.exit()    
else: 
    congrats = colored(f'Congrats! {word.upper()} is the word', 'magenta', attrs=['bold'])
    print(congrats)
    sys.exit()