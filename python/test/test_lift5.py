"""https://github.com/chgrivas/kata/blob/master/src/test/groovy/com/chgrivas/kata/playground/liftkata/LiftSpec.groovy"""

from behave import when, then, given
from nimoy.specification import Specification

class GreedyLiftCommandHandler:
    pass

class Building:
    def __init__(self, lowest_floor, highest_floor):
        pass

class Lift:
    def __init__(self, building, commandHandler):
        self.building = building
        self.commandHandler = commandHandler
        self.floor = 0

    def turnOn(self):
        pass

    def go(self, floor):
        pass

    def operate(self):
        pass

    def getCurrentFloor(self):
        return self.floor


class LiftTest(Specification):

    def test_lift_delivers_to_requested_floor_in_a_greedy_way(self):
        with given:
            commandHandler = GreedyLiftCommandHandler()
            building = Building(-2, 6)
            lift = Lift(building, commandHandler)
            lift.turnOn()
            lift.go(3)
            lift.go(4)
        with when:
            lift.operate()
        with then:
            assert lift.getCurrentFloor() == 3
        with when:
            lift.operate()
        with then:
            assert lift.getCurrentFloor() == 4
