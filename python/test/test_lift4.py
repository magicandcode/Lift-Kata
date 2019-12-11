"""https://github.com/alvarogarcia7/lift-kata-kotlin/blob/master/src/test/kotlin/LiftTest.kt"""

from hamcrest import assert_that, equal_to

from lift4 import Direction, Lift


def test_queues_calls_when_not_going_the_same_direction():
    lift = Lift(0, Direction.STOPPED)

    lift = lift.calledFrom(2, Direction.UP)
    lift = lift.calledFrom(2, Direction.DOWN)

    assert_that(lift.at, equal_to(2))
    assert_that(lift.goingTo, equal_to(Direction.UP))
