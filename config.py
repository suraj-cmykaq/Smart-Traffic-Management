from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Directory configuration
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

# File paths
TRAFFIC_DATA_FILE = DATA_DIR / "traffic_data.json"
LOG_FILE = LOG_DIR / "traffic_system.log"

# Simulation configuration
MAX_QUEUE_CAPACITY = 50
DEFAULT_GREEN_TIME = 30
DEFAULT_YELLOW_TIME = 5
DEFAULT_RED_TIME = 35

# Traffic density thresholds
LOW_DENSITY = 10
MEDIUM_DENSITY = 25
HIGH_DENSITY = 40

# Vehicle priorities
VEHICLE_PRIORITIES = {
    "CAR": 1,
    "BIKE": 2,
    "BUS": 3,
    "EMERGENCY": 4
}


def initialize_directories():
    """Create required project directories if they do not exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)