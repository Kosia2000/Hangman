import random, sys
from os import system
import curses

class User:
    
    def __init__(self):
        self.name = ""  
        self.mistakes = 0
        self.used_letters = set()
        self.letter_guessed = set()
        self.turns = 0
    
    def introduce(self):
        self.name = input("Enter name:\n")

    def add_mistake(self):
        self.mistakes += 1

    def choose_letter(self):
        print(self.name, "enter letter:")
        self.letter = input()

    def attempt(self):
        if not self.letter.isalpha():
            print("Enter ONLY a letter!")
        elif len(self.letter) > 1:
            print("Only ONE letter!")
        elif self.letter in self.used_letters:
            print("You have already used this letter!")
        else:
            self.used_letters.add(self.letter)

    def turn(self):
        if(self.letter):
            self.turns +=1

class Game:

    def __init__(self, user1):
        self.user1 = user1
    
    def random_word(self):
        list_of_words = ["apple", "banana", "raspberry", "strawberry", "cherry", 
                         "lemon", "currant", "gooseberry", "papaya", "grapes"]
        self.string = random.choice(list_of_words)
        word = 1
        while(word):
            self.guess_word = list(self.string.lower())
            word = 0
        self.print_underscore()

    def print_underscore(self):
        print(len(self.guess_word)* " _")

    def check_letter(self):
        if (self.user1.letter not in self.user1.letter_guessed) and (self.user1.letter in self.guess_word):
            self.user1.letter_guessed.add(self.user1.letter)

    def show_letters(self):
        for char in self.guess_word:
            if char in self.user1.letter_guessed:
                print(char, end='')
            else:
                print(' _',end='')

    def lose(self):
        if self.user1.mistakes == 10:
            print("That's end. You loose :(")
            print("See you next time!")
            quit()

    def win(self):
        sum = 0
        for char in self.guess_word:
            if char in self.user1.letter_guessed:
                sum += 1
            else:
                sum += 0
        if sum == len(self.guess_word):
            print("You won!\nCongratulations!")
            quit()

    def print_hangman(self):
        if self.user1.mistakes == 1:
            print("\n")
            print('_____')

        elif self.user1.mistakes == 2:
            print("\n")
            print("  |  ")
            print("  |  ")
            print("_____")

        elif self.user1.mistakes == 3:
            print("\n")
            print("  |  ")
            print("  |  ")
            print("  |  ")
            print("  |  ")
            print("_____")

        elif self.user1.mistakes == 4:
            print("\n")
            print("   _____")
            print("  |    |")
            print("  |  ")
            print("  |  ")
            print("  |  ")
            print("_____")  

        elif self.user1.mistakes == 5:
            print("\n")
            print("   _____")
            print("  |    |")
            print("  |    O")
            print("  |  ")
            print("  |  ")
            print("_____") 

        elif self.user1.mistakes == 6:
            print("\n")
            print("   _____")
            print("  |    |")
            print("  |    O")
            print("  |    |")
            print("  |  ")
            print("_____")

        elif self.user1.mistakes == 7:
            print("\n")
            print("   _____")
            print("  |    |")
            print("  |    O")
            print("  |   /|")
            print("  |  ")
            print("_____")

        elif self.user1.mistakes == 8:
            print("\n")
            print("   _____ ")
            print("  |    | ")
            print("  |    O ")
            print("  |   /|\\ ")
            print("  |  ")
            print("_____")

        elif self.user1.mistakes == 9:
            print("\n")
            print("   _____")
            print("  |    | ")
            print("  |    O ")
            print("  |   /|\\ ")
            print("  |   /  ")
            print("_____")

        elif self.user1.mistakes == 10:
            print("\n")
            print("   _____")
            print("  |    | ")
            print("  |    O ")
            print("  |   /|\\ ")
            print("  |   / \\ ")
            print("_____")

    def play_game(self):            
        if self.user1.letter in self.guess_word:
            print("Yes!")
            self.check_letter()
            self.show_letters()
            self.user1.turn()
            self.user1.attempt()
            self.print_hangman()
            print("\nUsed letters:",self.user1.used_letters)
            self.win()
        else:
            print("No")
            self.user1.add_mistake()
            self.check_letter()
            self.show_letters()
            self.user1.turn()
            self.print_hangman()
            self.user1.attempt()
            print("\nUsed letters:",self.user1.used_letters)
            print("Mistakes:", self.user1.mistakes)
            self.lose()
