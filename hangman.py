import random, sys
from collections import Counter


class User:
    
    def __init__(self):
        self.name = ""  
        self.mistakes = 0
        self.used_letters = []
        self.letter_guessed = []
        self.turns = 0
        self.wrong_answer = 0
    
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
            self.used_letters.append(self.letter)

    def turn(self):
        if(self.letter):
            self.turns +=1
            #print("You moved",self.turns) 

class Game:
    
    def __init__(self, user1):
        self.user1 = user1
    
    def random_word(self):
        list_of_words = ["KOSIA", "KINKA", "KMACIEG", "KSIEMEG"]
        self.string = random.choice(list_of_words)
        for word in range(1):
            self.guess_word = list(self.string.lower())

        self.print_underscore()
        print("Guess letter", self.guess_word)

    def print_underscore(self):
        print(len(self.guess_word)* " _")
        
            

    def end_program(self):
        print("That's end!")
        sys.exit()

    def check_letter(self):
        for char in range(len(self.guess_word)):
            if self.user1.letter == self.guess_word[char]:
                self.user1.letter_guessed.append(self.user1.letter)
                self.show_letter()
            else:
                print(" _")

    def show_letter(self):
        for char in self.user1.letter_guessed:
            print(char)
            
    def play_game(self):            
        print("Guess word:", self.guess_word)
       # self.print_underscore()
        if self.user1.letter in self.guess_word:
            print("YES")
            self.user1.attempt()
            self.check_letter()
            #print("Used letters:", self.user1.used_letters)
            #print("Mistakes:", self.user1.mistakes)
            #self.show_letter()
            self.user1.turn()
        else:
            print("NO")
            self.user1.add_mistake()
            self.user1.attempt()
            self.check_letter()
            #print("Used letters:", self.user1.used_letters)
            #print("Mistakes:", self.user1.mistakes)
            self.user1.turn()
