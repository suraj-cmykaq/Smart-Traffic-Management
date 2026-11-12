
import unittest

from traffic.road import Road
from traffic.intersection import Intersection
from traffic.traffic_light import TrafficLight

from vehicles.car import Car
from vehicles.emergency_vehicle import EmergencyVehicle

from controllers.fixed_time import FixedTimeController
from controllers.density_based import DensityBasedController
from controllers.emergency_priority import EmergencyPriorityController


class TestTrafficControllers(unittest.TestCase):

    def setUp(self):
        self.intersection = Intersection("TEST_INTERSECTION")

        self.north = Road("NORTH", "A", "B")
        self.south = Road("SOUTH", "C", "D")

        self.intersection.add_road(self.north)
        self.intersection.add_road(self.south)

        self.intersection.add_traffic_light(TrafficLight("NORTH"))
        self.intersection.add_traffic_light(TrafficLight("SOUTH"))

    def test_fixed_time_controller(self):
        controller = FixedTimeController(
            self.intersection,
            green_time=30
        )

        self.assertEqual(
            controller.calculate_green_time("NORTH"),
            30
        )

    def test_density_based_controller(self):
        self.north.add_vehicle(Car("C101", 60))
        self.north.add_vehicle(Car("C102", 50))

        controller = DensityBasedController(self.intersection)

        self.assertEqual(
            controller.calculate_green_time("NORTH"),
            14
        )

    def test_density_controller_selects_busiest_road(self):
        self.north.add_vehicle(Car("C101", 60))
        self.north.add_vehicle(Car("C102", 50))
        self.south.add_vehicle(Car("C103", 40))

        controller = DensityBasedController(self.intersection)

        self.assertEqual(controller.select_next_road(), "NORTH")

    def test_emergency_priority(self):
        self.south.add_vehicle(
            EmergencyVehicle("AMB101", 80, "AMBULANCE")
        )

        controller = EmergencyPriorityController(self.intersection)

        self.assertEqual(
            controller.select_next_road(),
            "SOUTH"
        )

        self.assertEqual(
            controller.calculate_green_time("SOUTH"),
            60
        )


if __name__ == "__main__":
    unittest.main()
