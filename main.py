
from traffic.road import Road
from traffic.intersection import Intersection
from traffic.traffic_light import TrafficLight
from traffic.traffic_network import TrafficNetwork

from patterns.vehicle_factory import VehicleFactory
from patterns.traffic_observer import (
    TrafficSubject,
    LoggingObserver,
    ConsoleObserver
)

from controllers.emergency_priority import EmergencyPriorityController
from simulation.simulator import TrafficSimulator

from storage.data_manager import DataManager
from ai.traffic_history import TrafficHistory
from ai.traffic_ai_service import TrafficAIService

from logger import get_logger
from config import initialize_directories


logger = get_logger(__name__)


def build_traffic_system():
    """Create and configure the complete traffic network."""

    intersection = Intersection("JAIN_CROSSROAD")

    road_north = Road("NORTH", "North Gate", "Central Road")
    road_south = Road("SOUTH", "South Gate", "Central Road")
    road_east = Road("EAST", "East Gate", "Central Road")
    road_west = Road("WEST", "West Gate", "Central Road")

    roads = [
        road_north,
        road_south,
        road_east,
        road_west
    ]

    for road in roads:
        intersection.add_road(road)
        intersection.add_traffic_light(
            TrafficLight(road.road_id)
        )

    # Add ordinary vehicles
    road_north.add_vehicle(
        VehicleFactory.create_vehicle("CAR", "C101", 60)
    )

    road_north.add_vehicle(
        VehicleFactory.create_vehicle("BIKE", "B101", 45)
    )

    road_south.add_vehicle(
        VehicleFactory.create_vehicle(
            "BUS", "BUS101", 40,
            passenger_capacity=50
        )
    )

    road_east.add_vehicle(
        VehicleFactory.create_vehicle("CAR", "C102", 55)
    )

    road_east.add_vehicle(
        VehicleFactory.create_vehicle("CAR", "C103", 50)
    )

    # Add emergency vehicle
    road_west.add_vehicle(
        VehicleFactory.create_vehicle(
            "EMERGENCY",
            "AMB101",
            80,
            emergency_type="AMBULANCE"
        )
    )

    network = TrafficNetwork("SMART_CITY_TRAFFIC_NETWORK")
    network.add_intersection(intersection)

    return network, intersection


def main():
    """Run the AI-powered Smart Traffic Management System."""

    try:
        initialize_directories()

        print("\n" + "=" * 60)
        print("       SMART TRAFFIC MANAGEMENT SYSTEM")
        print("=" * 60)

        network, intersection = build_traffic_system()

        # Register event observers
        event_manager = TrafficSubject()
        event_manager.attach(LoggingObserver())
        event_manager.attach(ConsoleObserver())

        # Select emergency-priority strategy
        controller = EmergencyPriorityController(intersection)

        # Initialize traffic history
        history_manager = TrafficHistory()

        # Initialize AI service
        ai_service = TrafficAIService()

        # Perform AI congestion analysis
        print("\n" + "=" * 60)
        print("       INITIAL AI TRAFFIC ANALYSIS")
        print("=" * 60)

        predictions = ai_service.analyse_intersection(intersection)

        ai_service.display_predictions(predictions)

        # Initialize simulator
        simulator = TrafficSimulator(
            intersection,
            controller,
            event_manager,
            history_manager
        )

        print("\nINITIAL NETWORK STATUS")
        print("-" * 60)

        for road in intersection.get_all_roads():
            print(road)

        print("\n" + "=" * 60)
        print("STARTING TRAFFIC SIMULATION")
        print("=" * 60)

        results = simulator.run(cycles=5)

        print("\nSIMULATION RESULTS")
        print("-" * 60)

        for result in results:
            print(result)

        # Perform AI analysis after simulation
        print("\n" + "=" * 60)
        print("       FINAL AI TRAFFIC ANALYSIS")
        print("=" * 60)

        final_predictions = ai_service.analyse_intersection(
            intersection
        )

        ai_service.display_predictions(final_predictions)

        # Save historical observations
        history_manager.save()

        print("\nTraffic history saved successfully.")

        # Save JSON report
        report = network.get_network_status()
        report["simulation_cycles"] = simulator.total_cycles
        report["simulation_results"] = results
        report["initial_ai_predictions"] = predictions
        report["final_ai_predictions"] = final_predictions

        DataManager.save_json(report)

        # Export road information
        road_records = [
            {
                "road_id": road.road_id,
                "vehicle_count": road.vehicle_count,
                "density_percentage": round(road.density, 2),
                "density_level": road.get_density_level()
            }
            for road in intersection.get_all_roads()
        ]

        DataManager.export_csv(
            road_records,
            "data/road_report.csv"
        )

        print("\n" + "=" * 60)
        print("SIMULATION COMPLETED SUCCESSFULLY")
        print("=" * 60)

        print("\nFinal network status:")
        print(network)

        print("\nReports saved:")
        print("- data/traffic_data.json")
        print("- data/road_report.csv")
        print("- data/traffic_history.csv")
        print("- ai/traffic_model.pkl")
        print("- logs/traffic_management.log")

    except Exception as error:
        logger.exception("Application failed: %s", error)
        print(f"\nApplication Error: {error}")


if __name__ == "__main__":
    main()
