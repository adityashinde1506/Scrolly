from scrolly.GameObjects.player import Player


class Town(Player):
    """
        Defines the Town hall. Makes workers. One per faction
    """
    def __init__(self,
                 name,
                 pos,
                 ai,
                 team,
                 sprite="/\\"):

        super().__init__(name=name,
                         pos=pos,
                         ai=None,
                         team=team,
                         health=9,
                         strength=1,
                         armour=9,
                         sprite=sprite)

    def play(self, game):
        return 0
