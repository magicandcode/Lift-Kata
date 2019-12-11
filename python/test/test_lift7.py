from lift7 import Movement, Call, Lift


def test_idle_lift_accepts_call():
    lift = Lift(floor=0)
    accepts_call = lift.accepts_call(Call(floor=3, direction=Movement.DOWN))
    assert accepts_call
    assert 3 == lift.get_next_planned_stop()


def test_busy_lift_rejects_call():
    lift = Lift(floor=0)
    lift.accepts_call(Call(floor=3, direction=Movement.DOWN))
    accepts_call = lift.accepts_call(Call(floor=2, direction=Movement.UP))
    assert not accepts_call
    assert 3 == lift.get_next_planned_stop()


def test_idle_lift_accepts_passenger_request():
    lift = Lift(floor=0)
    lift.request(floor=3)
    assert 3 == lift.get_next_planned_stop()


def test_idle_lift_accepts_several_passenger_requests():
    lift = Lift(floor=0)
    lift.request(floor=3)
    lift.request(floor=5)
    assert lift.get_next_planned_stop() == 3
    assert 5 in lift.requests
