
from traffic.intersection import Intersection
from traffic_exceptions import TrafficManagementError
from logger import get_logger


logger = get_logger(__name__)


class TrafficNetwork:
    """Manages multiple intersections in a traffic network."""

    def __init__(self, network_name: str):
        if not isinstance(network_name, str) or not network_name.strip():
            raise ValueError("Network name cannot be empty.")

        self.__network_name = network_name.strip()
        self.__intersections = {}

        logger.info(
            "Traffic network '%s' initialized.",
            self.__network_name
        )

    @property
    def network_name(self) -> str:
        return self.__network_name

    @property
    def intersection_count(self) -> int:
        return len(self.__intersections)

    def add_intersection(self, intersection: Intersection) -> None:
        if not isinstance(intersection, Intersection):
            raise TrafficManagementError(
                "Only Intersection objects can be added."
            )

        intersection_id = intersection.intersection_id

        if intersection_id in self.__intersections:
            raise TrafficManagementError(
                f"Intersection {intersection_id} already exists."
            )

        self.__intersections[intersection_id] = intersection

        logger.info(
            "Intersection %s added to network '%s'.",
            intersection_id,
            self.network_name
        )

    def get_intersection(self, intersection_id: str) -> Intersection:
        try:
            return self.__intersections[intersection_id.strip().upper()]
        except (KeyError, AttributeError):
            raise TrafficManagementError(
                f"Intersection {intersection_id} not found."
            ) from None

    def get_all_intersections(self) -> tuple:
        return tuple(self.__intersections.values())

    def get_total_vehicles(self) -> int:
        return sum(
            intersection.get_total_vehicle_count()
            for intersection in self.__intersections.values()
        )

    def get_network_status(self) -> dict:
        return {
            "network_name": self.network_name,
            "total_intersections": self.intersection_count,
            "total_vehicles": self.get_total_vehicles(),
            "intersections": {
                intersection.intersection_id: {
                    "roads": intersection.road_count,
                    "traffic_lights": intersection.traffic_light_count,
                    "vehicles": intersection.get_total_vehicle_count()
                }
                for intersection in self.__intersections.values()
            }
        }

    def __len__(self) -> int:
        return self.intersection_count

    def __str__(self) -> str:
        return (
            f"TrafficNetwork(Name={self.network_name}, "
            f"Intersections={self.intersection_count}, "
            f"Vehicles={self.get_total_vehicles()})"
        )
