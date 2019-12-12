"""https://github.com/alvarogarcia7/lift-kata-kotlin/blob/master/src/test/kotlin/LiftTest.kt"""

from enum import Enum


class Direction(Enum):
    STOPPED = 0
    UP = 1
    DOWN = 2


class Lift:
    def __init__(self, floor, direction):
        self.at = floor
        self.goingTo = direction

    def calledFrom(self, floor, direction):
        return self