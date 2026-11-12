
import unittest
from unittest.mock import patch

from simulation.simulator import TrafficSimulator
from traffic.traffic_light import SignalState


class TestTrafficSimulator(unittest.TestCase):

    def setUp(self):
        from traffic.intersection import Intersection
        from traffic.road import Road
        from traffic.traffic_light import TrafficLight
        from controllers.fixed_time import FixedTimeController
        from patterns.vehicle_factory import VehicleFactory

        self.intersection = Intersection("TEST_SIMULATION")

        road = Road("NORTH","START","END")
        self.intersection.add_road(road)

        self.intersection.add_traffic_light(
            TrafficLight("NORTH")
        )

        vehicle = VehicleFactory.create_vehicle(
            "CAR",
            vehicle_id="C101",
            speed=60
        )

        road.add_vehicle(vehicle)

        self.controller = FixedTimeController(self.intersection)

        self.simulator = TrafficSimulator(
            self.intersection,
            self.controller
        )

    @patch("simulation.simulator.time.sleep")
    def test_run_cycle(self, mock_sleep):
        result = self.simulator.run_cycle()

        self.assertEqual(result["selected_road"], "NORTH")
        self.assertEqual(result["released_vehicle"], "C101")
        self.assertEqual(result["remaining_vehicles"], 0)
        self.assertEqual(self.simulator.total_cycles, 1)

        mock_sleep.assert_called_once()

    @patch("simulation.simulator.time.sleep")
    def test_run_multiple_cycles(self, mock_sleep):
        results = self.simulator.run(cycles=2)

        self.assertEqual(len(results), 2)
        self.assertEqual(self.simulator.total_cycles, 2)
        self.assertFalse(self.simulator.is_running)

    def test_invalid_cycles(self):
        with self.assertRaises(ValueError):
            self.simulator.run(cycles=0)

    def test_negative_delay(self):
        with self.assertRaises(ValueError):
            self.simulator.run_cycle(delay=-1)

    def test_simulation_running_status(self):
        self.assertFalse(self.simulator.is_running)


if __name__ == "__main__":
    unittest.main()
