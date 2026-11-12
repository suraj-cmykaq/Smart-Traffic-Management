
from controllers.base_controller import TrafficController
from traffic_exceptions import TrafficManagementError
from logger import get_logger


logger = get_logger(__name__)


class EmergencyPriorityController(TrafficController):
    """Prioritises roads containing emergency vehicles."""

    MIN_GREEN_TIME = 10
    MAX_GREEN_TIME = 60
    EMERGENCY_GREEN_TIME = 60

    def calculate_green_time(self, road_id: str) -> int:
        road = self.intersection.get_road(road_id)

        has_emergency = any(
            vehicle.vehicle_type == "EMERGENCY"
            for vehicle in road
        )

        if has_emergency:
            logger.warning(
                "Emergency vehicle detected on road %s.",
                road_id
            )
            return self.EMERGENCY_GREEN_TIME

        green_time = (
            self.MIN_GREEN_TIME
            + road.vehicle_count * 2
        )

        return min(green_time, self.MAX_GREEN_TIME)

    def select_next_road(self) -> str:
        roads = self.intersection.get_all_roads()

        if not roads:
            raise TrafficManagementError(
                "No roads available at this intersection."
            )

        emergency_roads = [
            road for road in roads
            if any(
                vehicle.vehicle_type == "EMERGENCY"
                for vehicle in road
            )
        ]

        if emergency_roads:
            selected_road = max(
                emergency_roads,
                key=lambda road: road.vehicle_count
            )

            logger.warning(
                "Emergency priority activated for road %s.",
                selected_road.road_id
            )

            return selected_road.road_id

        selected_road = max(
            roads,
            key=lambda road: road.vehicle_count
        )

        logger.info(
            "No emergency vehicles detected. "
            "Selected road %s.",
            selected_road.road_id
        )

        return selected_road.road_id
