class Game:
    def __init__(self):
        self.current_scene = self.start_scene()

    def start_scene(self):
        return 'intro'

    def next_scene(self, scene_name):
        scenes = {
            'intro': self.intro,
            'forest': self.forest,
            'cave': self.cave,
            'castle': self.castle,
            'game_over': self.game_over
        }
        return scenes.get(scene_name)

    def play(self):
        while True:
            print("\n--------")
            scene_method = self.next_scene(self.current_scene)
            self.current_scene = scene_method()

    def intro(self):
        print("You are standing in a dark forest. There is a path to your left and right.")
        action = input("> ")
        if action == "left":
            return 'cave'
        elif action == "right":
            return 'castle'
        else:
            return 'game_over'

    def forest(self):
        # Implement the forest scene
        pass

    def cave(self):
        # Implement the cave scene
        pass

    def castle(self):
        # Implement the castle scene
        pass

    def game_over(self):
        print("You have lost the game. Better luck next time!")
        return 'game_over'


game = Game()
game.play()
