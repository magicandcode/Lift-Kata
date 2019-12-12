from lift3 import Person, SmallLift, SmallController


def PeopleHaveArrivedAtTheirDestinations(people):
    for p in people:
        assert p.destination == p.current_floor, \
            f"Expected {p.name} to be on floor {p.destination} but they are actually on floor {p.current_floor}"


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
