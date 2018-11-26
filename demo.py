import os
import time
from scrolly.Engine.controller import Controller
from scrolly.GameObjects.player import Player
from scrolly.AI.randomagent import RandomAgent


size = 50


def controller(game_object, game):

    action = game_object.play(game)

    if not action:
        game_object.pos -= 1


def handle_collisions(game_object):
    if game_object.pos >= size or game_object.pos < 0:
        game_object.reset_pos()


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

    # Define controller.
    controller = Controller()

    # Define players.
    aditya = Player(pos=45,
                    name="Aditya",
                    ai=RandomAgent())

    enemy = Player(pos=15,
                   name="Enemy",
                   ai=RandomAgent())

    scene = init_scene()
    objects = [aditya, enemy]

    while 1:

        for obj in objects:

            # Control logic
            controller.step(obj=obj, game=scene[:])

            # Collision logic
            handle_collisions(obj)

            # Update game
            scene = update_scene(objects)

            # Display logic
            display_scene(scene)
            time.sleep(0.1)


if __name__ == "__main__":
    loop()
