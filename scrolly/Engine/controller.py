import logging


class Controller:
    """
        Controller class. Makes changes to object locations and game states
        based on player or object actions.
    """

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.actions = {0: "nop",
                        1: "left",
                        2: "right"}

        self.king_actions = {0: "nop",
                             1: "left",
                             2: "right"}

    def move_left(self, obj):
        obj.change_pos(by=-1)

    def move_right(self, obj):
        obj.change_pos(by=1)

    def step(self, obj, game):
        """
            Steps through one of the object actions
        """
        action = obj.play(game)

        # Define actions for king.
        if obj.__class__.__name__ == "King":
            actions = self.king_actions
            self.logger.debug(f"{obj} chose action {actions[action]}")

        else:
            actions = self.actions

        if actions[action] == "left":
            self.move_left(obj)

        elif actions[action] == "right":
            self.move_right(obj)
