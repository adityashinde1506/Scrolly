import os
import time


size = 50


class Player:
    """
        Defines a basic player.
    """
    def __init__(self,
                 name="unnamed",
                 pos=0):

        self.name = name
        self.pos = pos

    def play(self, game):
        return 0


def controller(game_object, game):

    action = game_object.play(game)

    if not action:
        game_object.pos -= 1


def init_scene():
    """
        inits scene to blank space.
    """
    scene = ["_" for i in range(size)]
    return scene


def display_scene(scene):
    os.system("clear")
    print("Scrolly")
    print("\r\n"*5)
    print(" ".join(scene))


def update_scene(game_objects):
    """
        Updates state according to actions.
    """
    scene = init_scene()
    for obj in game_objects:
        scene[obj.pos] = obj.name[0]

    return scene


def loop():
    """
        Defines main game loop.
    """
    aditya = Player(pos=5, name="Aditya")
    enemy = Player(pos=0, name="Enemy")
    scene = init_scene()
    objects = [aditya, enemy]

    while 1:

        for obj in objects:

            # Control logic
            controller(game_object=obj, game=scene[:])

            # Update game
            scene = update_scene(objects)

            # Display logic
            display_scene(scene)
            time.sleep(1)


if __name__ == "__main__":
    loop()
