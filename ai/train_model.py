
import csv
from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


class TrafficCongestionModel:
    """Trains and evaluates a traffic congestion classifier."""

    FEATURES = [
        "vehicle_count",
        "max_capacity",
        "density_percentage",
        "emergency_count",
        "car_count",
        "bike_count",
        "bus_count",
        "emergency_vehicle_count"
    ]

    TARGET = "congestion_level"

    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            class_weight="balanced"
        )

        self.label_encoder = LabelEncoder()

    def load_dataset(self, file_path):
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {path}"
            )

        with path.open("r", newline="", encoding="utf-8") as file:
            records = list(csv.DictReader(file))

        if len(records) < 20:
            raise ValueError(
                "Dataset must contain at least 20 records."
            )

        return records

    def train(self, file_path="data/traffic_training_data.csv"):
        records = self.load_dataset(file_path)

        X = [
            [float(record[feature]) for feature in self.FEATURES]
            for record in records
        ]

        y = [
            record[self.TARGET]
            for record in records
        ]

        self.label_encoder.fit(y)
        y_encoded = self.label_encoder.transform(y)

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y_encoded,
            test_size=0.20,
            random_state=42,
            stratify=y_encoded
        )

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        print("\n======================================")
        print(" TRAFFIC CONGESTION MODEL EVALUATION")
        print("======================================")

        print(f"\nTraining records: {len(X_train)}")
        print(f"Testing records: {len(X_test)}")
        print(f"Accuracy: {accuracy * 100:.2f}%")

        print("\nClassification Report:")
        print(
            classification_report(
                y_test,
                predictions,
                labels=range(len(self.label_encoder.classes_)),
                target_names=self.label_encoder.classes_,
                zero_division=0
            )
        )

        print("Confusion Matrix:")
        print(confusion_matrix(y_test, predictions))

        return accuracy

    def save_model(self, file_path="ai/traffic_model.pkl"):
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        joblib.dump(
            {
                "model": self.model,
                "label_encoder": self.label_encoder,
                "features": self.FEATURES
            },
            path
        )

        print(f"\nModel saved successfully: {path}")


if __name__ == "__main__":
    try:
        traffic_model = TrafficCongestionModel()

        traffic_model.train()
        traffic_model.save_model()

    except (FileNotFoundError, ValueError, KeyError) as error:
        print(f"\nTraining error: {error}")
