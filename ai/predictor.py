
from pathlib import Path

import joblib


class TrafficPredictor:
    """Loads a trained model and predicts traffic congestion."""

    def __init__(self, model_path="ai/traffic_model.pkl"):
        self.model_path = Path(model_path)

        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Trained model not found: {self.model_path}"
            )

        saved_data = joblib.load(self.model_path)

        self.model = saved_data["model"]
        self.label_encoder = saved_data["label_encoder"]
        self.features = saved_data["features"]

    def predict(self, traffic_data):
        missing_features = [
            feature
            for feature in self.features
            if feature not in traffic_data
        ]

        if missing_features:
            raise ValueError(
                f"Missing traffic features: {missing_features}"
            )

        try:
            input_data = [[
                float(traffic_data[feature])
                for feature in self.features
            ]]
        except (TypeError, ValueError) as error:
            raise ValueError(
                "Traffic features must contain valid numbers."
            ) from error

        prediction = self.model.predict(input_data)[0]

        congestion_level = self.label_encoder.inverse_transform(
            [prediction]
        )[0]

        probabilities = self.model.predict_proba(input_data)[0]

        confidence = max(probabilities) * 100

        return {
            "congestion_level": congestion_level,
            "confidence": round(float(confidence), 2)
        }


if __name__ == "__main__":
    try:
        predictor = TrafficPredictor()

        sample_traffic = {
            "vehicle_count": 35,
            "max_capacity": 50,
            "density_percentage": 70.0,
            "emergency_count": 1,
            "car_count": 20,
            "bike_count": 8,
            "bus_count": 6,
            "emergency_vehicle_count": 1
        }

        result = predictor.predict(sample_traffic)

        print("\n================================")
        print(" AI TRAFFIC CONGESTION PREDICTION")
        print("================================")

        print(f"Predicted congestion: {result['congestion_level']}")
        print(f"Model confidence: {result['confidence']}%")

    except (FileNotFoundError, ValueError, KeyError) as error:
        print(f"Prediction error: {error}")
