"Second attempt of building a word guessing game."

import random
import sys

# Welcome and instructions:

def print_instructions(welcome, instructions):
    print(welcome.center(150))
    print(instructions.center(150))
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
    input_letter = input("Please type a letter or a word:  ")
    print(input_letter)
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
    print(" ".join([letter for letter in hidden_word]))

def check_word(word, hidden_word):
    for index, letter in enumerate(word):
        if hidden_word is word:
            return True

# Import file

with open("/Users/albarodriguez/Projects/Mark_the_Hangman/ListOfWords.txt") as f:
    list_of_words = f.readlines()

welcome = "Hello from the other side!"
instructions = """Can you guess the word?"""

print_instructions(welcome, instructions)
word = generate_random_word(list_of_words)
print(word)
print_hint(word)
lives = 5
hidden_word = print_underscores(word)

while hidden_word != word:
    input_letter = user_input()
    validation = validate_input_letter(input_letter)
    if validation is True:
        new_word = check_and_print_letter(word)
    if input_letter in word:
        print(f'Well Done! {input_letter} is correct!')
    else:
        print(f'Sorry, {input_letter} is not in the word')
        lives -= 1
        print(f'{lives} lives')
        if lives <1:
            print("Game Over")
            sys.exit()