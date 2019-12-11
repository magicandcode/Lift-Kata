import enum

from attr import dataclass


class Movement(enum.Enum):
    NONE = 0
    UP = 1
    DOWN = 2


@dataclass
class Call:
    floor: int
    direction: Movement


class Lift:

    def __init__(self, floor=0):
        self.requests = []
        self.floor = floor

    def accepts_call(self, call):
        return True

    def get_next_planned_stop(self):
        pass

    def request(self, floor):
        pass