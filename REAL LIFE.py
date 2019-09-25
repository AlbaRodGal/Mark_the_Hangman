"Second attempt of building a word guessing game."

import random

# Welcome and instructions:

def print_instructions(welcome, instructions):
    print(welcome.center(150))
    print(instructions.center(150))
    print()
    
# Choose random word of list_of_words

def generate_random_word(list_of_words):
    random_word = random.choice(list_of_words)
    selected_word = list(random_word.rstrip("\n"))
    return selected_word

# Function to hide selected_word

def hide_word(selected_word):
    number_of_letters = len(selected_word)
    hidden_word = ["_"] * len(selected_word)
    return hidden_word

# Funtion to print an updated version hidden_word
def print_hidden_word():
    print(" ".join([letter for letter in hidden_word]))

#################### --- LIVES --- to be reviewed --- #########################

print(f"Hint: {number_of_letters} letters")
lives = 5
print(f"Lives: {lives}")
print()

# Function to look for user's input in selected word
def input():
    for index in range(0,10):
        print_hidden_word()
        input_letter = input("Please type a letter or word:  ")

# Function to validate and check user's input
def check_input():    
    if input_letter.isalpha():
        print()
    else:
        print("Sorry, I didn't understand that")
    if input_letter in selected_word:
        print("Well Done!")
        for index, letter in enumerate(selected_word):
            if letter is input_letter:
                hidden_word[index] = input_letter
            
    else:
        print("No, sorry")
        lives -= 1
        print(f"Lives: {lives}")
    if lives == 0:
        print()
        print("GAME OVER")
        break


# Function for user to attempt to guess the word
def input_word():
    answer = input("Can you guess the word? (yes/no): ")
    if answer is yes:
        attempt = input("Type the word: ")
    else:
        input()





# Function to check whether the user's guessed the word
def check_user_attempt():
    for index, letters in enumerate(attempt):
        if user_attempt is selected_word:
            user_attempt[index] == selected_word[index]


########################## M a i n ##################################

# Import file

with open("/Users/albarodriguez/Projects/Mark_the_Hangman/ListOfWords.txt") as f:
    list_of_words = f.readlines()

#### Definition of variables ####

welcome = "Hello from the other side!"
instructions = """Can you guess the word?"""
random_word = random.choice(list_of_words)
selected_word = list(random_word.rstrip("\n"))
hidden_word = ["_"] * len(selected_word)


#### Working Programme ####

print_instructions(welcome,instructions)
generate_random_word(list_of_words)
hide_word(selected_word)
print_hidden_word():
