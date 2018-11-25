import os
import time


size = 10


def init_scene():
    """
        inits scene to blank space.
    """
    scene = ["_" for i in range(size)]
    return scene


def display_scene(scene):
    os.system("clear")
    print("Scrolly")
    print("\r\n"*10)
    print(" ".join(scene))


def loop():
    """
        Defines main game loop.
    """
    while 1:

        scene = init_scene()
        display_scene(scene)
        time.sleep(1)


if __name__ == "__main__":
    loop()
