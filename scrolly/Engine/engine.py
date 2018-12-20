import logging
import os
import time
from scrolly.Engine.collision_handler import CollisionHandler
from scrolly.Engine.controller import Controller


def init_scene(size):
    """
        inits scene to blank space.
    """
    scene = ["_" for i in range(size)]
    return scene


def display_scene(scene, objs):
    os.system("clear")
    print("Scrolly")
    print("\r\n"*5)
    print(" ".join(scene))

    for obj in objs:
        print(f"{obj.name}: {obj.health:0.2f}, {obj.strength:0.2f}, {obj.armour}")


def update_scene(size, game_objects):
    """
        Updates state according to actions.
    """
    scene = init_scene(size)
    for obj in game_objects:
        scene[obj.pos] = obj.sprite

    return scene


class GameEngine:
    """
        Defines the basic game engine.
    """
    def __init__(self,
                 size=75):

        self.size = size
        self.game_objects = []
        self.collision_handler = CollisionHandler(size=self.size)
        self.controller = Controller()
        self.scene = init_scene(size=self.size)

        self.logger = logging.getLogger(self.__class__.__name__)

    def add_object(self,
                   obj):

        self.logger.debug(f"Adding object {obj} to engine.")
        self.game_objects.append(obj)

    def end_loop(self):
        """
            Handles end of loop processes.
        """
        for obj in self.game_objects:
            if obj.health < 0:
                self.game_objects.remove(obj)

    def loop(self):

        for obj in self.game_objects:

            # Control logic
            self.controller.step(obj=obj, game=self.scene[:])

            # Collision logic
            self.collision_handler.handle_collisions(obj,
                                                     self.game_objects)

            # End loop
            self.end_loop()

            # Update game
            self.scene = update_scene(self.size, self.game_objects)

            # Display logic
            display_scene(self.scene, self.game_objects)
            time.sleep(0.1)
