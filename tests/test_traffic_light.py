
import unittest

from traffic.traffic_light import TrafficLight, SignalState
from traffic_exceptions import InvalidSignalTransitionError


class TestTrafficLight(unittest.TestCase):

    def setUp(self):
        self.light = TrafficLight("NORTH")

    def test_initial_state(self):
        self.assertEqual(self.light.state, SignalState.RED)

    def test_red_to_green(self):
        self.light.transition_to(SignalState.GREEN)

        self.assertEqual(self.light.state, SignalState.GREEN)

    def test_green_to_yellow(self):
        self.light.transition_to(SignalState.GREEN)
        self.light.transition_to(SignalState.YELLOW)

        self.assertEqual(self.light.state, SignalState.YELLOW)

    def test_yellow_to_red(self):
        self.light.transition_to(SignalState.GREEN)
        self.light.transition_to(SignalState.YELLOW)
        self.light.transition_to(SignalState.RED)

        self.assertEqual(self.light.state, SignalState.RED)

    def test_invalid_transition(self):
        with self.assertRaises(InvalidSignalTransitionError):
            self.light.transition_to(SignalState.YELLOW)

    def test_invalid_state_type(self):
        with self.assertRaises(InvalidSignalTransitionError):
            self.light.transition_to("GREEN")

    def test_green_duration(self):
        self.light.transition_to(SignalState.GREEN)

        self.assertGreater(self.light.duration, 0)


if __name__ == "__main__":
    unittest.main()
