
import unittest

from vehicles.car import Car
from vehicles.bike import Bike
from vehicles.bus import Bus
from vehicles.emergency_vehicle import EmergencyVehicle

from traffic_exceptions import InvalidVehicleError


class TestVehicles(unittest.TestCase):

    def test_car_creation(self):
        car = Car("C101", 60, seats=5)

        self.assertEqual(car.vehicle_id, "C101")
        self.assertEqual(car.speed, 60)
        self.assertEqual(car.vehicle_type, "CAR")

    def test_bike_creation(self):
        bike = Bike("B101", 45, has_pillion=True)

        self.assertEqual(bike.vehicle_type, "BIKE")
        self.assertTrue(bike.has_pillion)

    def test_bus_creation(self):
        bus = Bus("BUS101", 40, passenger_capacity=50)

        self.assertEqual(bus.vehicle_type, "BUS")
        self.assertEqual(bus.passenger_capacity, 50)

    def test_emergency_vehicle_creation(self):
        ambulance = EmergencyVehicle(
            "AMB101",
            80,
            "AMBULANCE"
        )

        self.assertEqual(ambulance.vehicle_type, "EMERGENCY")
        self.assertEqual(ambulance.get_priority(), 10)

    def test_invalid_vehicle_id(self):
        with self.assertRaises(InvalidVehicleError):
            Car("", 60)

    def test_invalid_speed(self):
        with self.assertRaises(InvalidVehicleError):
            Car("C101", -10)

    def test_invalid_emergency_type(self):
        with self.assertRaises(InvalidVehicleError):
            EmergencyVehicle("E101", 80, "UNKNOWN")

    def test_vehicle_occupancy(self):
        car = Car("C101", 60)
        bike = Bike("B101", 45)

        self.assertEqual(car.calculate_space_occupancy(), 2.5)
        self.assertEqual(bike.calculate_space_occupancy(), 1.0)


if __name__ == "__main__":
    unittest.main()
