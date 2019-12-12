"""https://github.com/chgrivas/kata/blob/master/src/test/groovy/com/chgrivas/kata/playground/liftkata/LiftSpec.groovy"""

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