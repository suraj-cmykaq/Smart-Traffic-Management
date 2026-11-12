
import unittest
from unittest.mock import patch, MagicMock

from traffic.road import Road
from traffic.intersection import Intersection
from ai.traffic_ai_service import TrafficAIService


class TestTrafficAIService(unittest.TestCase):

    def setUp(self):
        self.intersection = Intersection("AI_TEST_INTERSECTION")

        north = Road("NORTH", "North Gate", "Central Road")
        south = Road("SOUTH", "South Gate", "Central Road")

        self.intersection.add_road(north)
        self.intersection.add_road(south)

    @patch("ai.traffic_ai_service.TrafficPredictor")
    def test_analyse_all_roads(self, mock_predictor):
        mock_instance = MagicMock()

        mock_instance.predict.return_value = {
            "congestion_level": "LOW",
            "confidence": 99.0
        }

        mock_predictor.return_value = mock_instance

        service = TrafficAIService()

        predictions = service.analyse_intersection(
            self.intersection
        )

        self.assertEqual(len(predictions), 2)

        self.assertEqual(
            predictions[0]["congestion_level"],
            "LOW"
        )

        self.assertEqual(
            predictions[1]["congestion_level"],
            "LOW"
        )

        self.assertEqual(
            mock_instance.predict.call_count,
            2
        )

    @patch("ai.traffic_ai_service.TrafficPredictor")
    def test_prediction_contains_road_information(
        self,
        mock_predictor
    ):
        mock_instance = MagicMock()

        mock_instance.predict.return_value = {
            "congestion_level": "HIGH",
            "confidence": 95.0
        }

        mock_predictor.return_value = mock_instance

        service = TrafficAIService()

        predictions = service.analyse_intersection(
            self.intersection
        )

        self.assertEqual(
            predictions[0]["intersection_id"],
            "AI_TEST_INTERSECTION"
        )

        self.assertEqual(
            predictions[0]["road_id"],
            "NORTH"
        )

        self.assertIn("vehicle_count", predictions[0])
        self.assertIn("density_percentage", predictions[0])
        self.assertIn("confidence", predictions[0])


if __name__ == "__main__":
    unittest.main()
