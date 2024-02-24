class Game:
    def __init__(self):
        self.current_scene = self.intro

    def intro(self):
        print("You find yourself in a dark room with two doors. Do you go through door #1 or door #2?")
        choice = input("> ")
        if choice == "1":
            self.current_scene = self.door1
        elif choice == "2":
            self.current_scene = self.door2
        else:
            print("Invalid choice. Try again.")
            self.current_scene = self.intro

    def door1(self):
        print("You've entered a room full of gold. You're rich! The end.")
        self.current_scene = self.end

    def door2(self):
        print("You've entered a room full of spikes. You're dead! The end.")
        self.current_scene = self.end

    def end(self):
        print("Would you like to play again? (yes/no)")
        choice = input("> ")
        if choice.lower() == "yes":
            self.current_scene = self.intro
        elif choice.lower() == "no":
            print("Thanks for playing!")
            exit(0)
        else:
            print("Invalid choice. Try again.")
            self.current_scene = self.end

    def play(self):
        while True:
            self.current_scene()

game = Game()
game.play()
