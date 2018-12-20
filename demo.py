import os
import time
import logging
from scrolly.Engine.controller import Controller
from scrolly.GameObjects.king import King
from scrolly.GameObjects.town import Town
from scrolly.AI.randomagent import RandomAgent
from scrolly.Engine.engine import GameEngine

size = 75


# logging.basicConfig(level=logging.DEBUG)


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


def new_loop():

    size = 10

    engine = GameEngine(size=size)
    engine.add_object(King(name="Aditya", pos=2,
                           ai=RandomAgent(), team="red"))
    engine.add_object(King(name="Enemy", pos=size-3,
                           ai=RandomAgent(), team="blue"))

    engine.add_object(Town(name="Town", pos=1, ai=None, team="red"))
    engine.add_object(Town(name="Town", pos=size-2, ai=None, team="blue"))

    while 1:
        engine.loop()


if __name__ == "__main__":
    new_loop()
