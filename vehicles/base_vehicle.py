
from abc import ABC, abstractmethod

from traffic_exceptions import InvalidVehicleError


class Vehicle(ABC):
    """
    Abstract base class representing a vehicle
    entering the smart traffic management system.
    """

    def __init__(self, vehicle_id: str, speed: float):
        self.vehicle_id = vehicle_id
        self.speed = speed

    @property
    def vehicle_id(self) -> str:
        return self.__vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise InvalidVehicleError(
                "Vehicle ID must be a non-empty string."
            )

        self.__vehicle_id = value.strip().upper()

    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, value: float):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise InvalidVehicleError("Speed must be numeric.")

        if value <= 0:
            raise InvalidVehicleError("Speed must be greater than zero.")

        self.__speed = float(value)

    @property
    @abstractmethod
    def vehicle_type(self) -> str:
        """Return the category of the vehicle."""
        pass

    @abstractmethod
    def calculate_space_occupancy(self) -> float:
        """Return the road space occupied by the vehicle."""
        pass

    def __str__(self) -> str:
        return (
            f"{self.vehicle_type} | "
            f"ID: {self.vehicle_id} | "
            f"Speed: {self.speed} km/h"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(vehicle_id={self.vehicle_id!r}, "
            f"speed={self.speed!r})"
        )
