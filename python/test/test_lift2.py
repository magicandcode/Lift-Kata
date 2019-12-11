"""https://drive.google.com/file/d/0B2hUBY7A0poaQUhYTTI5MG93a1dUNThvcGF1VmVIUmxMVE44/view"""

from lift2 import ElevatorAction, ElevatorState, Lift


def test_Start():
    """After pressing the button, elevator closes
    doors, and once they are closed,
    it starts the engine.
    """
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
