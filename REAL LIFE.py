"Second attempt of building a word guessing game."

import random

# Welcome and instructions:

def print_instructions(welcome, instructions):
    print(welcome.center(150))
    print(instructions.center(150))
    print()
    
# Choose random word of list_of_words

def generate_random_word(list_of_words):
    word = random.choice(list_of_words)
    random_word = list(word.rstrip("\n"))
    return random_word

# Function to hide random_word

def hide_word(random_word):
    hidden_word = ["_"] * len(random_word)
    return hidden_word

# Funtion to print an updated version hidden_word
def print_hidden_word():
    print(" ".join([letter for letter in hidden_word]))
    return None

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

# Function to check whether the input_letter is a letter

def validate_input_letter(input_letter):
    if input_letter.isalpha():
        a = check_answer(word, input_letter)
    else:
        print("Sorry, that's not a letter. Please try again.")
        

# Function to check whether or not input_letter in in word

def check_answer(word, input_letter):
    for index, letter in enumerate(word):
        if letter is input_letter:
            hidden_word[index] = input_letter
        # else:
        #     wrong = wrong_answer(word, input_letter) 

    print_new_word(hidden_word)

   # print(f'{input_letter} is right. Well done!')
    print_new_word(hidden_word)
    


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

welcome = "Hello from the other side!"
instructions = """Can you guess the word?"""

print_instructions(welcome, instructions)
random_word = generate_random_word(list_of_words)

hidden_word = hide_word(random_word)
print_hidden_word(hidden_word)
validation = validate_input_letter(input_letter)

