
import unittest

from ai.traffic_data_collector import TrafficDataCollector
from traffic.intersection import Intersection
from traffic.road import Road
from vehicles.car import Car
from vehicles.bike import Bike
from vehicles.emergency_vehicle import EmergencyVehicle


class TestTrafficDataCollector(unittest.TestCase):

    def setUp(self):
        self.intersection = Intersection("TEST_CROSSROAD")

        self.road = Road(
            "NORTH",
            "START",
            "END",
            max_capacity=20
        )

        self.intersection.add_road(self.road)

        self.road.add_vehicle(Car("C101", 60))
        self.road.add_vehicle(Bike("B101", 40))
        self.road.add_vehicle(
            EmergencyVehicle("AMB101", 80, "AMBULANCE")
        )

    def test_vehicle_count(self):
        data = TrafficDataCollector.collect(self.intersection)

        self.assertEqual(data[0]["vehicle_count"], 3)

    def test_density_percentage(self):
        data = TrafficDataCollector.collect(self.intersection)

        self.assertEqual(data[0]["density_percentage"], 15.0)

    def test_emergency_vehicle_count(self):
        data = TrafficDataCollector.collect(self.intersection)

        self.assertEqual(data[0]["emergency_count"], 1)

    def test_vehicle_type_counts(self):
        data = TrafficDataCollector.collect(self.intersection)

        self.assertEqual(data[0]["car_count"], 1)
        self.assertEqual(data[0]["bike_count"], 1)
        self.assertEqual(data[0]["emergency_vehicle_count"], 1)
        self.assertEqual(data[0]["bus_count"], 0)


if __name__ == "__main__":
    unittest.main()
