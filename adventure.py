class AdventureGame:
    def __init__(self):
        self.current_scene = self.intro

    def intro(self):
        print("You are at the edge of a dark forest.")
        print("There is a path to your left and right.")
        print("Which way do you go? Left or Right?")
        choice = input("> ")
        if choice.lower() == "left":
            return self.left_path
        elif choice.lower() == "right":
            return self.right_path
        else:
            print("You can only choose left or right.")
            return self.intro

    def left_path(self):
        print("You go left and encounter a troll!")
        print("Do you fight or run?")
        choice = input("> ")
        if choice.lower() == "fight":
            print("You fight the troll and win!")
            return self.treasure_room
        else:
            print("You run away. Back to start.")
            return self.intro

    def right_path(self):
        print("You go right and find a treasure chest!")
        print("Do you open it?")
        choice = input("> ")
        if choice.lower() == "yes":
            return self.treasure_room
        else:
            print("You ignore the chest and walk away. Back to start.")
            return self.intro

    def treasure_room(self):
        print("You found the treasure! Congratulations, you win!")
        return self.end

    def end(self):
        print("Game Over.")
        return self.end

    def play(self):
        scene = self.current_scene
        while True:
            scene = scene()

game = AdventureGame()
game.play()
