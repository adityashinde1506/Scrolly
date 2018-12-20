import logging
from scrolly.GameObjects.baseobject import BaseObject


class Player(BaseObject):
    """
        Defines a basic player.
    """
    def __init__(self,
                 name,
                 pos,
                 ai,
                 team="blue",
                 health=9,
                 strength=1,
                 armour=1,
                 sprite=None):

        self.logger = logging.getLogger(__class__.__name__)

        super().__init__(pos=pos, name=name)
        self._prev_pos = None
        self._team = team
        self._health = health
        self._strength = strength
        self._armour = armour
        self._ai = ai

        if sprite is None:
            self._sprite = self._name[0]
        else:
            self._sprite = sprite

    def reset_pos(self):
        """
            Resets pos to prev_pos in case of hard collisions.
        """
        self._pos = self._prev_pos

    def decrease_health(self, by):
        self._health -= (by/self._armour)

    def increase_strength(self, by):

        self._strength += by
        self.logger.debug(f"Strength for {self._name} increased {self._strength}")

        if self._strength > 9:
            self.logger.debug(f"Strength overflow for {self._name}")
            self._strength = 9

    def decrease_strength(self, by):
        self._strength -= by
        self.logger.debug(f"Strength for {self._name} decreased {self._strength}")

        if self._strength <= 0:
            self.logger.debug(f"Strength underflow for {self._name}")
            self._strength = 0.1

    def increase_armour(self, by):
        self._armour += by
        self.logger.debug(f"Armour for {self._name} increased {self._armour}")

        if self._armour > 9:
            self.logger.debug(f"Armour overflow for {self._name}")
            self._armour = 9

    def decrease_armour(self, by):
        self._armour -= by
        self.logger.debug(f"Armour for {self._name} decreased {self._armour}")

        if self._armour <= 0:
            self.logger.debug(f"Armour underflow for {self._name}")
            self._armour = 0.1

    @property
    def health(self):
        return self._health

    @property
    def strength(self):
        return self._strength

    @property
    def armour(self):
        return self._armour

    @property
    def _id(self):
        return f"{self.name}_{self.team}"

    @property
    def team(self):
        return self._team

    @property
    def sprite(self):
        return self._sprite

    def play(self, game):
        self._prev_pos = self._pos
        return self._ai.play(game)
