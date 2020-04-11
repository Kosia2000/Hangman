from hangman import User
from hangman import Game
from os import system


print("Nice to meet you! Welcome to Hangman!")
print("First some rules:")
print("1. You can input ONLY one letter per round")
print("2. You've got 10 chances")
print("3. Category is fruit name")

print("If You are ready to play press y [YES]")
start = input()
system('clear')

if start == 'y':
    user1 = User()
    game = Game(user1)
    user1.introduce()
    game.random_word()

    while True:
        user1.choose_letter()
        game.play_game()
else:
    print("See you next time!")

