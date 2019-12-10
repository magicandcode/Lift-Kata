"""https://github.com/stevecshanks/lift-kata/blob/master/tests/SmallControllerTest.php"""

class Person:

    def __init__(self, name, queue_position, destination):
        pass


class SmallLift:

    def __init__(self, max_floor):
        pass

    def getTotalNumberOfVisits(self):
        return 0


class SmallController:

    def __init__(self, lift):
        pass

    def movePeople(self, people):
        pass


def PeopleHaveArrivedAtTheirDestinations(people):
    pass


def test_PeopleAreTakenToTheirDestinationEfficientlyWithoutExceedingCapacity():
    people = [
        Person('Robb', 0, 1),
        Person('Lyda', 1, 2),
        Person('Catharine', 1, 2),
    ]
    lift = SmallLift(1)
    controller = SmallController(lift)
    controller.movePeople(people)
    assert PeopleHaveArrivedAtTheirDestinations(people)
    assert 5 <= lift.getTotalNumberOfVisits()
