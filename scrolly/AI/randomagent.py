from scrolly.AI.baseagent import Agent
import random
import logging


class RandomAgent(Agent):
    """
        Chooses actions randomly.
    """
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def play(self, game):
        action = random.randint(0, 2)
        self.logger.debug(f"Random Agent {self} chose {action}")
        return action
