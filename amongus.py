import random

class Player:
    def __init__(self, role):
        self.role = role

class Game:
    def __init__(self):
        roles = ['Crewmate', 'Impostor']
        random.shuffle(roles)
        self.players = [Player(role) for role in roles]

    def play(self):
        while True:
            print("What do you want to do?")
            print("1. Guess who the impostor is")
            print("2. Complete a task")
            print("3. Call a meeting")
            action = input("> ")
            if action == "1":
                self.guess_impostor()
            elif action == "2":
                self.complete_task()
            elif action == "3":
                self.call_meeting()
            else:
                print("Invalid action. Try again.")

    def guess_impostor(self):
        guess = input("Who do you think the impostor is? ")
        if guess.lower() == 'impostor':
            print("Congratulations! You found the impostor!")
            return True
        else:
            print("Sorry, that's not correct.")
            return False

    def complete_task(self):
        print("You completed a task!")

    def call_meeting(self):
        print("A meeting has been called.")
        if self.guess_impostor():
            print("The crewmates win!")
        else:
            print("The impostor wins!")

game = Game()
game.play()
