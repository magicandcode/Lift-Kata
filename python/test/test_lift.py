from approvaltests import verify

from lift import Lift, LiftSystem
from lift_printers import print_lifts


def test_lift_goes_to_adjacent_requested_floor():
    outputs = []
    step = '''
    |
    V
'''
    liftA = Lift("A", 0)
    lifts = LiftSystem(floors=[0,1], lifts=[liftA])

    # Initial state
    outputs.append(print_lifts(lifts))

    # Request floor
    liftA.request_floor(1)
    outputs.append(print_lifts(lifts))

    # Move one floor
    lifts.tick()
    outputs.append(print_lifts(lifts))

    # Open doors
    lifts.tick()
    outputs.append(print_lifts(lifts))

    scenario_output = step.join(outputs)
    verify(scenario_output)
