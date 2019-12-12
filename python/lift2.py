"""https://drive.google.com/file/d/0B2hUBY7A0poaQUhYTTI5MG93a1dUNThvcGF1VmVIUmxMVE44/view"""

from enum import Enum


class ElevatorAction(Enum):
    CLOSE_DOORS = 1
    START_ENGINE_UP = 2
    START_ENGINE_DOWN = 3


class ElevatorState(Enum):
    WAITING = 0


class Lift:
    def __init__(self, total_floors):
        self.total_floors = total_floors

    def pushButton(self, floor):
        pass

    def nextAction(self):
        return ElevatorAction.CLOSE_DOORS

    def getState(self):
        pass