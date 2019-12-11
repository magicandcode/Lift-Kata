"""https://github.com/forestfart/oopKata/blob/master/src/test/java/kata/the/elevator/ElevatorTest.java"""
from enum import Enum

from hamcrest import assert_that, equal_to


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


def test_current_floor_monitor_displays_current_level():
    # Given
    elevator = Elevator(floor(2))
    
    # When
    currentLevelDisplayStep0 = elevator.currentFloor()
    elevator.innerElevatorRequest(floor(3))
    elevator.run()
    currentLevelDisplayStep1 = elevator.currentFloor()
    elevator.innerElevatorRequest(floor(4))
    elevator.run()
    currentLevelDisplayStep2 = elevator.currentFloor()
    elevator.innerElevatorRequest(floor(0))
    elevator.run()
    currentLevelDisplayStep3 = elevator.currentFloor()
    
    # Then
    assert_that(currentLevelDisplayStep0, equal_to(floor(2)))
    assert_that(currentLevelDisplayStep1, equal_to(floor(3)))
    assert_that(currentLevelDisplayStep2, equal_to(floor(4)))
    assert_that(currentLevelDisplayStep3, equal_to(floor(0)))


def test_elevator_will_move_up_and_down_then_standby_until_next_move_down_and_up():
        # Given
        elevator = Elevator(floor(0))

        # When
        elevator.floorCall(floor(56), Direction.DOWN)
        elevator.run()
        elevator.innerElevatorRequest(floor(0))
        isStandby1 = elevator.isStandingBy()
        standbyFloor1 = elevator.currentFloor()
        elevator.floorCall(floor(-5), Direction.UP)
        elevator.run()
        elevator.innerElevatorRequest(floor(26))
        elevator.run()
        isStandby2 = elevator.isStandingBy()
        standbyFloor2 = elevator.currentFloor()

        # Then
        assert_that(isStandby1, equal_to(False))
        assert_that(standbyFloor1, equal_to(floor(56)))
        assert_that(isStandby2, equal_to(True))
        assert_that(standbyFloor2, equal_to(floor(26)))