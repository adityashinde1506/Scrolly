from scrolly.GameObjects.player import Player


class King(Player):
    """
        Defines king. One per faction
    """
    def __init__(self,
                 name,
                 pos,
                 ai,
                 team="blue"):

        super().__init__(name=name,
                         pos=pos,
                         ai=ai,
                         team=team,
                         health=9,
                         strength=1,
                         armour=5)

        self._money = 10

    def increase_money(self, by=1):
        self._money += (by*10)

    def decrease_money(self, by=1):
        self._money -= (by*10)

    @property
    def money(self):
        return self._money

    def play(self, game):
        self._prev_pos = self._pos
        return self._ai.play({"game": game,
                              "money": self._money})
