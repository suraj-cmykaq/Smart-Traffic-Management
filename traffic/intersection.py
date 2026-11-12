
from traffic.road import Road
from traffic.traffic_light import TrafficLight
from traffic_exceptions import TrafficManagementError
from logger import get_logger


logger = get_logger(__name__)


class Intersection:
    """Manages roads and traffic lights at an intersection."""

    def __init__(self, intersection_id: str):
        if not isinstance(intersection_id, str) or not intersection_id.strip():
            raise ValueError("Intersection ID cannot be empty.")

        self.__intersection_id = intersection_id.strip().upper()
        self.__roads = {}
        self.__traffic_lights = {}

        logger.info(
            "Intersection %s initialized.",
            self.__intersection_id
        )

    @property
    def intersection_id(self) -> str:
        return self.__intersection_id

    @property
    def road_count(self) -> int:
        return len(self.__roads)

    @property
    def traffic_light_count(self) -> int:
        return len(self.__traffic_lights)

    def add_road(self, road: Road) -> None:
        if not isinstance(road, Road):
            raise TrafficManagementError(
                "Only Road objects can be added."
            )

        if road.road_id in self.__roads:
            raise TrafficManagementError(
                f"Road {road.road_id} already exists."
            )

        self.__roads[road.road_id] = road

        logger.info(
            "Road %s added to intersection %s.",
            road.road_id,
            self.intersection_id
        )

    def add_traffic_light(self, light: TrafficLight) -> None:
        if not isinstance(light, TrafficLight):
            raise TrafficManagementError(
                "Only TrafficLight objects can be added."
            )

        if light.light_id in self.__traffic_lights:
            raise TrafficManagementError(
                f"Traffic light {light.light_id} already exists."
            )

        self.__traffic_lights[light.light_id] = light

        logger.info(
            "Traffic light %s added to intersection %s.",
            light.light_id,
            self.intersection_id
        )

    def get_road(self, road_id: str) -> Road:
        try:
            return self.__roads[road_id.strip().upper()]
        except (KeyError, AttributeError):
            raise TrafficManagementError(
                f"Road {road_id} not found."
            ) from None

    def get_traffic_light(self, light_id: str) -> TrafficLight:
        try:
            return self.__traffic_lights[light_id.strip().upper()]
        except (KeyError, AttributeError):
            raise TrafficManagementError(
                f"Traffic light {light_id} not found."
            ) from None

    def get_all_roads(self) -> tuple:
        return tuple(self.__roads.values())

    def get_all_traffic_lights(self) -> tuple:
        return tuple(self.__traffic_lights.values())

    def get_total_vehicle_count(self) -> int:
        return sum(road.vehicle_count for road in self.__roads.values())

    def __str__(self) -> str:
        return (
            f"Intersection(ID={self.intersection_id}, "
            f"Roads={self.road_count}, "
            f"Traffic Lights={self.traffic_light_count}, "
            f"Vehicles={self.get_total_vehicle_count()})"
        )
