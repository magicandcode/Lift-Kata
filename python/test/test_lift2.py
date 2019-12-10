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


def test_3Start():
    """3. After pressing the button, elevator closes doors,
    and once they are closed, it starts the engine."""
    e = Lift(7)
    e.pushButton(1)
    a = e.nextAction()
    assert a.equals(ElevatorAction.CLOSE_DOORS)
    a = e.nextAction()
    assert a.equals(ElevatorAction.START_ENGINE_UP)
    while not e.getState() == ElevatorState.WAITING:
        a = e.nextAction()
    e.pushButton(0)
    a = e.nextAction()
    assert a.equals(ElevatorAction.CLOSE_DOORS)
    a = e.nextAction()
    assert a.equals(ElevatorAction.START_ENGINE_DOWN)
