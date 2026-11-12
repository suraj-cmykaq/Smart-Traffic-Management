
from collections import deque

from config import MAX_QUEUE_CAPACITY
from traffic_exceptions import (
    InvalidVehicleError,
    DuplicateVehicleError,
    QueueCapacityError
)
from logger import get_logger


logger = get_logger(__name__)


class Road:
    """Represents a road with a queue of waiting vehicles."""

    def __init__(
        self,
        road_id: str,
        start_point: str,
        end_point: str,
        max_capacity: int = MAX_QUEUE_CAPACITY
    ):
        if not isinstance(road_id, str) or not road_id.strip():
            raise ValueError("Road ID cannot be empty.")

        if not isinstance(start_point, str) or not start_point.strip():
            raise ValueError("Start point cannot be empty.")

        if not isinstance(end_point, str) or not end_point.strip():
            raise ValueError("End point cannot be empty.")

        if isinstance(max_capacity, bool) or not isinstance(max_capacity, int):
            raise ValueError("Maximum capacity must be an integer.")

        if max_capacity <= 0:
            raise ValueError("Maximum capacity must be positive.")

        self.__road_id = road_id.strip().upper()
        self.__start_point = start_point.strip()
        self.__end_point = end_point.strip()
        self.__max_capacity = max_capacity

        self.__vehicles = deque()
        self.__vehicle_ids = set()

        logger.info("Road %s created.", self.__road_id)

    @property
    def road_id(self) -> str:
        return self.__road_id

    @property
    def vehicle_count(self) -> int:
        return len(self.__vehicles)

    @property
    def max_capacity(self) -> int:
        return self.__max_capacity

    @property
    def is_full(self) -> bool:
        return self.vehicle_count >= self.max_capacity

    @property
    def density(self) -> float:
        return (self.vehicle_count / self.max_capacity) * 100

    def add_vehicle(self, vehicle) -> None:
        from vehicles.base_vehicle import Vehicle

        if not isinstance(vehicle, Vehicle):
            raise InvalidVehicleError(
                "Only valid Vehicle objects can enter a road."
            )

        if vehicle.vehicle_id in self.__vehicle_ids:
            raise DuplicateVehicleError(
                f"Vehicle {vehicle.vehicle_id} is already on this road."
            )

        if self.is_full:
            raise QueueCapacityError(
                f"Road {self.road_id} has reached maximum capacity."
            )

        self.__vehicles.append(vehicle)
        self.__vehicle_ids.add(vehicle.vehicle_id)

        logger.info(
            "Vehicle %s entered road %s.",
            vehicle.vehicle_id,
            self.road_id
        )

    def remove_vehicle(self):
        if not self.__vehicles:
            return None

        vehicle = self.__vehicles.popleft()
        self.__vehicle_ids.remove(vehicle.vehicle_id)

        logger.info(
            "Vehicle %s exited road %s.",
            vehicle.vehicle_id,
            self.road_id
        )

        return vehicle

    def get_vehicles(self) -> tuple:
        return tuple(self.__vehicles)

    def get_density_level(self) -> str:
        if self.vehicle_count <= 10:
            return "LOW"

        elif self.vehicle_count <= 25:
            return "MEDIUM"

        elif self.vehicle_count <= 40:
            return "HIGH"

        return "CRITICAL"

    def __len__(self) -> int:
        return self.vehicle_count

    def __iter__(self):
        return iter(tuple(self.__vehicles))

    def __str__(self) -> str:
        return (
            f"Road(ID={self.road_id}, "
            f"Vehicles={self.vehicle_count}, "
            f"Density={self.density:.1f}%)"
        )
