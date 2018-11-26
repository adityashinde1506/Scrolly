
class BaseObject:
    """
        Base object for all game objects.
    """
    def __init__(self,
                 pos,
                 name):

        self._name = name
        self._pos = pos

    def change_pos(self, by):
        self._pos += by

    def play(self, game):
        raise NotImplementedError

    @property
    def pos(self):
        return self._pos

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f"{self._name}({self._pos})"
