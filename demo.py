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
        self.prev_pos = None

    def play(self, game):
        self.prev_pos = self.pos
        return 0


def controller(game_object, game):

    action = game_object.play(game)

    if not action:
        game_object.pos -= 1


def handle_collisions(game_object):
    if game_object.pos >= size or game_object.pos < 0:
        game_object.pos = game_object.prev_pos


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
    aditya = Player(pos=45, name="Aditya")
    enemy = Player(pos=15, name="Enemy")
    scene = init_scene()
    objects = [aditya, enemy]

    while 1:

        for obj in objects:

            # Control logic
            controller(game_object=obj, game=scene[:])

            # Collision logic
            handle_collisions(obj)

            # Update game
            scene = update_scene(objects)

            # Display logic
            display_scene(scene)
            time.sleep(0.1)


if __name__ == "__main__":
    loop()
