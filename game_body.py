from hangman import User
from hangman import Game


user1 = User()
game = Game(user1)
user1.introduce()
game.random_word()


for i in range(0,3):
    user1.choose_letter()
    game.check_letters()