
import time

from traffic.traffic_light import SignalState
from patterns.traffic_observer import (
    TrafficSubject,
    TrafficEvent
)
from logger import get_logger

logger = get_logger(__name__)


class TrafficSimulator:
    """Runs and coordinates the traffic simulation."""

    def __init__(
        self,
        intersection,
        controller,
        event_manager=None,
        history_manager=None
    ):
        if controller.intersection is not intersection:
            raise ValueError(
                "Controller and simulator must use the same intersection."
            )

        self.__intersection = intersection
        self.__controller = controller
        self.__event_manager = event_manager or TrafficSubject()
        self.__history_manager = history_manager
        self.__running = False
        self.__total_cycles = 0

    @property
    def intersection(self):
        return self.__intersection

    @property
    def controller(self):
        return self.__controller

    @property
    def total_cycles(self) -> int:
        return self.__total_cycles

    @property
    def is_running(self) -> bool:
        return self.__running

    def run_cycle(self, delay: float = 0) -> dict:
        if isinstance(delay, bool) or not isinstance(delay, (int, float)):
            raise ValueError("Delay must be numeric.")

        if delay < 0:
            raise ValueError("Delay cannot be negative.")

        # Capture traffic conditions before changing the signal.
        if self.__history_manager is not None:
            self.__history_manager.capture(self.intersection)

        road_id = self.controller.select_next_road()
        road = self.intersection.get_road(road_id)

        green_time = self.controller.calculate_green_time(road_id)

        if (
            isinstance(green_time, bool)
            or not isinstance(green_time, (int, float))
            or green_time <= 0
        ):
            raise ValueError("Green time must be a positive number.")

        traffic_light = self.intersection.get_traffic_light(road_id)

        traffic_light.transition_to(SignalState.GREEN)

        self._publish_event(
            "SIGNAL_GREEN",
            f"Green signal activated for road {road_id}.",
            road_id
        )

        time.sleep(green_time)

        released_vehicle = road.remove_vehicle()

        traffic_light.transition_to(SignalState.YELLOW)

        if delay > 0:
            time.sleep(delay)

        traffic_light.transition_to(SignalState.RED)

        self.__total_cycles += 1

        result = {
            "cycle": self.total_cycles,
            "selected_road": road_id,
            "green_time": green_time,
            "released_vehicle": (
                released_vehicle.vehicle_id
                if released_vehicle else None
            ),
            "remaining_vehicles": road.vehicle_count
        }

        logger.info("Simulation cycle completed: %s", result)

        self._publish_event(
            "CYCLE_COMPLETED",
            f"Simulation cycle {self.total_cycles} completed.",
            road_id
        )

        return result

    def _publish_event(
        self,
        event_type: str,
        message: str,
        source: str
    ) -> None:
        event = TrafficEvent.create(
            event_type=event_type,
            message=message,
            source=source
        )

        self.__event_manager.notify(event)

    def run(self, cycles: int = 5, delay: float = 0) -> list:
        if isinstance(cycles, bool) or not isinstance(cycles, int):
            raise ValueError("Cycles must be an integer.")

        if cycles <= 0:
            raise ValueError("Cycles must be positive.")

        if self.__running:
            raise RuntimeError("Simulation is already running.")

        self.__running = True
        results = []

        logger.info("Traffic simulation started.")

        try:
            for _ in range(cycles):
                results.append(self.run_cycle(delay))

        except Exception:
            logger.exception("Traffic simulation encountered an error.")
            raise

        finally:
            self.__running = False
            logger.info("Traffic simulation stopped.")

        return results
