import random, sys

class User:
    
    def __init__(self):
        self.name = ""  
        self.mistakes = 0
        self.used_letters = []
    
    def introduce(self):
        self.name = input("Enter name:\n")

    def add_mistake(self):
        self.mistakes += 1

    def choose_letter(self):
        print(self.name, "enter letter:")
        self.letter = input()

    def attempt(self):
        if self.letter in self.used_letters:
            print("You have already used this letter!")
        else:
            self.used_letters.append(self.letter)


class Game:
    
    def __init__(self, user1):
        self.user1 = user1
    
    def random_word(self):
        #choose random word from list, cut it on letters
        self.array_with_letters = []
        list_of_words = ["Kosia", "KInka", "KMacieg", "KSiemeg"]
        self.string = random.choice(list_of_words)
        #print("String = ", self.string)
        for word in range(1):
            self.guess_word = list(self.string)
            self.array_with_letters.append(self.guess_word)
        print("Array_with_letters",self.array_with_letters)
        self.print_underscore()

        
    def print_underscore(self):
        for word in range(1):
            print(len(self.guess_word)* " _")
    
    def check_letters(self):            
        print("Guess word:", self.guess_word)
        self.print_underscore()
        if self.user1.letter in self.guess_word:
            print("YES")
            self.user1.attempt()
            print("Used letters:", self.user1.used_letters)
            print("Mistakes:", self.user1.mistakes)
        else:
            print("NO")
            self.user1.add_mistake()
            self.user1.attempt()
            print("Used letters:", self.user1.used_letters)
            print("Mistakes:", self.user1.mistakes)
            

        
#user1 = User()
#game = Game(user1)
#user1.introduce()
#game.random_word()
#game.print_underscore()

#user1.choose_letter()

#game.check_letters()

