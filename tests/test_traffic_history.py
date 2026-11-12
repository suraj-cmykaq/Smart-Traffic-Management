
import unittest
import tempfile
from pathlib import Path

from ai.traffic_history import TrafficHistory
from traffic.intersection import Intersection
from traffic.road import Road
from vehicles.car import Car


class TestTrafficHistory(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

        self.file_path = (
            Path(self.temp_dir.name) / "traffic_history.csv"
        )

        self.intersection = Intersection("HISTORY_TEST")

        self.road = Road(
            "NORTH",
            "START",
            "END",
            max_capacity=20
        )

        self.intersection.add_road(self.road)
        self.road.add_vehicle(Car("C101", 60))

        self.history = TrafficHistory(self.file_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_capture_observations(self):
        observations = self.history.capture(self.intersection)

        self.assertEqual(len(observations), 1)
        self.assertEqual(len(self.history.records), 1)

    def test_timestamp_is_added(self):
        self.history.capture(self.intersection)

        self.assertIn("timestamp", self.history.records[0])

    def test_save_creates_csv(self):
        self.history.capture(self.intersection)
        self.history.save()

        self.assertTrue(self.file_path.exists())

    def test_save_clears_memory_records(self):
        self.history.capture(self.intersection)
        self.history.save()

        self.assertEqual(len(self.history.records), 0)


if __name__ == "__main__":
    unittest.main()
