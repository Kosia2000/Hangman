from hangman import User
from hangman import Game
from os import system


print("Nice to meet you! Welcome to Hangman!")
print("First some rules:")
print("You've got 20 chances")

print("If you want to start game press y [YES]")
y = input()
system('clear')

if y == 'y':
    user1 = User()
    game = Game(user1)
    user1.introduce()
    game.random_word()

    for i in range(11):
        user1.choose_letter()
        game.play_game()
else:
    print("See you next time!")

