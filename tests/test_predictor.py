
import unittest
from unittest.mock import patch, MagicMock

from ai.predictor import TrafficPredictor


class TestTrafficPredictor(unittest.TestCase):

    def setUp(self):
        self.mock_model = MagicMock()
        self.mock_encoder = MagicMock()

        self.mock_model.predict.return_value = [2]
        self.mock_model.predict_proba.return_value = [
            [0.01, 0.02, 0.95, 0.02]
        ]

        self.mock_encoder.inverse_transform.return_value = [
            "HIGH"
        ]

        self.saved_data = {
            "model": self.mock_model,
            "label_encoder": self.mock_encoder,
            "features": [
                "vehicle_count",
                "max_capacity",
                "density_percentage",
                "emergency_count",
                "car_count",
                "bike_count",
                "bus_count",
                "emergency_vehicle_count"
            ]
        }

    @patch("ai.predictor.joblib.load")
    @patch("ai.predictor.Path.exists", return_value=True)
    def test_model_loading(self, mock_exists, mock_load):
        mock_load.return_value = self.saved_data

        predictor = TrafficPredictor()

        self.assertIsNotNone(predictor.model)
        self.assertIsNotNone(predictor.label_encoder)

    @patch("ai.predictor.joblib.load")
    @patch("ai.predictor.Path.exists", return_value=True)
    def test_successful_prediction(self, mock_exists, mock_load):
        mock_load.return_value = self.saved_data

        predictor = TrafficPredictor()

        traffic_data = {
            "vehicle_count": 35,
            "max_capacity": 50,
            "density_percentage": 70,
            "emergency_count": 1,
            "car_count": 20,
            "bike_count": 8,
            "bus_count": 6,
            "emergency_vehicle_count": 1
        }

        result = predictor.predict(traffic_data)

        self.assertEqual(result["congestion_level"], "HIGH")
        self.assertEqual(result["confidence"], 95.0)

    @patch("ai.predictor.joblib.load")
    @patch("ai.predictor.Path.exists", return_value=True)
    def test_missing_features(self, mock_exists, mock_load):
        mock_load.return_value = self.saved_data

        predictor = TrafficPredictor()

        with self.assertRaises(ValueError):
            predictor.predict({
                "vehicle_count": 20
            })

    @patch("ai.predictor.joblib.load")
    @patch("ai.predictor.Path.exists", return_value=True)
    def test_invalid_numeric_values(self, mock_exists, mock_load):
        mock_load.return_value = self.saved_data

        predictor = TrafficPredictor()

        traffic_data = {
            "vehicle_count": "invalid",
            "max_capacity": 50,
            "density_percentage": 70,
            "emergency_count": 1,
            "car_count": 20,
            "bike_count": 8,
            "bus_count": 6,
            "emergency_vehicle_count": 1
        }

        with self.assertRaises(ValueError):
            predictor.predict(traffic_data)


if __name__ == "__main__":
    unittest.main()
