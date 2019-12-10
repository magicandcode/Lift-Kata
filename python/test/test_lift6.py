"""https://github.com/forestfart/oopKata/blob/master/src/test/java/kata/the/elevator/ElevatorTest.java"""

from hamcrest import assert_that, equal_to


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
