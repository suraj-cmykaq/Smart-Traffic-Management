
from controllers.base_controller import TrafficController
from traffic_exceptions import TrafficManagementError
from logger import get_logger


logger = get_logger(__name__)


class FixedTimeController(TrafficController):
    """Controls traffic using predefined signal timings."""

    def __init__(self, intersection, green_time: int = 30):
        super().__init__(intersection)

        if isinstance(green_time, bool) or not isinstance(green_time, int):
            raise ValueError("Green time must be an integer.")

        if green_time <= 0:
            raise ValueError("Green time must be positive.")

        self.__green_time = green_time
        self.__current_index = 0

    @property
    def green_time(self) -> int:
        return self.__green_time

    def calculate_green_time(self, road_id: str) -> int:
        self.intersection.get_road(road_id)

        logger.info(
            "Fixed green time for road %s: %s seconds.",
            road_id,
            self.green_time
        )

        return self.green_time

    def select_next_road(self) -> str:
        roads = self.intersection.get_all_roads()

        if not roads:
            raise TrafficManagementError(
                "No roads available at this intersection."
            )

        selected_road = roads[self.__current_index % len(roads)]
        self.__current_index += 1

        logger.info(
            "Fixed-time controller selected road %s.",
            selected_road.road_id
        )

        return selected_road.road_id
