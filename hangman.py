import random, sys
from collections import Counter


class User:
    
    def __init__(self):
        self.name = ""  
        self.mistakes = 0
        self.used_letters = set()
        self.letter_guessed = set()
        self.turns = 0
        #self.wrong_answer = 0
    
    def introduce(self):
        self.name = input("Enter name:\n")

    def add_mistake(self):
        self.mistakes += 1

    def choose_letter(self):
        print(self.name, "enter letter:")
        self.letter = input()
        #self.attempt()

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
        list_of_words = ["apple", "banana", "raspberry", "coconut"]
        self.string = random.choice(list_of_words)
        for word in range(1):
            self.guess_word = list(self.string.lower())

        self.print_underscore()
        print("Guess letter", self.guess_word)

    def print_underscore(self):
        print(len(self.guess_word)* " _")

    def check_letter(self):
        if (self.user1.letter not in self.user1.letter_guessed) and (self.user1.letter in self.guess_word):
            self.user1.letter_guessed.add(self.user1.letter)

    def show_letters(self):
        for char in self.guess_word:
            if char in self.user1.letter_guessed:
                print(char)
            else:
                print(' _')

    def print_hangman(self):
        if self.user1.mistakes == 1:
            print("_____")

        elif self.user1.mistakes == 2:
            print("  |  ")
            print("  |  ")
            print("_____")

        elif self.user1.mistakes == 3:
            print("  |  ")
            print("  |  ")
            print("  |  ")
            print("  |  ")
            print("_____")

        elif self.user1.mistakes == 4:
            print("   _____")
            print("  |    |")
            print("  |  ")
            print("  |  ")
            print("  |  ")
            print("_____")  

        elif self.user1.mistakes == 5:
            print("   _____")
            print("  |    |")
            print("  |    O")
            print("  |  ")
            print("  |  ")
            print("_____") 

        elif self.user1.mistakes == 6:
            print("   _____")
            print("  |    |")
            print("  |    O")
            print("  |    |")
            print("  |  ")
            print("_____")

        elif self.user1.mistakes == 7:
            print("   _____")
            print("  |    |")
            print("  |    O")
            print("  |   /|")
            print("  |  ")
            print("_____")

        elif self.user1.mistakes == 8:
            print("   _____ ")
            print("  |    | ")
            print("  |    O ")
            print("  |   /|\ ")
            print("  |  ")
            print("_____")

        elif self.user1.mistakes == 9:
            print("   _____")
            print("  |    | ")
            print("  |    O ")
            print("  |   /|\ ")
            print("  |   /  ")
            print("_____")

        elif self.user1.mistakes == 10:
            print("   _____")
            print("  |    | ")
            print("  |    O ")
            print("  |   /|\ ")
            print("  |   / \ ")
            print("_____")

    def loose(self):
        if self.user1.mistakes == 10:
            print("That's end. You loose :(")
            print("See you next time!")
            quit()

    def play_game(self):            
        if self.user1.letter in self.guess_word:
            print("YES")
            self.user1.attempt()
            self.check_letter()
            self.show_letters()
            self.user1.turn()
        else:
            print("NO")
            self.user1.add_mistake()
            self.user1.attempt()
            self.check_letter()
            self.show_letters()
            self.print_hangman()
            print("Mistakes:", self.user1.mistakes)
            self.user1.turn()
            self.loose()
