"""https://github.com/forestfart/oopKata/blob/master/src/test/java/kata/the/elevator/ElevatorTest.java"""

from enum import Enum


class Direction(Enum):
    STOPPED = 0
    UP = 1
    DOWN = 2


def floor(number):
    return number


class Elevator:
    def __init__(self, floor):
        self.floor = floor

    def currentFloor(self):
        return self.floor

    def innerElevatorRequest(self, floor):
        pass

    def run(self):
        pass

    def floorCall(self, floor, direction):
        pass

    def isStandingBy(self):
        pass