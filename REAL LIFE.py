"Second attempt of builing a word guessing game."

import random

# Welcome and instructions:

welcome = "Hello from the other side!"
instructions = """Can you guess the word?"""

print(welcome.center(150))
print(instructions.center(150))
print()

# Import file

with open("C:/Users/Alba/PycharmProjects/MarkTheHangman/ListOfWords.txt") as f:
    list_of_words = f.readlines()

# Choose random word of list_of_words

random_word = random.choice(list_of_words)
selected_word = list(random_word.rstrip("\n"))
print(selected_word)

# print(selected_word)

# Hide random_word

number_of_letters = len(selected_word)
print(f"Hint: {number_of_letters} letters")

lives = 5

print(f"Lives: {lives}")

print()

hidden_word = ["_"] * len(selected_word)
# print(number_of_letters * "_ ")
# print()

# User to type letter or word

# input_letter = input("Please type a letter or word:  ")

# if input_letter.isalpha():
   # print("True")
# else:
    #print("Sorry, I didn't understand that")

# Funtion to print an updated version hidden_word
def print_hidden_word():
    print(" ".join([letter for letter in hidden_word])) # .join converts hidden_word in string

# Look for user's input in selected word

for index in range(0,10):
    print_hidden_word()
    input_letter = input("Please type a letter or word:  ")
    # Validation of user's input
    if input_letter.isalpha():
        print()
    else:
        print("Sorry, I didn't understand that")

    if input_letter in selected_word:
        print("Well Done!")
        for index, letter in enumerate(selected_word):
            if letter is input_letter:
                hidden_word[index] = input_letter
                input_word = input("Can you guess the word?(Yes/No): ")
                if input_word == "yes":
                    attempt = input("Type the word: ")
                else:
                    print()
    else:
        print("No, sorry")
        lives -= 1
        print(f"Lives: {lives}")
        if lives == 0:
            print()
            print("GAME OVER")
            break

