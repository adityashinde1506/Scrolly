import logging


class Controller:
    """
        Controller class. Makes changes to object locations and game states
        based on player or object actions.
    """

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.actions = {0: "left",
                        1: "right"}

    def move_left(self, obj):
        obj.change_pos(by=-1)

    def move_right(self, obj):
        obj.change_pos(by=1)

    def step(self, obj, game):
        """
            Steps through one of the object actions
        """
        action = obj.play(game)
        self.logger.debug(f"{obj} chose action {self.actions[action]}")

        if self.actions[action] == "left":
            self.move_left(obj)

        elif self.actions[action] == "right":
            self.move_right(obj)
