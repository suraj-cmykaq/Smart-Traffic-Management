
from vehicles.emergency_vehicle import EmergencyVehicle


class TrafficDataCollector:
    """Collects machine-learning features from an intersection."""

    @staticmethod
    def collect(intersection) -> list:
        observations = []

        for road in intersection.get_all_roads():
            vehicles = road.get_vehicles()

            emergency_count = sum(
                isinstance(vehicle, EmergencyVehicle)
                for vehicle in vehicles
            )

            vehicle_type_counts = {}

            for vehicle in vehicles:
                vehicle_type = vehicle.vehicle_type

                vehicle_type_counts[vehicle_type] = (
                    vehicle_type_counts.get(vehicle_type, 0) + 1
                )

            observation = {
                "intersection_id": intersection.intersection_id,
                "road_id": road.road_id,
                "vehicle_count": road.vehicle_count,
                "max_capacity": road.max_capacity,
                "density_percentage": road.density,
                "emergency_count": emergency_count,
                "car_count": vehicle_type_counts.get("CAR", 0),
                "bike_count": vehicle_type_counts.get("BIKE", 0),
                "bus_count": vehicle_type_counts.get("BUS", 0),
                "emergency_vehicle_count": vehicle_type_counts.get(
                    "EMERGENCY", 0
                )
            }

            observations.append(observation)

        return observations
