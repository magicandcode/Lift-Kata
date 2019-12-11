"""https://github.com/stevecshanks/lift-kata/blob/master/tests/SmallControllerTest.php"""
from lift3 import Person, SmallLift, SmallController


def PeopleHaveArrivedAtTheirDestinations(people):
    for person in people:
        assert person.destination == person.current_floor, \
            f"Expected {person.name} to be on floor {person.destination} but they are actually on floor {person.current_floor}"



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
