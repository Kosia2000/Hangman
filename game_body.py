from hangman import User
from hangman import Game


user1 = User()
game = Game(user1)
user1.introduce()
game.random_word()
game.print_underscore()

for i in range(0,9):
    user1.choose_letter()
    user1.different_letters()
    game.check_letters()
