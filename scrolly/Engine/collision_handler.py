import logging


class CollisionHandler:
    """
        Handles collisions
    """

    def __init__(self, size):
        self.size = size
        self.logger = logging.getLogger(self.__class__.__name__)

        self.coll_types = {"c_King_King": self._kk_coll,
                           "c_King_Town": self._kt_coll}

    def _kk_coll(self, one, two):
        two.decrease_health(by=one.strength)
        one.increase_strength(by=0.01)
        one.reset_pos()

    def _kt_coll(self, one, two):
        if two.team != one.team:
            two.decrease_health(by=one.strength)
            one.increase_strength(by=1)
            one.reset_pos()

    def coll_true(self, one, two):
        """
            Checks for collisions.
        """

        return one.pos == two.pos

    def handle_collisions(self,
                          target_obj,
                          all_objs):

        pos = target_obj.pos
        if pos >= self.size or pos < 0:
            target_obj.reset_pos()

        one = target_obj.__class__.__name__

        for obj in all_objs:
            two = obj.__class__.__name__

            if obj.name == target_obj.name:
                continue

            if self.coll_true(target_obj, obj):
                self.logger.debug(f"Collision between {target_obj.name} {obj.name}")

                coll_name = f"c_{one}_{two}"
                if coll_name not in self.coll_types.keys():
                    continue

                self.coll_types[f"c_{one}_{two}"](target_obj,
                                                  obj)
