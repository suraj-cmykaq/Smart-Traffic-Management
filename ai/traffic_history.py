
from datetime import datetime
from pathlib import Path

from ai.traffic_data_collector import TrafficDataCollector
from storage.data_manager import DataManager


class TrafficHistory:
    """Collects and stores historical traffic observations."""

    def __init__(self, file_path="data/traffic_history.csv"):
        self.file_path = Path(file_path)
        self.records = []

    def capture(self, intersection):
        observations = TrafficDataCollector.collect(intersection)

        timestamp = datetime.now().isoformat(timespec="seconds")

        for observation in observations:
            record = observation.copy()
            record["timestamp"] = timestamp
            self.records.append(record)

        return observations

    def save(self):
        if not self.records:
            raise ValueError("No traffic observations available to save.")

        existing_records = []

        if self.file_path.exists():
            existing_records = DataManager.import_csv(self.file_path)

        combined_records = existing_records + self.records

        DataManager.export_csv(
            combined_records,
            self.file_path
        )

        self.records.clear()
