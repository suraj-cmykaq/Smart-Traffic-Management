
from controllers.base_controller import TrafficController
from traffic_exceptions import TrafficManagementError
from logger import get_logger


logger = get_logger(__name__)


class DensityBasedController(TrafficController):
    """Adjusts signal timing according to traffic density."""

    MIN_GREEN_TIME = 10
    MAX_GREEN_TIME = 60
    TIME_PER_VEHICLE = 2

    def calculate_green_time(self, road_id: str) -> int:
        road = self.intersection.get_road(road_id)

        vehicle_count = road.vehicle_count

        green_time = (
            self.MIN_GREEN_TIME
            + vehicle_count * self.TIME_PER_VEHICLE
        )

        green_time = min(
            green_time,
            self.MAX_GREEN_TIME
        )

        logger.info(
            "Density-based timing for road %s: %s seconds "
            "(%s vehicles).",
            road_id,
            green_time,
            vehicle_count
        )

        return green_time

    def select_next_road(self) -> str:
        roads = self.intersection.get_all_roads()

        if not roads:
            raise TrafficManagementError(
                "No roads available at this intersection."
            )

        selected_road = max(
            roads,
            key=lambda road: road.vehicle_count
        )

        logger.info(
            "Density-based controller selected road %s "
            "with %s vehicles.",
            selected_road.road_id,
            selected_road.vehicle_count
        )

        return selected_road.road_id
