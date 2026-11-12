
import csv
import random
from pathlib import Path


class TrafficDatasetGenerator:
    """Generates synthetic traffic data for ML experiments."""

    ROADS = ["NORTH", "SOUTH", "EAST", "WEST"]

    def __init__(self, samples_per_road=1000, seed=42):
        self.samples_per_road = samples_per_road
        self.random = random.Random(seed)

    @staticmethod
    def classify_congestion(density):
        if density <= 20:
            return "LOW"
        elif density <= 40:
            return "MEDIUM"
        elif density <= 70:
            return "HIGH"
        return "CRITICAL"

    def generate_record(self, road_id):
        max_capacity = 50

        vehicle_count = self.random.randint(0, max_capacity)
        density = (vehicle_count / max_capacity) * 100

        emergency_count = self.random.randint(
            0, min(vehicle_count, 3)
        )

        remaining = vehicle_count - emergency_count

        car_count = self.random.randint(0, remaining)
        remaining -= car_count

        bike_count = self.random.randint(0, remaining)
        remaining -= bike_count

        bus_count = self.random.randint(0, remaining)

        label = self.classify_congestion(density)

        return {
            "road_id": road_id,
            "vehicle_count": vehicle_count,
            "max_capacity": max_capacity,
            "density_percentage": round(density, 2),
            "emergency_count": emergency_count,
            "car_count": car_count,
            "bike_count": bike_count,
            "bus_count": bus_count,
            "emergency_vehicle_count": emergency_count,
            "congestion_level": label
        }

    def generate(self):
        records = []

        for road in self.ROADS:
            for _ in range(self.samples_per_road):
                records.append(self.generate_record(road))

        self.random.shuffle(records)
        return records

    def save(self, file_path="data/traffic_training_data.csv"):
        records = self.generate()

        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=records[0].keys()
            )
            writer.writeheader()
            writer.writerows(records)

        print(f"Dataset generated successfully: {len(records)} records")
        print(f"Saved to: {path}")

        return records


if __name__ == "__main__":
    generator = TrafficDatasetGenerator(samples_per_road=1000)
    generator.save()
