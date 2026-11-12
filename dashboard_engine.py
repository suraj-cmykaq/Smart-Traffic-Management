
from pathlib import Path

from main import build_traffic_system

from config import initialize_directories

from patterns.traffic_observer import TrafficSubject
from controllers.emergency_priority import EmergencyPriorityController
from simulation.simulator import TrafficSimulator

from ai.traffic_history import TrafficHistory
from ai.traffic_ai_service import TrafficAIService
from ai.traffic_data_collector import TrafficDataCollector


class DashboardEngine:
    """Connects the existing traffic system to the Streamlit dashboard."""

    def __init__(self):
        initialize_directories()

        # Build the existing traffic network
        self.network, self.intersection = build_traffic_system()

        # Initialize existing project components
        self.history_manager = TrafficHistory()

        self.event_manager = TrafficSubject()

        self.controller = EmergencyPriorityController(
            self.intersection
        )

        self.simulator = TrafficSimulator(
            self.intersection,
            self.controller,
            self.event_manager,
            self.history_manager
        )

        # Load the trained Random Forest model
        self.ai_service = TrafficAIService()

        self.history_path = Path("data/traffic_history.csv")

    def get_snapshot(self):
        """Collect actual traffic data and AI predictions."""

        observations = TrafficDataCollector.collect(
            self.intersection
        )

        predictions = self.ai_service.analyse_intersection(
            self.intersection
        )

        prediction_map = {
            item["road_id"]: item
            for item in predictions
        }

        roads = []

        for observation in observations:

            road_id = observation["road_id"]

            traffic_light = self.intersection.get_traffic_light(
                road_id
            )

            prediction = prediction_map[road_id]

            road_data = {
                **observation,
                "signal": traffic_light.state.value,
                "congestion": prediction["congestion_level"],
                "confidence": prediction["confidence"]
            }

            roads.append(road_data)

        total_vehicles = self.intersection.get_total_vehicle_count()

        total_emergency = sum(
            road["emergency_count"] for road in roads
        )

        average_density = (
            sum(road["density_percentage"] for road in roads)
            / len(roads)
            if roads else 0
        )

        return {
            "intersection_id": self.intersection.intersection_id,
            "total_roads": len(roads),
            "total_vehicles": total_vehicles,
            "total_emergency": total_emergency,
            "average_density": round(average_density, 2),
            "total_cycles": self.simulator.total_cycles,
            "roads": roads,
            "predictions": predictions
        }

    def run_cycle(self):
        """Execute one actual traffic simulation cycle."""

        result = self.simulator.run_cycle()

        # Persist observations collected during this cycle
        self.history_manager.save()

        return result


