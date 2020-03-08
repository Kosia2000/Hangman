import random, sys
from PIL import Image

class User:
    
    def __init__(self):
        self.name = ""  
        self.mistakes = 0;
        self.used_letters = []
    
    def introduce(self):
        self.name = input("Enter name:\n")

    def add_mistake(self):
        self.mistakes += 1
        
    def not_in_word(self):
        self.used_letters.append(self.letter)
        
        
    def choose_letter(self):
        print(self.name, "enter letter:")
        self.letter = input()
        
class Game:
    
    def __init__(self, user1):
        self.user1 = user1
    
    def random_word(self):
        #choose random word from list, cut it on letters
        list_of_words = ["Kosia", "KInka", "KMacieg", "KSiemeg"]
        self.string = random.choice(list_of_words)
        
    def print_underscore(self):
        for word in range(1):
            self.guess_word = list(self.string)
            print(len(self.guess_word)* " _")
    
    def check_letters(self):
        for word in range(1):
            print("String:", self.guess_word)
            if self.user1.choose_letter in self.guess_word:
                print("YES")
                print("Mistakes:", self.user1.mistakes)
                
            else:
                print("NO")
                self.user1.add_mistake()
                self.user1.not_in_word()
                print("Used letters:", self.user1.used_letters)
                print("Mistakes:", self.user1.mistakes)
        
    


user1 = User()
game = Game(user1)
user1.introduce()
game.random_word()
game.print_underscore()

user1.choose_letter()
game.check_letters()

