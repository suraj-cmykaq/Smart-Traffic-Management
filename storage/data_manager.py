
import json
import csv
from pathlib import Path

from config import TRAFFIC_DATA_FILE, initialize_directories
from traffic_exceptions import DataPersistenceError
from logger import get_logger


logger = get_logger(__name__)


class DataManager:
    """Handles JSON and CSV data persistence."""

    @staticmethod
    def save_json(data, file_path=TRAFFIC_DATA_FILE):
        try:
            initialize_directories()

            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)

            with path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

            logger.info("JSON data saved to %s.", path)

        except (OSError, TypeError, ValueError) as error:
            logger.exception("Failed to save JSON data.")
            raise DataPersistenceError(
                f"Could not save JSON data: {error}"
            ) from error

    @staticmethod
    def load_json(file_path=TRAFFIC_DATA_FILE):
        try:
            path = Path(file_path)

            with path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            logger.info("JSON data loaded from %s.", path)
            return data

        except (OSError, json.JSONDecodeError) as error:
            logger.exception("Failed to load JSON data.")
            raise DataPersistenceError(
                f"Could not load JSON data: {error}"
            ) from error

    @staticmethod
    def export_csv(records, file_path):
        try:
            records = list(records)

            if not records:
                raise DataPersistenceError(
                    "Cannot export an empty dataset."
                )

            if not all(isinstance(record, dict) for record in records):
                raise DataPersistenceError(
                    "Every CSV record must be a dictionary."
                )

            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)

            fieldnames = list(records[0].keys())

            if not fieldnames:
                raise DataPersistenceError(
                    "CSV records must contain fields."
                )

            with path.open(
                "w",
                newline="",
                encoding="utf-8"
            ) as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames,
                    extrasaction="ignore"
                )

                writer.writeheader()
                writer.writerows(records)

            logger.info("CSV data exported to %s.", path)

        except (OSError, csv.Error, TypeError, ValueError) as error:
            logger.exception("Failed to export CSV data.")
            raise DataPersistenceError(
                f"Could not export CSV data: {error}"
            ) from error

    @staticmethod
    def import_csv(file_path):
        try:
            path = Path(file_path)

            with path.open(
                "r",
                newline="",
                encoding="utf-8"
            ) as file:
                reader = csv.DictReader(file)
                records = list(reader)

            if not reader.fieldnames:
                raise DataPersistenceError(
                    "CSV file has no header row."
                )

            logger.info(
                "%s records imported from %s.",
                len(records),
                path
            )

            return records

        except (OSError, csv.Error) as error:
            logger.exception("Failed to import CSV data.")
            raise DataPersistenceError(
                f"Could not import CSV data: {error}"
            ) from error
